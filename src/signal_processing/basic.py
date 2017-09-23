import numpy as np
from typing import List
Vector = List[np.float64]

def main():
    print(compute_energy(np.ones(10), 1))
    print(type(normalize(np.ones(10), 'peak')))


def compute_energy(waveform: np.ndarray, sampling_rate: int) -> np.float64:
    return np.float64(np.sum(amplitude ** 2 for amplitude in waveform) * (1 / float(sampling_rate)))


def compute_power(waveform: np.ndarray, sampling_rate: int) -> np.float64:
    return compute_energy(waveform, sampling_rate) / duration(waveform, sampling_rate)


def duration(waveform: np.ndarray, sampling_rate: int) -> np.float64:
    return np.float64(np.float64(len(waveform)) * (1 / float(sampling_rate)))


def normalize(waveform: np.ndarray, method: str) -> np.ndarray:
    if method == 'peak':
        return waveform / np.max(np.abs(waveform))
    elif method == 'rms':
        raise NotImplementedError





if __name__ == '__main__':
    main()
