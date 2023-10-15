from os.path import dirname, join, realpath
from enum import Enum


class Paths:
    class Resources(Enum):
        RAW = 0
        RENAMED = 1
        FORMATTED = 2
        TRUNCATED = 3

    __resource_paths = {
        0: 'dataset_eeg_cafe2022/raw',
        1: 'dataset_eeg_cafe2022/renamed',
        2: 'dataset_eeg_cafe2022/formatted',
        3: 'dataset_eeg_cafe2022/truncated'
    }


    @staticmethod
    def get_resource_path(resource: Resources) -> str:
        file_directory = dirname(__file__)
        project_directory = realpath(join(file_directory, '..', '..'))
        return join(project_directory, Paths.__resource_paths[resource.value])
