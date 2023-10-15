import json
from typing import List, Dict


class TruncIntervals:
    def __init__(self, trunc_intervals_path: str):
        self.channels = ['Fp1', 'Fp2', 'C3', 'C4', 'P7', 'P8', 'O1', 'O2']
        self.trunc_intervals_path = trunc_intervals_path
        
        self.filename = None
        self.file_intervals = None

        
    def load_cutting_intervals(self, csv_file):
        self.filename = csv_file.replace('.csv','')
        self.file_intervals = {channel: [] for channel in self.channels}
        
        try:
            with open(f'{self.trunc_intervals_path}/chop_{self.filename}.json', 'r') as file:
                self.file_intervals = json.load(file)
        except FileNotFoundError:
                self.file_intervals = {channel: [] for channel in self.channels}


    def save_cutting_intervals(self):
            with open(f'{self.trunc_intervals_path}/chop_{self.filename}.json', 'w') as file:
                json.dump(self.file_intervals, file)

                
    def add_interval(self, channel: str, start: float, end: float):
        self.file_intervals[channel].append({'start': start, 'end': end})


    def pop_interval(self, channel: str):
        self.file_intervals[channel].pop()

        
    def get_cutting_intervals(self, channel: str) -> List[Dict[str,float]]:
        return self.file_intervals[channel]


