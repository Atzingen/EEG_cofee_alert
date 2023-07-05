from typing import List, Tuple
import pandas as pd
import numpy as np

'''
    Corta todos os sinais de um DataFrame por canal de acordo com um arquivo extra de timestamps.
'''

class SinalChopper:
    def __init__(self, df):
        self.csv_df = df
        self.fp1: List[Tuple[float, float]] = []
        self.fp2: List[Tuple[float, float]] = []
        self.c3: List[Tuple[float, float]] = []
        self.c4: List[Tuple[float, float]] = []
        self.p7: List[Tuple[float, float]] = []
        self.p8: List[Tuple[float, float]] = []
        self.o1: List[Tuple[float, float]] = []
        self.o2: List[Tuple[float, float]] = []


    def populate_timestamps(self, timestamps_file: str, separator: str):
        df = pd.read_csv(timestamps_file, sep=separator)

        for column in df.columns:
            if column == 'fp1':
                self.fp1 = [tuple(map(float, cell.split(','))) for cell in df[column] if not pd.isna(cell)]
            elif column == 'fp2':
                self.fp2 = [tuple(map(float, cell.split(','))) for cell in df[column] if not pd.isna(cell)]
            elif column == 'c3':
                self.c3 = [tuple(map(float, cell.split(','))) for cell in df[column] if not pd.isna(cell)]
            elif column == 'c4':
                self.c4 = [tuple(map(float, cell.split(','))) for cell in df[column] if not pd.isna(cell)]
            elif column == 'p7':
                self.p7 = [tuple(map(float, cell.split(','))) for cell in df[column] if not pd.isna(cell)]
            elif column == 'p8':
                self.p8 = [tuple(map(float, cell.split(','))) for cell in df[column] if not pd.isna(cell)]
            elif column == 'o1':
                self.o1 = [tuple(map(float, cell.split(','))) for cell in df[column] if not pd.isna(cell)]
            elif column == 'o2':
                self.o2 = [tuple(map(float, cell.split(','))) for cell in df[column] if not pd.isna(cell)]


    def perform_chop(self):
        for t1, t2 in self.fp1:
            self.__chop_signal(t1, t2, 'fp1')
        for t1, t2 in self.fp2:
            self.__chop_signal(t1, t2, 'fp2')
        for t1, t2 in self.c3:
            self.__chop_signal(t1, t2, 'c3')
        for t1, t2 in self.c4:
            self.__chop_signal(t1, t2, 'c4')
        for t1, t2 in self.p7:
            self.__chop_signal(t1, t2, 'p7')
        for t1, t2 in self.p8:
            self.__chop_signal(t1, t2, 'p8')
        for t1, t2 in self.o1:
            self.__chop_signal(t1, t2, 'o1')
        for t1, t2 in self.o2:
            self.__chop_signal(t1, t2, 'o2')


    def __chop_signal(self, t1, t2, channel_name):
        self.csv_df.loc[(self.csv_df['Timestamp'] >= t1) & (self.csv_df['Timestamp'] <= t2), channel_name] = np.nan

