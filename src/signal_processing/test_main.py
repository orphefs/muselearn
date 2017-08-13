import pytest
import unittest
import numpy as np
from muselearn.src.signal_processing.main import compute_energy, compute_power, duration


@pytest.fixture(scope='class')
def init_dc_signal(request):
    request.cls.waveform = np.ones(10)
    request.cls.sampling_rate = 0.5


@pytest.fixture(scope='class')
def init_ac_signal_triangle(request):
    request.cls.waveform = np.array([-1, 1] * 5)
    request.cls.sampling_rate = 0.5

@pytest.fixture(scope='class')
def init_ac_signal_square(request):
    request.cls.waveform = np.array([-1, 1] * 5)
    request.cls.sampling_rate = 0.5

fixture_collection = ('init_dc_signal', 'init_ac_signal_triangle', 'init_ac_signal_square')


@pytest.mark.usefixtures(fixture_collection)
class TestEnergyComputation(unittest.TestCase):
    def test_compute_energy(self):
        assert compute_energy(waveform=self.waveform, sampling_rate=self.sampling_rate) == 20.0


@pytest.mark.usefixtures(fixture_collection)
class TestPowerComputation(unittest.TestCase):
    def test_compute_power(self):
        assert compute_power(waveform=self.waveform, sampling_rate=self.sampling_rate) == 1.0


@pytest.mark.usefixtures(fixture_collection)
class TestDurationCalculation(unittest.TestCase):
    def test_duration(self):
        assert duration(waveform=self.waveform, sampling_rate=self.sampling_rate) == 20.0


if __name__ == '__main__':
    import os
    import subprocess

    subprocess.call(['pytest', os.path.basename(__file__)])
