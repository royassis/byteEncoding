"""
File containing helper function
"""

import zipfile
from pathlib import Path
import datetime
import array


def get_file_handle_from_zip(zippathstr):
    """
    :param zippathstr: path to zip archive containing bin file
    :return: handle to archived binnary file
    """

    zippath = Path(zippathstr)

    # Handle to zip archive
    archive = zipfile.ZipFile(zippath.resolve(), 'r')

    # First file in zip
    filename = archive.namelist()[0]

    # Get a reading handle for file
    items_file = archive.open(filename, 'r')

    return items_file


# items_file.read(8)

def byte_to_double(new_bytearr: bytearray) -> float:
    """
    Wrapper for array.array()

    :param new_bytearr: 8 byte chunck representing Double
    :return: float
    """
    return array.array('d', new_bytearr)[0]


def bytes_to_datetime(new_bytearr: bytearray, timeformat: str) -> datetime:
    """
    Converts eight bytes to datetime

    :param new_bytearr: 8 byte chunck representing Double
    :return: datetime object
    """
    doubles_sequence = byte_to_double(new_bytearr)
    seconds = (doubles_sequence - 25569) * 86400.0
    dt_obj = datetime.datetime.utcfromtimestamp(seconds)

    return dt_obj.strftime(timeformat)


class MeasurePoint():
    """
    TODO: add docstring
    """

    def __init__(self, timestampbytes, measurebytes):
        self._timestampbytes = timestampbytes
        self._measurebytes = measurebytes

    @property
    def timestamp(self):
        return bytes_to_datetime(self._timestampbytes, timeformat = "%Y-%m-%d-%H-%M-%S")

    @property
    def measure(self):
        return byte_to_double(self._measurebytes)

    def __str__(self):
        return (f"{self.measure}, {self.timestamp}")
