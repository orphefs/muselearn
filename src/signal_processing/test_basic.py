import pytest
import numpy as np
from muselearn.src.signal_processing.basic import compute_energy, \
    compute_power, duration, normalize, compute_energy_over_time_window

triangle_waveform = [-1, 1] * 5
dc_signal = [1, 1] * 5
random_waveform = [-2, 0, 0, 0, -1, 1, -1, 1, -1, 1]


@pytest.mark.parametrize("waveform, sampling_rate, expected_result", [
    pytest.param(triangle_waveform, 1, 10.0, id='triangle 1 S/s'),
    pytest.param(dc_signal, 1, 10.0, id='dc 1 S/s'),
    pytest.param(triangle_waveform, 2, 5.0, id='triangle 2 S/s'),
    pytest.param(dc_signal, 2, 5.0, id='dc 2 S/s'),
])
def test_duration(waveform, sampling_rate, expected_result):
    assert duration(waveform=waveform, sampling_rate=sampling_rate) == expected_result


@pytest.mark.parametrize("waveform, sampling_rate, expected_result", [
    pytest.param(triangle_waveform, 1, 10.0, id='triangle 1 S/s'),
    pytest.param(dc_signal, 1, 10.0, id='dc 1 S/s'),
    pytest.param(triangle_waveform, 2, 5.0, id='triangle 2 S/s'),
    pytest.param(dc_signal, 2, 5.0, id='dc 2 S/s'),
])
def test_compute_energy(waveform, sampling_rate, expected_result):
    assert compute_energy(waveform=waveform, sampling_rate=sampling_rate) == expected_result


@pytest.mark.parametrize("waveform, sampling_rate, expected_result", [
    pytest.param(triangle_waveform, 1, 1.0, id='triangle 1 S/s'),
    pytest.param(dc_signal, 1, 1.0, id='dc 1 S/s'),
    pytest.param(triangle_waveform, 2, 1.0, id='triangle 2 S/s'),
    pytest.param(dc_signal, 2, 1.0, id='dc 2 S/s'),
])
def test_compute_power(waveform, sampling_rate, expected_result):
    assert compute_power(waveform=waveform, sampling_rate=sampling_rate) == expected_result


@pytest.mark.parametrize("waveform, method, expected_result", [
    pytest.param(triangle_waveform, 'peak', triangle_waveform, id='triangle'),
    pytest.param(dc_signal, 'peak', dc_signal, id='dc'),
    pytest.param(random_waveform, 'peak', np.array([-1., 0., 0., 0., -0.5, 0.5, -0.5, 0.5, -0.5, 0.5]), id='random'),
])
def test_normalize(waveform, method, expected_result):
    assert np.array_equal(normalize(waveform=waveform, method=method), expected_result)


if __name__ == '__main__':
    import os
    import subprocess

    # subprocess.call(['pytest', os.path.basename(__file__), '--collect-only'])
    subprocess.call(['pytest', os.path.basename(__file__)])
