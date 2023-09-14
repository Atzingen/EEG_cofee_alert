import os
from signalChopper import SignalChopper

files_path = 'dataset_eeg_cafe2022/RenamedFiles'
chop_files_path = 'src/filter/ChopSignals/cuttingIntervals'
save_path = 'src/data/treatedSignalFiles'
channels = ['Fp1', 'Fp2', 'C3', 'C4', 'P7', 'P8', 'O1', 'O2']

def main():

    chop_files = [file for file in os.listdir(chop_files_path) if '.json' in file]
    csv_files = [file.replace('chop_','').replace('.json','.csv') for file in chop_files]

    signalChopper = SignalChopper(files_path, chop_files_path)

    for file in csv_files:
       signalChopper.set_chopper(file)
       signalChopper.perform_chop()
       signalChopper.save_data(save_path)

if __name__ == '__main__':
    main()