from abc import ABC
from .config import SEGMENT_SIZE
import io
from .utils import decode_sgement


class BaseFileIterator(ABC):
    def __init__(self):
        self.file_object = None

    def __enter__(self):
        self.file_object = open(self._path, "rb")
        return self

    def __exit__(self, type, val, tb):
        self.file_object.close()

    def __iter__(self):
        return self

    def __next__(self):
        segment_bytes = self.file_object.read(SEGMENT_SIZE)

        if self.file_object is None or segment_bytes == b'':
            raise StopIteration
        else:
            timestamp, value = decode_sgement(segment_bytes)

            return timestamp, value


class BytesArrayIterator():
    def __init__(self, data):
        self.data = data
        self.file_object = io.BytesIO(data)

    def __iter__(self):
        return self

    def __next__(self):
        segment_bytes = self.file_object.read(SEGMENT_SIZE)

        if self.file_object is None or segment_bytes == b'':
            raise StopIteration
        else:
            timestamp, value = decode_sgement(segment_bytes)

            return timestamp, value



class FileIterator(BaseFileIterator):

    def __init__(self, file_path):
        self._path = file_path
        self.file_object = None

    def __enter__(self):
        self.file_object = open(self._path, "rb")
        return self

    def __iter__(self):
        return self
