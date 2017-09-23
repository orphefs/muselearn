class Waveform(object):

    def __init__(self, input_waveform, sampling_rate):
        self._waveform = input_waveform
        self._sampling_rate = sampling_rate
        self._number_of_samples = len(input_waveform)
        self._duration = self.compute_waveform_duration(self._number_of_samples,
                                                   self._sampling_rate)

    @staticmethod
    def compute_waveform_duration(number_of_samples, sampling_rate):
        return number_of_samples/sampling_rate

    def __getitem__(self, item):
        return self._waveform[item]

