import abc
import wave
from wave import Wave_read
from scipy.io.wavfile import read
from pathlib import Path


class _Loader(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, path_to_file: Path):
        self._path_to_file = path_to_file
        self._content = self.load()

    @abc.abstractmethod
    def load(self):
        """Retrieve data from the input source and return an object."""
        return

    @abc.abstractmethod
    def load(self):
        """Retrieve data from the input source and return an object."""
        return


class WavLoader(_Loader):
    def __init__(self, path_to_file):
        super(WavLoader, self).__init__(path_to_file)

    def load(self) -> Wave_read:
        with open(str(self._path_to_file), 'rb') as infile:
            self._content = read(infile)
        return self._content

if __name__ == '__main__':
    path_to_file = Path('/home/orphefs/Documents/Code/muselearn/muselearn/data/music/_candyman.wav')
    wave = WavLoader(path_to_file).load()
    print(wave)
