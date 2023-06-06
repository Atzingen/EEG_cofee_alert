from typing import List, Tuple
import pandas as pd

class ChopSignalsLogic:
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
        # Isso não corta automaticamente outros canais em que o sinal possa estar bom?
        for t1, t2 in self.fp1:
            self.csv_df = self.__chop_signal(t1, t2)
        for t1, t2 in self.fp2:
            self.csv_df = self.__chop_signal(t1, t2)
        for t1, t2 in self.c3:
            self.csv_df = self.__chop_signal(t1, t2)
        for t1, t2 in self.c4:
            self.csv_df = self.__chop_signal(t1, t2)
        for t1, t2 in self.p7:
            self.csv_df = self.__chop_signal(t1, t2)
        for t1, t2 in self.p8:
            self.csv_df = self.__chop_signal(t1, t2)
        for t1, t2 in self.o1:
            self.csv_df = self.__chop_signal(t1, t2)
        for t1, t2 in self.o2:
            self.csv_df = self.__chop_signal(t1, t2)


    def __chop_signal(self, t1, t2):
        return self.csv_df.loc[(self.csv_df['Timestamp'] >= t1) & (self.csv_df['Timestamp'] <= t2)]

