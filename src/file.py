import os 
import shutil
from enum import Enum


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

    @staticmethod
    def get_data_from_bucket():
        '''
            #!/bin/bash
            gsutil cp -r gs://dataset_eeg_cafe2022 ./
        '''
        pass



class Paths:
    class Resources(Enum):
        RAW = 0
        RENAMED = 1
        FORMATTED = 2
        TRUNCATED = 3
        TRUNC_JSONS = 4

    __resource_paths = {
        0: 'dataset_eeg_cafe2022/raw',
        1: 'dataset_eeg_cafe2022/renamed',
        2: 'dataset_eeg_cafe2022/formatted',
        3: 'dataset_eeg_cafe2022/truncated',
        4: 'assets/trunc_intervals'
    }

    @staticmethod
    def get_resource_path(resource: Resources) -> str:
        file_directory = os.dirname(__file__)
        project_directory = os.realpath(os.join(file_directory, '..', '..'))
        return join(project_directory, Paths.__resource_paths[resource.value])

