"""
File containing helper function
"""
import datetime
import array
import re
from pathlib import Path


def byte_to_double(new_bytearr: bytearray) -> float:
    """
    Wrapper for array.array()

    :param new_bytearr: 8 byte chunck representing Double
    :return: float
    """
    return array.array('d', new_bytearr)[0]


def bytes_to_datetime(new_bytearr: bytearray):
    """
    Converts eight bytes to datetime

    :param new_bytearr: 8 byte chunck representing Double
    :return: datetime object
    """
    doubles_sequence = byte_to_double(new_bytearr)
    seconds = (doubles_sequence - 25569) * 86400.0
    dt_obj = datetime.datetime.utcfromtimestamp(seconds)

    return dt_obj


class PenReader():
    def __init__(self, file_path):
        self._path = file_path
        self.__file_object = None
        self.sensor_number = self.get_pennumber()
        self.measure_date = self.get_pendate()

    def read_all(self, **kwargs):
        outtext = ""
        for line in self.custom_iter(**kwargs):
            outtext = outtext + line + "\n"

        return outtext

    def to_csv(self, outpath=None, adddate=True, mode="a", sep="," ):

        if not outpath:
            raise ValueError("please enter a path")

        outpath = Path(outpath)

        if not outpath.is_dir() and adddate:
            raise ValueError("outpath is not a dir while adddate is True")

        if  outpath.is_dir() and adddate:
            outpath = outpath / self.measure_date / ".csv"

        with open(outpath, mode) as fp:
            fp.write(self.read_all(sep = sep))

    def get_pennumber(self):
        format = r".*Pen(?P<sensornumber>\d+).*"
        match = re.match(format, str(self._path))

        return int(match.group("sensornumber"))

    def get_pendate(self):
        with open(self._path, "rb") as fp:
            bts = fp.read(8)

        return bytes_to_datetime(bts).date

    def custom_iter(self, timeformat="%Y-%m-%d %H:%M:%S", sep="\t", perc=2, addsensor=True):

        for ts, value in self:
            output = []
            timestamp = ts.strftime(timeformat)
            value = "{1:,.{0}f}".format(perc, value)

            output.append(timestamp)
            output.append(value)
            if addsensor:
                output.append(self.sensor_number)

            stroutput = map(str, output)

            yield sep.join(stroutput)

    def __enter__(self):
        self.__file_object = open(self._path, "rb")
        return self

    def __exit__(self, type, val, tb):
        self.__file_object.close()

    def __iter__(self):
        return self

    def __next__(self):
        initial_data = self.__file_object.read(16)

        if self.__file_object is None or initial_data == b'':
            raise StopIteration
        else:
            timestamp = bytes_to_datetime(initial_data[:8])
            value = byte_to_double(initial_data[8:])

            return timestamp, value


class PenZipReader():
    def __init__(self, zippath):
        pass
