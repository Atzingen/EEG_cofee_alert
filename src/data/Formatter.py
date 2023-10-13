import pandas as pd

# Type this file

class Formatter:
    def __init__(self, dfs):
        self.raw_dfs = dfs
        self.formatted_dfs = []


    def set_initial_and_final_timestamps(self):
        for df in self.raw_dfs:
            df['Timestamp'] = df['Timestamp'] - df['Timestamp'].min()


    def remove_other_columns(self):
        for df in self.raw_dfs:
            other_columns = df.columns.to_list()[10:23]
            other_columns.append('other.13')
            other_columns.append('Unnamed: 0')
            other_columns.append('Timestamp (Formatted)')

            df = df.drop(labels=other_columns, axis=1)

            self.formatted_dfs.append(df)


    #REMOVE THIS
    def write_filtered_csvs(self, file_names):
        if len(self.formatted_dfs) == 0:
            raise Exception('[ERROR] Cannot write files by empty list! Format DFs first.')

        for index, df in enumerate(self.formatted_dfs):
            df.to_csv(f'dataset_eeg_cafe2022/formatted/{file_names[index]}')

