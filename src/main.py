from muselearn.src.signal_processing.advanced import compute_energy_over_time_window
from muselearn.src.scraping.mp3_downloader import download_mp3_from_youtube_link
from muselearn.src.converters.type_converter import TypeConverter
from muselearn.src.converters.file_converter import FileConverter
from pathlib import Path


def main():
    waveform = collect_data()
    print(len(waveform), type(waveform))


def collect_data():
    path_to_mp3 = download_mp3_from_youtube_link('https://www.youtube.com/watch?v=IS6n2Hx9Ykk')
    path_to_wav = FileConverter.from_type('mp3_to_wav',
                                          Path(path_to_mp3)).convert()
    waveform = TypeConverter.from_type('wav_to_numpy', path_to_wav)
    return waveform


def process_data(waveform):
    compute_energy_over_time_window(waveform)
    pass


def plot_data():
    pass


if '__name__' == '__main__':
    main()
