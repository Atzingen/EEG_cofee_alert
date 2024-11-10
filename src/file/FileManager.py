import os 
import shutil

from src.setup.Paths import Paths


class FileManager:
    @staticmethod
    def __create_path_if_not_exists(path: str) -> None:
        if not os.path.exists(path):
            os.mkdir(path)

    @staticmethod
    def rename_raw_files():
        raw = Paths.get_resource_path(Paths.Resources.RAW)
        renamed = Paths.get_resource_path(Paths.Resources.RENAMED)

        signal_types = ["alpha", "chimp", "seq", "react"]
        exp_numbers = list(range(1, 22))
        coffee_signal_numbers = list(range(1, 3))

        FileManager.__create_path_if_not_exists(renamed)

        for sig_t in signal_types:
            for exp in exp_numbers:
                try:
                    shutil.copyfile(
                        f"{raw}/main-session_{sig_t}-{exp}_formatted.csv",
                        f"{renamed}/{sig_t}_{exp}.csv"
                    )
                except Exception as e:
                    print(e)
                    continue

        for cff_sn in coffee_signal_numbers:
            for exp in exp_numbers:
                try:
                    shutil.copyfile(
                        f"{raw}/main-session_cafe-{exp}_{cff_sn}_formatted.csv",
                        f"{renamed}/cafe-{cff_sn}_{exp}.csv"
                    )
                except Exception as e:
                    print(e)
                    continue

    @staticmethod
    def write_csvs_in(path, data_frames, filenames):
        if len(data_frames) == 0:
            raise Exception('[ERROR] Cannot write files by empty list!')

        FileManager.__create_path_if_not_exists(path)

        for index, df in enumerate(data_frames):
            df.to_csv(f'{path}/{filenames[index]}')

