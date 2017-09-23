import numpy as np
from muselearn.src.containers.waveform import Waveform


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


def compute_energy_over_time_window(waveform: np.ndarray, sampling_rate: int, window_length: float) -> list[np.float64]:
    wav = Waveform(waveform, sampling_rate)
    number_of_iterations = wav.duration / window_length
    energies = []
    for i in range(0, number_of_iterations):
        from_sample = int(i - 1 * window_length)
        to_sample = int(i * window_length)
        energy_over_time_window = {
            [from_sample, to_sample]: wav[from_sample:to_sample]
        }

        energies.append(compute_energy(energy_over_time_window.value(), sampling_rate))
    return energies


if __name__ == '__main__':
    main()
