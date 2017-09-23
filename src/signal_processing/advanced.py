import numpy as np
from muselearn.src.containers.waveform import Waveform
from muselearn.src.signal_processing.basic import compute_energy
from typing import List

Vector = List[np.float64]


def compute_energy_over_time_window(waveform: np.ndarray,
                                    sampling_rate: int,
                                    window_length_seconds: float) -> Vector:
    wav = Waveform(waveform, sampling_rate)
    number_of_iterations = int(wav.duration / window_length_seconds)
    energies = []
    for i in range(1, number_of_iterations + 1):
        from_sample = int((i - 1) * window_length_seconds)
        to_sample = int(i * window_length_seconds)
        energies.append({
            (from_sample, to_sample): compute_energy(
                wav[from_sample:to_sample], sampling_rate)
        })
    return energies


if __name__ == '__main__':
    energies = compute_energy_over_time_window(np.array([-1, 1] * 5), 1, 2)
    for energy in energies:
        print(energy)
