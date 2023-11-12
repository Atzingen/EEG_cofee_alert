import os 

class FileManager:
    @classmethod
    def rename_raw_files(cls):
        signal_types = ["alpha","chimp","seq","react"]
        exp_numbers = list(range(1,22))


        for sig_t in signal_types:
            for exp in exp_numbers:
                try:
                    os.rename(f"main-session_{sig_t}-{exp}_formatted.csv",f"{sig_t}_{exp}.csv")
                except OSError:
                    continue

        for coffee_signal_number in range(1,3):
            for exp in exp_numbers:
                try:
                    os.rename(f"main-session_cafe-{exp}_{coffee_signal_number}_formatted.csv",f"cafe-{coffee_signal_number}_{exp}.csv")
                except OSError:
                    continue


    @staticmethod
    def write_csvs_in_path(path, dfs, filenames):
        if len(dfs) == 0:
            raise Exception('[ERROR] Cannot write files by empty list!')

        if not os.path.exists(path): 
            os.mkdir(path)

        for index, df in enumerate(dfs):
            df.to_csv(f'{path}/{filenames[index]}')


