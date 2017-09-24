import abc
import wave
from wave import Wave_read
from scipy.io.wavfile import read
from pathlib import Path
from muselearn.src.containers.waveform import Waveform


class _Loader(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, path_to_file: Path):
        self._path_to_file = path_to_file
        self._content = self.load()

    @abc.abstractmethod
    def load(self):
        """Retrieve data from the input source and return an object."""
        return


class WavLoader(_Loader):
    def __init__(self, path_to_file):
        super(WavLoader, self).__init__(path_to_file)

    def load(self) -> Waveform:
        with open(str(self._path_to_file), 'rb') as infile:
            return Waveform(input_waveform=read(infile)[1],
                            sampling_rate=read(infile)[0])


if __name__ == '__main__':
    path_to_file = Path('/home/orphefs/Documents/Code/muselearn/muselearn/data/music/_candyman.wav')
    wave = WavLoader(path_to_file).load()
    print(wave)
