import pytest
import unittest
import numpy as np
from muselearn.src.signal_processing.main import compute_energy


@pytest.fixture(scope='class')
def init_dc_signal(request):
    request.cls.waveform = np.ones(10)
    request.cls.sampling_rate = 1


@pytest.mark.usefixtures('init_dc_signal')
class TestEnergyComputation(unittest.TestCase):
    def test_compute_energy(self):
        assert compute_energy(waveform=self.waveform, sampling_rate=self.sampling_rate) == 10.0


if __name__ == '__main__':
    import os
    import subprocess

    subprocess.call(['pytest',  os.path.basename(__file__)])
