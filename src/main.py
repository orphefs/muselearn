from muselearn.src.signal_processing.advanced import *
from muselearn.src.scraping.mp3_downloader import download_mp3_from_youtube_link
from muselearn.src.converters.type_converter import TypeConverter
from muselearn.src.converters.file_converter import FileConverter
from muselearn.src.loaders.loader import WavLoader
import matplotlib.pyplot as plt
from muselearn.src.signal_processing.statistics import plot_kdeplot, plot_histogram
import numpy as np
from pathlib import Path


def main():
    waveform = collect_data()
    print(len(waveform), type(waveform))
    quantities = process_data(waveform)
    plot_data(quantities)


def collect_data():
    # path_to_mp3 = download_mp3_from_youtube_link('https://www.youtube.com/watch?v=nq0ESlJhvBM')
    # path_to_wav = FileConverter.from_type('mp3_to_wav',
    #                                       Path(path_to_mp3)).convert()
    # path_to_wav = '/home/orphefs/Documents/Code/muselearn/muselearn/data/music/Fragz_Disphonia_Blind.wav'
    path_to_wav = '/home/orphefs/Documents/Code/muselearn/muselearn/data/music/mozart-symphony40-1.wav'
    # path_to_wav = '/home/orphefs/Documents/Code/muselearn/muselearn/data/music/Toccata-and-Fugue-Dm.wav'

    waveform = WavLoader(path_to_wav).load()
    return waveform


def process_data(waveform):
    quantities = compute_quantity_over_time_window(kernel_function=compute_power,
                                                   waveform=waveform.waveform,
                                                   sampling_rate=waveform.duration,
                                                   window_length_seconds=5)
    return quantities


def plot_data(data):
    fig, axes = plt.subplots(nrows=1, ncols=1)
    plot_histogram(data=abs(np.array([item[1] for item in list(data.values())])), bins=30, axes=axes)
    plt.show()


if __name__ == '__main__':
    main()
