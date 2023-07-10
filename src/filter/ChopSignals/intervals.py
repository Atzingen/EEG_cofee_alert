import json
from typing import List, Dict


class Intervals:
    
    def __init__(self, files_path: str):
        self.files_path = files_path
        self.channels = ['Fp1', 'Fp2', 'C3', 'C4', 'P7', 'P8', 'O1', 'O2']
        
        self.filename = None
        self.cutting_intervals = None

        
    def load_cutting_intervals(self, csv_file):
        self.filename = csv_file.strip('.csv')
        self.cutting_intervals = {channel: [] for channel in self.channels}
        try:
            with open(f'cuttingIntervals/chop_{self.filename}.json', 'r') as file:
                self.cutting_intervals = json.load(file)
        except FileNotFoundError:
                self.cutting_intervals = {channel: [] for channel in self.channels}


    def save_cutting_intervals(self):
            with open(f'cuttingIntervals/chop_{self.filename}.json', 'w') as file:
                json.dump(self.cutting_intervals, file)

                
    def add_interval(self, channel: str, start: float, end: float):
        self.cutting_intervals[channel].append({'start': start, 'end': end})


    def pop_interval(self, channel: str):
        self.cutting_intervals[channel].pop()

        
    def get_cutting_intervals(self, channel: str) -> List[Dict[str,float]]:
        return self.cutting_intervals[channel]