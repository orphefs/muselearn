import pytest
import numpy as np
from muselearn.src.signal_processing.advanced import compute_energy_over_time_window

triangle_waveform = [-1, 1] * 5
dc_signal = [1, 1] * 5
random_waveform = [-2, 0, 0, 0, -1, 1, -1, 1, -1, 1]
special_waveform = [-1, 1, 2, 1, 1, 1, 1]


@pytest.mark.parametrize("waveform, sampling_rate, window_length_seconds, expected_result", [
    pytest.param(triangle_waveform, 1, 2, [{(0, 2): 2.0},
                                           {(2, 4): 2.0},
                                           {(4, 6): 2.0},
                                           {(6, 8): 2.0},
                                           {(8, 10): 2.0}], id='triangle'),
    pytest.param(special_waveform, 1, 4, [{(0, 4): 7.0}], id='special'),
])
def test_compute_energy_over_time_window(waveform, sampling_rate, window_length_seconds, expected_result):
    assert compute_energy_over_time_window(waveform=waveform,
                                           sampling_rate=sampling_rate,
                                           window_length_seconds=window_length_seconds), expected_result
