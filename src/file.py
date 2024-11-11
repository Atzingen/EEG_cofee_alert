import pandas as pd
import os 
import shutil
from pathlib import Path
from typing import List


class File:
    __source_path = Path(__file__).parent.resolve()
    __project_path = Path(__source_path).parent.resolve()

    __resource_paths = {
        "raw": "dataset_eeg_cafe2022/raw",
        "renamed": "dataset_eeg_cafe2022/renamed",
        "formatted": "dataset_eeg_cafe2022/formatted",
        "truncated": "dataset_eeg_cafe2022/truncated",
        "truncation_intervals": "assets/truncation_intervals"
    }

    @staticmethod
    def __create_path_if_not_exists(path: str) -> None:
        if not os.path.exists(path):
            os.mkdir(path)

    @classmethod
    def get_path_by(cls, resource_name: str) -> Path:
        return Path(cls.__project_path, cls.__resource_paths[resource_name])

    @classmethod
    def rename_raw_files(cls):
        raw = cls.__resource_paths["raw"]
        renamed = cls.__resource_paths["renamed"]

        signal_types = ["alpha", "chimp", "seq", "react"]
        exp_numbers = list(range(1, 22))
        coffee_signal_numbers = list(range(1, 3))

        cls.__create_path_if_not_exists(renamed)

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
    def write_dataframes_in(path: str,
                            dataframes: List[pd.DataFrame],
                            filenames: List[str]):
        if len(dataframes) == 0:
            raise Exception('[ERROR] Cannot write files by empty list!')

        File.__create_path_if_not_exists(path)

        for index, df in enumerate(dataframes):
            df.to_csv(f'{path}/{filenames[index]}')

    @staticmethod
    def get_data_from_bucket():
        '''
            #!/bin/bash
            gsutil cp -r gs://dataset_eeg_cafe2022 ./
        '''
        pass

