import json
import numpy as np
from _collections_abc import abstractmethod


class _Metadata(object):
    pass


class SongMetadata(_Metadata):
    def __init__(self, artist, title, album, year):
        self.artist = artist
        self.title = title
        self.album = album
        self.year = year


class FileMetadata(_Metadata):
    def __init__(self, file_name, file_size):
        self.file_name = file_name
        self.file_size = file_size


class AudioMetadata(_Metadata):
    def __init__(self, dynamic_range, bpm):
        self.dynamic_range = dynamic_range
        self.bpm = bpm


class Segment(object):
    def __init__(self, floor_entry_time,
                 floor_exit_time,
                 delta_floor,
                 entry_structure_id,
                 exit_structure_id,
                 delta_pressure_of_transition,
                 checks=None):
        self._floor_entry_time = floor_entry_time
        self._floor_exit_time = floor_exit_time
        self._delta_floor = delta_floor
        self._entry_structure_id = entry_structure_id
        self._exit_structure_id = exit_structure_id
        self._delta_pressure_of_transition = delta_pressure_of_transition

        self._duration = floor_exit_time - floor_entry_time
        self._checks = checks

    def __repr__(self):
        return 'Segment(floor_entry_time=%r, ' \
               'floor_exit_time=%r, ' \
               'delta_floor=%r, ' \
               'entry_structure_id=%r,  ' \
               'exit_structure_id=%r, ' \
               'delta_pressure_of_transition=%r) \n' % (self._floor_entry_time,
                                                        self._floor_exit_time,
                                                        self._delta_floor,
                                                        self._entry_structure_id,
                                                        self._exit_structure_id,
                                                        self._delta_pressure_of_transition)

    def __str__(self):
        return "{},{},{},{},{},{}".format(self._floor_entry_time,
                                          self._floor_exit_time,
                                          self._delta_floor,
                                          self._entry_structure_id,
                                          self._exit_structure_id,
                                          self._delta_pressure_of_transition)

    @classmethod
    def from_data_frame_row(cls, df):
        raise NotImplementedError

    @property
    def checks(self):
        return self._checks

    @checks.setter
    def checks(self, checklist):
        self._checks = checklist

    @property
    def duration(self):
        return self._duration

    @property
    def delta_pressure_of_transition(self):
        return self._delta_pressure_of_transition

    @delta_pressure_of_transition.setter
    def delta_pressure_of_transition(self, value):
        self._delta_pressure_of_transition = value

    @property
    def delta_floor(self):
        return self._delta_floor

    @delta_floor.setter
    def delta_floor(self, value):
        self._delta_floor = value


class Audio(object):
    def __init__(self, path_to_file, metadata):
        self._path_to_file = path_to_file
        self._metadata = metadata
        self._waveform = []

    def __repr__(self):
        return 'Song({})'.format([segment for segment in self._segments])

    def load_waveform(self):
        self._waveform = pd.DataFrame(self._path_to_file)

    @property
    def metadata(self):
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        self._metadata = metadata

    @classmethod
    def from_file(cls, path_to_audio_file):
        """Factory method to create trajectory from floorchange and building"""
        file = load_audio_file()
        audio = Audio(path_to_file=path_to_audio_file, metadata=None)
        return audio

    def write_to_file(self, path_to_floorchange):

        with open(path_to_floorchange, 'w') as outfile:
            outfile.write('floor_entry_time, '
                          'floor_exit_time, '
                          'delta_floor, '
                          'entry_structure_id, '
                          'exit_structure_id, '
                          'delta_pressure_of_transition \n')
            for segment in self._segments:
                outfile.write(str(segment))
                outfile.write('\n')

    @property
    def segments(self):
        return self._segments

    def __iter__(self):
        for segment in self._segments:
            yield segment

    def __getitem__(self, index):
        return self._segments[index]

    def remove(self, segment):
        if segment in self._segments:
            self._segments.remove(segment)


if __name__ == '__main__':
    segment1 = Segment(0, 1, 1, 100, 101, -0.7, [])
    segment2 = Segment(1, 2, -1, 101, 100, 0.8, [])

    trajectory = Song([segment1, segment2])
    for segment in trajectory:
        print(segment)

    print(trajectory[0])
