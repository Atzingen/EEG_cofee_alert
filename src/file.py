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
        "continuous": "dataset_eeg_cafe2022/continuous",
        "truncation_intervals": "assets/truncation_intervals"
    }
    __signal_types = ["alpha", "cafe", "chimp", "seq", "react"]
    __coffee_type_numbers = list(range(1, 3))
    __experiment_numbers = list(range(1, 22))

    @staticmethod
    def __create_path_if_not_exists(path: str) -> None:
        if not os.path.exists(path):
            os.mkdir(path)

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

    @classmethod
    def get_files_from(cls, resource: str) -> List[str]:
        return [file for file \
                in os.listdir(cls.get_path_by(resource_name=resource))]

    @classmethod
    def get_path_by(cls, resource_name: str) -> Path:
        return Path(cls.__project_path, cls.__resource_paths[resource_name])

    @classmethod
    def rename_raw_files(cls):
        raw = cls.__resource_paths["raw"]
        renamed = cls.__resource_paths["renamed"]

        cls.__create_path_if_not_exists(renamed)

        for sig_t in cls.__signal_types:
            if sig_t == "cafe":
                continue

            for exp in cls.__experiment_numbers:
                try:
                    shutil.copyfile(
                        f"{raw}/main-session_{sig_t}-{exp}_formatted.csv",
                        f"{renamed}/{sig_t}_{exp}.csv"
                    )
                except Exception as e:
                    print(e)
                    continue

        for cff_t in cls.__coffee_type_numbers:
            for exp in cls.__experiment_numbers:
                try:
                    shutil.copyfile(
                        f"{raw}/main-session_cafe-{exp}_{cff_t}_formatted.csv",
                        f"{renamed}/cafe-{cff_t}_{exp}.csv"
                    )
                except Exception as e:
                    print(e)
                    continue

