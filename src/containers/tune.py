

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


class Snippet(object):
    def __init__(self):
        raise NotImplementedError

    def __repr__(self):
        return 'vlah=%r' % (self._vlah
                                                )

    def __str__(self):
        return "{}".format(self._vlah)

    @classmethod
    def from_data_frame_row(cls, df):
        raise NotImplementedError


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
        """Factory method"""
        file = load_audio_file()
        audio = Audio(path_to_file=path_to_audio_file, metadata=None)
        return audio

    def __iter__(self):
        for snippet in self._snippets:
            yield snippet

    def __getitem__(self, index):
        return self._snippets[index]

    def remove(self, segment):
        if snippet in self._snippets:
            self._snippets.remove(snippet)


if __name__ == '__main__':
    pass
