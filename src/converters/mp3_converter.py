import abc
from pathlib import Path
import magic
import subprocess


class Converter(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, path_to_input_file: Path):
        self._path_to_input_file = path_to_input_file
        self._path_to_output_file = Path()
        self.convert()

    # Create based on class name:
    @staticmethod
    def factory(type, path_to_input_file):
        if type == "wav_to_mp3":
            return _Wav2Mp3(path_to_input_file)
        else:
            raise TypeError

    @abc.abstractmethod
    def convert(self):
        """Retrieve data from the input source and return an object."""
        return


class _Wav2Mp3(Converter):

    def __init__(self, path_to_input_file):
        super(_Wav2Mp3, self).__init__(path_to_input_file)
        print(magic.from_file(str(path_to_input_file)))
        self._path_to_output_file = Path(self._path_to_input_file.stem + '.mp3')

    def convert(self):
        cmd = "lame --preset insane {infile} {outfile}".format(infile=str(self._path_to_input_file),
                                               outfile=str(self._path_to_output_file))
        subprocess.call(cmd, shell=True)


if __name__ == '__main__':
    Converter.factory('wav_to_mp3', Path('/home/orphefs/Documents/Code/muselearn/muselearn/data/music/candyman.wav')).convert()
