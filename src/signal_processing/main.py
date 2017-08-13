import numpy as np


def main():
    print(compute_energy(np.ones(10), 1))


def compute_energy(waveform: np.array[np.int64], sampling_rate: int) -> np.float64:
    return np.float64(np.sum(amplitude ** 2 for amplitude in waveform) * (1 / float(sampling_rate)))


def compute_power(waveform: np.array[np.int64], sampling_rate: int) -> np.float64:
    return compute_energy(waveform, sampling_rate) / duration(waveform, sampling_rate)


def duration(waveform: np.array[np.int64], sampling_rate: int)-> np.float64:
    return np.float64(np.float64(len(waveform)) * (1 / float(sampling_rate)))


def normalize(waveform: np.array[np.int64], method: str) -> np.array[np.int64]:
    if method == 'peak':
        return waveform / np.max(waveform)
    elif method == 'rms':
        raise NotImplementedError



if __name__ == '__main__':
    main()
