from ipywidgets import Output
from typing import List, Dict, Optional
from pathlib import Path
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import os
import copy
import json

from src.file import File


class Formatter:
    @staticmethod
    def normalize_timestamps_for(dfs: List[pd.DataFrame]):
        normalized_dfs = []

        for df in dfs:
            df['Timestamp'] = df['Timestamp'] - df['Timestamp'].min()
            normalized_dfs.append(df)

        return normalized_dfs


    @staticmethod
    def remove_other_columns_for(dfs: List[pd.DataFrame]):
        formatted_dfs = []

        for df in dfs:
            other_columns = df.columns.to_list()[10:23]
            other_columns.append('other.13')
            other_columns.append('Unnamed: 0')
            other_columns.append('Timestamp (Formatted)')

            formatted_dfs.append(df.drop(labels=other_columns, axis=1))

        return formatted_dfs


class Truncate:
    """
        Corta todos os sinais de um DataFrame por canal de 
        acordo com um arquivo extra de timestamps.
    """
    def __init__(self, files_path: str, trunc_intervals_path):
        self.files_path = files_path
        self.channels = ['Fp1', 'Fp2', 'C3', 'C4', 'P7', 'P8', 'O1', 'O2']

        self.df = None
        self.trunc_intervals = TruncateIntervals(trunc_intervals_path)
        self.csv_filename = None


    def setup_by_filename(self, csv_filename: str):
        self.csv_filename = csv_filename
        self.df = pd.read_csv(f'{self.files_path}/{csv_filename}', delimiter=',')
        self.trunc_intervals.load_file_intervals(csv_filename)


    def truncate(self):
        for channel in self.channels:
            for interval in self.trunc_intervals.get_channel_intervals(channel):
                self.__replace_with_nan(interval['start'], interval['end'], channel)

        return self.df


    def __replace_with_nan(self, start, end, channel_name):
        self.df.loc[(self.df['Timestamp'] >= start) & (self.df['Timestamp'] <= end), channel_name] = np.nan


class Plotter:
    """
        Responsável pela criação das figuras e gráficos dos sinais
    """
    def __init__(self, files_path: str, output: Output):
        self.files_path = files_path
        self.output = output
        self.channels = ['Fp1', 'Fp2', 'C3', 'C4', 'P7', 'P8', 'O1', 'O2']
        
        self.csv_filename = None
        self.channel = None
        self.df = None
        self.figs = None
        self.current_fig = None


    def load_signal(self, filename: str, channel: str):
        self.csv_filename = filename
        self.channel = channel
        self.df = pd.read_csv(f'{self.files_path}/{self.csv_filename}', delimiter=',')
        self.figs = {channel : self.__create_fig(channel) for channel in self.channels}
        self.current_fig = self.figs[channel]
    
    
    def change_current_fig(self, channel: str):
        self.channel = channel
        self.current_fig = self.figs[channel]
    
    
    def plot_signal(self, intervals: List[Dict[str,float]] = []):
        fig = copy.deepcopy(self.current_fig)
        
        fig.update_layout(title = f"{self.csv_filename.replace('.csv','')} - {self.channel}")
        
        if len(intervals) != 0:
            for interval in intervals:
                start = interval['start']
                end = interval['end']
                fig.add_shape(type="rect",
                              xref="x",
                              yref="paper",
                              x0=start,
                              y0=0,
                              x1=end,
                              y1=1,
                              fillcolor="orange",
                              opacity=0.3,
                              layer="below",
                              line=dict(width=0))

        with self.output:
            self.output.clear_output()
            fig.show()
            print(f"xf = {fig.data[0].x.tolist()[-1]}")


    def __create_fig(self, channel: str) -> go.Figure:
        channel_data = self.df[channel].to_numpy()
        timestamps = self.df['Timestamp'].to_numpy()
        fig = px.line(x = timestamps, y = channel_data)
        
        return fig


class TruncateIntervals:
    """
    A classe `TruncateIntervals` gerencia arquivos de corte de intervalos para diferentes canais de dados.
    
    Args:
        truncate_intervals_path (str): Caminho para o diretório onde os arquivos de intervalos de corte (JSON) são armazenados.
    """

    def __init__(self, truncate_intervals_path: str) -> None:
        self.channels: List[str] = ['Fp1', 'Fp2', 'C3', 'C4', 'P7', 'P8', 'O1', 'O2']
        self.trunc_intervals_path: str = truncate_intervals_path
        
        self.__filename: Optional[str] = None
        self.__file_intervals: Dict[str, List[Dict[str, float]]] = None

        File.create_path_if_not_exists(path=Path(truncate_intervals_path))

    def load_file_intervals(self, csv_file_path: str) -> None:
        """
        Carrega os intervalos de um arquivo JSON correspondente a um arquivo CSV fornecido.
        Se o arquivo JSON não existir, cria uma estrutura de dados vazia para cada canal.
        
        Args:
            csv_file_path (str): Caminho para o arquivo CSV utilizado para determinar o nome do arquivo JSON de intervalos.
        """
        self.__filename = os.path.basename(csv_file_path).replace('.csv', '')
        
        try:
            with open(f'{self.trunc_intervals_path}/{self.__filename}.json', 'r') as file:
                self.__file_intervals = json.load(file)
        except FileNotFoundError:
            self.__file_intervals = {channel: [] for channel in self.channels}

    def save_current_file_intervals(self) -> None:
        """
        Salva os intervalos de corte atuais em um arquivo JSON com base no nome do arquivo carregado.
        """
        with open(f'{self.trunc_intervals_path}/{self.__filename}.json', 'w') as file:
            json.dump(self.__file_intervals, file)

    def add_interval_by_channel(self, channel: str, start: float, end: float) -> None:
        """
        Adiciona um novo intervalo de corte para um canal específico.
        
        Args:
            channel (str): Nome do canal.
            start (float): Início do intervalo.
            end (float): Fim do intervalo.
        """
        self.__file_intervals[channel].append({'start': start, 'end': end})

    def pop_interval_by_channel(self, channel: str) -> None:
        """
        Remove o último intervalo de corte de um canal específico.
        
        Args:
            channel (str): Nome do canal.
        """
        self.__file_intervals[channel].pop()

    def get_channel_intervals(self, channel: str) -> List[Dict[str, float]]:
        """
        Retorna a lista de intervalos de corte para um canal específico.
        
        Args:
            channel (str): Nome do canal.
        
        Returns:
            List[Dict[str, float]]: Lista de dicionários com os intervalos de início e fim para o canal.
        """
        return self.__file_intervals[channel]


class Continuous:
    """
    A classe `Continuous` é responsável por transformar arquivos de dados truncados em
    múltiplos arquivos contínuos com base em intervalos definidos em arquivos JSON.

    Args:
        input_data_path (str): Caminho para os arquivos de dados truncados.
        output_data_path (str): Local onde os segmentos contínuos serão salvos.
        truncate_intervals_path (str): Caminho para os arquivos de intervalos de corte.
    """

    def __init__(self, input_data_path: str, output_data_path: str, truncate_intervals_path: str) -> None:
        self.input_data_path: str = input_data_path
        self.output_data_path: str = output_data_path
        self.truncate_intervals: TruncateIntervals = TruncateIntervals(truncate_intervals_path)

    def process_file(self, csv_file_path: str) -> None:
        """
        Processa um arquivo de dados truncados, segmentando-o em arquivos contínuos
        com base nos intervalos unificados definidos em todos os canais.

        Args:
            csv_file_path (str): Caminho para o arquivo CSV de dados.
        """
        self.truncate_intervals.load_file_intervals(csv_file_path)

        data = pd.read_csv(f'{self.input_data_path}/{csv_file_path}')

        all_intervals = self._unify_intervals()

        if all_intervals:
            self._split_and_save_excluding_intervals(data,
                                                     all_intervals,
                                                     csv_file_path)

    def _unify_intervals(self) -> list:
        """
        Unifica os intervalos de todos os canais para gerar uma lista geral de cortes.

        Returns:
            list: Lista de intervalos unificados, com cada elemento sendo um dicionário {'start': float, 'end': float}.
        """
        unified_intervals = []
        for channel in self.truncate_intervals.channels:
            channel_intervals = self.truncate_intervals.get_channel_intervals(channel)
            unified_intervals.extend(channel_intervals)

        unified_intervals = sorted(unified_intervals, key=lambda x: x['start'])
        merged_intervals = []
        for interval in unified_intervals:
            if not merged_intervals or interval['start'] > merged_intervals[-1]['end']:
                merged_intervals.append(interval)
            else:
                merged_intervals[-1]['end'] = max(merged_intervals[-1]['end'], interval['end'])

        return merged_intervals

    def _split_and_save_excluding_intervals(self, data: pd.DataFrame, intervals: list, csv_file_path: str) -> None:
        """
        Divide os dados em segmentos que estão fora dos intervalos fornecidos.

        Args:
            data (pd.DataFrame): DataFrame com os dados originais.
            intervals (list): Lista de intervalos com 'start' e 'end'.
            csv_file_path (str): Caminho do arquivo de entrada.
        """
        base_filename = csv_file_path.replace('.csv', '')
        valid_segments = []
        current_start = 0

        for interval in intervals:
            start, end = interval['start'], interval['end']

            if current_start < start:
                segment = data[(data['Timestamp'] >= current_start) & (data['Timestamp'] < start)].copy()
                if len(segment) > 1:
                    valid_segments.append(segment)

            current_start = end

        if current_start < data['Timestamp'].iloc[-1]:
            segment = data[data['Timestamp'] >= current_start].copy()
            if len(segment) > 1:
                valid_segments.append(segment)

        for idx, segment in enumerate(valid_segments):
            output_filename = f'{base_filename}_{idx + 1}.csv'
            segment.to_csv(f'{self.output_data_path}/{output_filename}', index=False)

