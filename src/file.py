from pathlib import Path
from typing import List, Tuple
from math import floor
from random import Random
import pandas as pd
import os 
import shutil


class File:
    __source_path = Path(__file__).parent.resolve()
    __project_path = Path(__source_path).parent.resolve()
    __resource_paths = {
        "raw": "dataset_eeg_cafe2022/raw",
        "renamed": "dataset_eeg_cafe2022/renamed",
        "formatted": "dataset_eeg_cafe2022/formatted",
        "truncated": "dataset_eeg_cafe2022/truncated",
        "continuous": "dataset_eeg_cafe2022/continuous",
        "pre_training": "dataset_eeg_cafe2022/pre_training",
        "truncation_intervals": "assets/truncation_intervals",
        "pre_calculated_truncation_intervals": "assets/pre_calculated_truncation_intervals"
    }
    __signal_types = ["alpha", "cafe-1", "cafe-2", "chimp", "seq", "react"]
    __experiment_numbers = list(range(1, 22))

    @staticmethod
    def create_path_if_not_exists(path: Path) -> None:
        if not path.exists():
            os.makedirs(name=str(path), exist_ok=True)

    @staticmethod
    def get_data_from_bucket():
        '''
            #!/bin/bash
            gsutil cp -r gs://dataset_eeg_cafe2022 ./
        '''
        pass

    @classmethod
    def write_dataframes_in(cls,
                            path: str,
                            dataframes: List[pd.DataFrame],
                            filenames: List[str]) -> None:
        if len(dataframes) == 0:
            return

        cls.create_path_if_not_exists(Path(path))

        for index, df in enumerate(dataframes):
            df.to_csv(f'{path}/{filenames[index]}')

    @classmethod
    def get_files_from(cls, resource: str, subdirs: str = "") -> List[str]:
        return [file for file \
                in os.listdir(cls.get_path_by(resource=resource, subdirs=subdirs))]

    @classmethod
    def get_path_by(cls, resource: str, subdirs: str = "") -> Path:
        return Path(cls.__project_path,
                    cls.__resource_paths[resource],
                    subdirs)

    @classmethod
    def rename_raw_files(cls) -> None:
        raw = cls.get_path_by(resource="raw")
        renamed = cls.get_path_by(resource="renamed")

        cls.create_path_if_not_exists(renamed)

        for sig_t in cls.__signal_types:
            raw_file_format = \
                "main-session_{sig_t}-{exp}_formatted.csv" \
                if not sig_t.startswith("cafe") \
                else "main-session_cafe-{exp}_{coffee_number}_formatted.csv"
            coffee_number = 1 if sig_t == "cafe-1" else 2

            for exp in cls.__experiment_numbers:
                raw_file = raw_file_format.format(sig_t=sig_t,
                                                  exp=exp,
                                                  coffee_number=coffee_number)
                try:
                    shutil.copyfile(
                        f"{raw}/{raw_file}",
                        f"{renamed}/{sig_t}_{exp}.csv"
                    )
                except Exception:
                    continue

    @classmethod
    def _create_train_test_file_structure_in(cls, parent_dir: Path) -> None:
        cls.create_path_if_not_exists(path=parent_dir)

        dirs_by_signal_type = [d if not d.endswith(("-1", "-2")) else "cafe" \
                               for d in cls.__signal_types]

        for sig_t in dirs_by_signal_type:
            for inner_dir in ["train", "test"]:
                dest_path = Path(parent_dir,
                                 f"{sig_t}/{inner_dir}")

                cls.create_path_if_not_exists(path=dest_path)

    @classmethod
    def _randomize(cls,
                   files: List[str],
                   test_proportion: float = 0.3,
                   seed: int = 42) -> Tuple[List[str], List[str]]:
        randomizer = Random()
        randomizer.seed(a=seed)

        randomizer.shuffle(files)

        test_amount = floor(test_proportion * len(files))
        train_amount = len(files) - test_amount

        return (files[:train_amount], files[train_amount:])

    @classmethod
    def _copy_train_test_files_from(cls,
                                    origin: Path,
                                    to: Path,
                                    samples: Tuple[List[str], List[str]]) \
                                    -> None:
        (train, test) = samples

        for file in train:
            src = Path(origin, file)
            dst = Path(to, "train", file)

            shutil.copy(src=src, dst=dst)

        for file in test:
            src = Path(origin, file)
            dst = Path(to, "test", file)

            shutil.copy(src=src, dst=dst)

    @classmethod
    def generate_train_test_files(cls) -> None:
        continuous = cls.get_path_by(resource="continuous")
        pre_training = cls.get_path_by(resource="pre_training")

        cls._create_train_test_file_structure_in(parent_dir=pre_training)

        files = [file for file in os.listdir(continuous)]

        for sig_t in cls.__signal_types:
            sig_t_files = [file for file in files if file.startswith(sig_t)]

            cls._copy_train_test_files_from(
                origin=continuous,
                to=Path(pre_training,
                          sig_t if not sig_t.startswith("cafe") else "cafe"),
                samples=cls._randomize(files=sig_t_files)
            )

    @classmethod
    def add_not_fragmented_files_to_continuous(cls) -> None:
        formatted = cls.get_files_from(resource="formatted")
        truncated = cls.get_files_from(resource="truncated")

        formatted_path = cls.get_path_by(resource="formatted")
        continuous_path = cls.get_path_by(resource="continuous")

        missing_files = list(set(formatted) - set(truncated))

        for file in missing_files:
            shutil.copy(src=Path(formatted_path, file),
                        dst=Path(continuous_path, file))

