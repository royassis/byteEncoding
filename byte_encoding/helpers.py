"""
File containing helper function
"""
import datetime
import array


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


class MeasurePoint():
    """
    TODO: add docstring
    """

    def __init__(self, timestampbytes, measurebytes, timeformat="%Y-%m-%d-%H-%M-%S"):
        self._timestampbytes = timestampbytes
        self._measurebytes = measurebytes
        self._timeformat = timeformat

    @property
    def timestamp(self):
        return bytes_to_datetime(self._timestampbytes, self._timeformat)

    @property
    def measure(self):
        return byte_to_double(self._measurebytes)

    def __str__(self):
        return (f"{self.measure}, {self.timestamp}")


def generic_generator(filepath, dateformat="%Y-%m-%d-%H-%M-%S"):
    double_bytes = 8
    with open(filepath, "rb") as filehandle:

        while True:
            datetime_bytes = filehandle.read(double_bytes)
            measure_bytes = filehandle.read(double_bytes)

            if len(measure_bytes) != 8 or len(datetime_bytes) != 8:
                break

            yield f"{bytes_to_datetime(datetime_bytes, dateformat)}, {byte_to_double(measure_bytes)}"


class PenReader():
    def __init__(self, file_path, dateformat="%Y-%m-%d %H:%M:%S", floatprecision=None):
        self.__path = file_path
        self.__dateformat = dateformat
        self.__file_object = None

    def __enter__(self):
        self.__file_object = open(self.__path, "rb")
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
            return f"{bytes_to_datetime(initial_data[:8], self.__dateformat)}, {byte_to_double(initial_data[8:])}"


