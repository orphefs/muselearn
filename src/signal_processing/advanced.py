import numpy as np
from muselearn.src.containers.waveform import Waveform
from muselearn.src.signal_processing.basic import *
from typing import Callable
from typing import get_type_hints

Vector = List[np.float64]


def compute_quantity_over_time_window(kernel_function: Callable, waveform: np.ndarray,
                                      sampling_rate: int,
                                      window_length_seconds: float) -> Vector:
    waveform = Waveform(waveform, sampling_rate)
    number_of_iterations = int(waveform.duration / window_length_seconds)
    quantities = {}
    for i in range(1, number_of_iterations + 1):
        from_sample = int((i - 1) * window_length_seconds)
        to_sample = int(i * window_length_seconds)
        quantities.update({
            (from_sample, to_sample): kernel_function(
                waveform[from_sample:to_sample], sampling_rate)
        })
    return quantities


if __name__ == '__main__':
    energies = compute_quantity_over_time_window(compute_energy, np.array([-1, 1] * 5), 1, 2)
    for energy in energies:
        print(energy)
