from muselearn.src.signal_processing.basic import duration
import numpy as np


class Waveform(object):
    def __init__(self, input_waveform: np.ndarray, sampling_rate: int):
        self._waveform = input_waveform
        self._sampling_rate = sampling_rate
        self._number_of_samples = len(input_waveform)
        self._duration = duration(input_waveform,
                                  sampling_rate)
        self._waveform = input_waveform

    def __getitem__(self, item):
        return self._waveform[item]

    @property
    def duration(self):
        return self._duration

    @property
    def sampling_rate(self):
        return self._sampling_rate

    @property
    def waveform(self):
        return self._waveform

    def __len__(self):
        return self._number_of_samples
