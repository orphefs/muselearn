from muselearn.src.signal_processing.advanced import compute_energy_over_time_window
from muselearn.src.scraping.mp3_downloader import download_mp3_from_youtube_link
from muselearn.src.converters.type_converter import TypeConverter
from muselearn.src.converters.file_converter import FileConverter
from muselearn.src.loaders.loader import WavLoader
import matplotlib.pyplot as plt
from muselearn.src.signal_processing.statistics import plot_histogram

from pathlib import Path


def main():
    waveform = collect_data()
    print(len(waveform), type(waveform))
    energies = process_data(waveform)
    plot_data(energies)


def collect_data():
    # path_to_mp3 = download_mp3_from_youtube_link('https://www.youtube.com/watch?v=nq0ESlJhvBM')
    # path_to_wav = FileConverter.from_type('mp3_to_wav',
    #                                       Path(path_to_mp3)).convert()
    path_to_wav = '/home/orphefs/Documents/Code/muselearn/muselearn/data/music/Fragz_Disphonia_Blind.wav'
    waveform = WavLoader(path_to_wav).load()
    return waveform


def process_data(waveform):
    energies = compute_energy_over_time_window(waveform=waveform.waveform,
                                               sampling_rate=waveform.duration,
                                               window_length_seconds=1)
    return energies


def plot_data(data):
    fig, axes = plt.subplots(nrows=1, ncols=1)
    plot_histogram(data=[item[0] for item in list(data.values())], bins=60, axes=axes)
    plt.show()


if __name__ == '__main__':
    main()
