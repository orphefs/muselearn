from muselearn.src.signal_processing.basic import duration
import numpy as np


class Waveform(object):
    def __init__(self, input_left: np.ndarray,input_right: np.ndarray, sampling_rate: int):
        self._left = input_left
        self._right = input_right
        self._sampling_rate = sampling_rate
        self._number_of_samples = len(input_left)
        self._duration = duration(input_left,
                                  sampling_rate)

    @property
    def duration(self):
        return self._duration

    @property
    def sampling_rate(self):
        return self._sampling_rate

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    def __len__(self):
        return self._number_of_samples
