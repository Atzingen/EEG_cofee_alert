from intervals import Intervals
import pandas as pd
import numpy as np

'''
    Corta todos os sinais de um DataFrame por canal de acordo com um arquivo extra de timestamps.
'''

class SinalChopper:
    def __init__(self, files_path: str):
        self.files_path = files_path
        self.channels = ['Fp1', 'Fp2', 'C3', 'C4', 'P7', 'P8', 'O1', 'O2']

        self.df = None
        self.intervals = Intervals()


    def set_chopper(self, csv_file: str):
        self.df = pd.read_csv(f'{self.files_path}/{csv_file}', delimiter=',')
        self.intervals.load_cutting_intervals(csv_file)


    def perform_chop(self):
        for channel in self.channels:
            for interval in self.intervals.get_cutting_intervals(channel):
                self.__chop_signal__(interval['start'], interval['end'], channel)


    def __chop_signal__(self, start, end, channel_name):
        self.df.loc[(self.df['Timestamp'] >= start) & (self.df['Timestamp'] <= end), channel_name] = np.nan
