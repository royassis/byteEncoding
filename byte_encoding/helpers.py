"""
File containing helper function
"""
import datetime
import array
import re


def byte_to_double(new_bytearr: bytearray) -> float:
    """
    Wrapper for array.array()

    :param new_bytearr: 8 byte chunck representing Double
    :return: float
    """
    return array.array('d', new_bytearr)[0]


def bytes_to_datetime(new_bytearr: bytearray, timeformat: str = "%Y-%m-%d-%H-%M-%S") -> datetime:
    """
    Converts eight bytes to datetime

    :param new_bytearr: 8 byte chunck representing Double
    :return: datetime object
    """
    doubles_sequence = byte_to_double(new_bytearr)
    seconds = (doubles_sequence - 25569) * 86400.0
    dt_obj = datetime.datetime.utcfromtimestamp(seconds)

    return dt_obj.strftime(timeformat)


class PenReader():
    def __init__(self, file_path, dateformat="%Y-%m-%d %H:%M:%S", floatprecision=2, sep="\t",
                 include_sensor_name=False):
        self._path = file_path
        self.__dateformat = dateformat
        self.__file_object = None
        self.__sep = sep
        self.__floatprecision = floatprecision
        self.__include_sensor_name = include_sensor_name
        self._pen_number = self.get_pennumber()
        self._pen_date = self.get_pendate()

    def read_all(self):
        outtext = ""
        for line in self:
            outtext = outtext + line + "\n"

        return outtext

    def to_csv(self, outpath=None):
        if not outpath:
            outpath = f"{self._pen_date}.csv"

        with open(outpath, "w") as fp:
            fp.write(self.read_all())

    def get_pennumber(self):
        format = r".*Pen(?P<sensornumber>\d+).*"
        match = re.match(format, str(self._path))

        return int(match.group("sensornumber"))

    def get_pendate(self):
        with open(self._path, "rb") as fp:
            bts = fp.read(8)

        return bytes_to_datetime(bts)[:10]

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
            timestamp = bytes_to_datetime(initial_data[:8], self.__dateformat)
            s = self.__sep
            value = byte_to_double(initial_data[8:])
            retstr = f"{timestamp}{s}{value}"

            if self.__include_sensor_name:
                retstr = f"{retstr}{s}{self._pen_number}"
            return retstr


class PenZipReader():
    def __init__(self, zippath):
        pass