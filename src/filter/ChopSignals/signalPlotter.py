import pandas as pd
import numpy as np
import copy
import plotly.express as px
import plotly.graph_objects as go
from ipywidgets import Output
from typing import List, Dict


class SignalPlotter:
    
    def __init__(self, files_path: str, output: Output):
        self.files_path = files_path
        self.output = output
        self.channels = ['Fp1', 'Fp2', 'C3', 'C4', 'P7', 'P8', 'O1', 'O2']
        
        self.csv_file = None
        self.channel = None
        self.df = None
        self.figs = None
        self.currentFig = None


    def load_signal(self, csv_file: str, channel: str):
        self.csv_file = csv_file
        self.channel = channel
        self.df = pd.read_csv(f'{self.files_path}/{self.csv_file}', delimiter=',')
        self.figs = {channel:self.__create_fig__(channel) for channel in self.channels}
        self.currentFig = self.figs['Fp1']
    
    
    def change_current_fig(self, channel: str):
        self.currentFig = self.figs[channel]
    
    
    def plot_signal(self, intervals: List[Dict[str,float]]):
        fig = copy.deepcopy(self.currentFig)
        
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


    def __create_fig__(self, channel: str) -> go.Figure:
        channel_data = self.df[channel].to_numpy()
        timestamps = self.df['Timestamp'].to_numpy()
        fig = px.line(x=timestamps, y=channel_data)
        return fig