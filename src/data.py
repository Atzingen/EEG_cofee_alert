import pandas as pd
import numpy as np
import copy
import plotly.express as px
import plotly.graph_objects as go
from ipywidgets import Output
from typing import List, Dict
import json


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
        self.trunc_intervals = TruncIntervals(trunc_intervals_path)
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

class TruncIntervals:
    def __init__(self, trunc_intervals_path: str):
        self.channels = ['Fp1', 'Fp2', 'C3', 'C4', 'P7', 'P8', 'O1', 'O2']
        self.trunc_intervals_path = trunc_intervals_path
        
        self.filename = None
        self.file_intervals = None

        
    def load_file_intervals(self, csv_file):
        self.filename = csv_file.replace('.csv','')
        self.file_intervals = {channel: [] for channel in self.channels}
        
        try:
            with open(f'{self.trunc_intervals_path}/{self.filename}.json', 'r') as file:
                self.file_intervals = json.load(file)
        except FileNotFoundError:
                self.file_intervals = {channel: [] for channel in self.channels}


    def save_current_file_intervals(self):
            with open(f'{self.trunc_intervals_path}/{self.filename}.json', 'w') as file:
                json.dump(self.file_intervals, file)

                
    def add_interval_by_channel(self, channel: str, start: float, end: float):
        self.file_intervals[channel].append({'start': start, 'end': end})


    def pop_interval_by_channel(self, channel: str):
        self.file_intervals[channel].pop()

        
    def get_channel_intervals(self, channel: str) -> List[Dict[str,float]]:
        return self.file_intervals[channel]


