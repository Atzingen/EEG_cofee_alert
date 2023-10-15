import pandas as pd
import numpy as np
import copy
import plotly.express as px
import plotly.graph_objects as go
from ipywidgets import Output
from typing import List, Dict

from src.data.trunc_intervals import TruncIntervals

'''
    Corta todos os sinais de um DataFrame por canal de 
    acordo com um arquivo extra de timestamps.
'''
class Truncate:
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


    # remove this, use FileManager
    def save_data(self, save_path: str):
        self.df.to_csv(f'{save_path}/{self.csv_filename}')


    def __replace_with_nan(self, start, end, channel_name):
        self.df.loc[(self.df['Timestamp'] >= start) & (self.df['Timestamp'] <= end), channel_name] = np.nan


'''
    Responsável pela criação das figuras e gráficos dos sinais
'''
class Plotter:
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


