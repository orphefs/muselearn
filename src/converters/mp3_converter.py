import abc
import re
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
    def from_type(type, path_to_input_file):
        if type == "wav_to_mp3":
            return _Wav2Mp3(path_to_input_file)
        elif type == "mp3_to_wav":
            return _Mp32Wav(path_to_input_file)
        else:
            raise TypeError

    @abc.abstractmethod
    def convert(self):
        """Retrieve data from the input source and return an object."""
        return


class _Wav2Mp3(Converter):
    def __init__(self, path_to_input_file):
        super(_Wav2Mp3, self).__init__(path_to_input_file)
        mime = magic.from_file(str(path_to_input_file), mime=True)
        if not re.search('wav', mime):
            raise TypeError("Invalid input file binary format.")
        self._path_to_output_file = Path(self._path_to_input_file.with_suffix('.mp3'))

    def convert(self):
        cmd = "lame --preset insane {infile} {outfile}".format(infile=str(self._path_to_input_file),
                                                               outfile=str(self._path_to_output_file))
        subprocess.call(cmd, shell=True)
        return self._path_to_output_file


class _Mp32Wav(Converter):
    def __init__(self, path_to_input_file):
        super(_Mp32Wav, self).__init__(path_to_input_file)
        mime = magic.from_file(str(path_to_input_file), mime=True)
        if not re.search('mpeg', mime):
            raise TypeError("Invalid input file binary format.")
        self._path_to_output_file = Path(self._path_to_input_file.with_suffix('.wav'))

    def convert(self):
        cmd = "lame --decode {infile} {outfile}".format(infile=str(self._path_to_input_file),
                                                        outfile=str(self._path_to_output_file))
        subprocess.call(cmd, shell=True)
        return self._path_to_output_file


if __name__ == '__main__':
    # path_to_fake_wav = '/home/orphefs/Documents/Code/muselearn/muselearn/data/music/fake.wav'
    # path_real_wav = '/home/orphefs/Documents/Code/muselearn/muselearn/data/music/_candyman.wav'
    # path_to_mp3 = Converter.from_type('wav_to_mp3',
    #                     Path(path_real_wav)).convert()

    path_to_mp3 = '/home/orphefs/Documents/Code/muselearn/muselearn/data/music/candyman.mp3'
    path_to_wav = Converter.from_type('mp3_to_wav',
                                      Path(path_to_mp3)).convert()

    print(path_to_mp3)
