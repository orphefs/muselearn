import abc
import wave
from wave import Wave_read
import re
from pathlib import Path
import magic
import subprocess


class TypeConverter(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, input_object):
        self._input_object = input_object
        self._output_object = output_object
        self.convert()

    # Create based on class name:
    @staticmethod
    def from_type(conversion_type, path_to_input_file):
        if conversion_type == "wav_to_numpy":
            return _Wav2Numpy(path_to_input_file)
        else:
            raise TypeError

    @abc.abstractmethod
    def convert(self):
        """Retrieve data from the input source and return an object."""
        return


class _Wav2Numpy(TypeConverter):
    def __init__(self, input_object):
        super(_Wav2Numpy, self).__init__(input_object)
        if not isinstance(self._input_object, Wave_read):
            raise TypeError("Invalid input type.")

    def convert(self):
        '''Convert a Wave_read object into numpy array'''
        raise NotImplementedError
        return self._output_object

