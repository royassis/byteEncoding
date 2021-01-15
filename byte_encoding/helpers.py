"""
File containing helper function
"""
import datetime
import array
import re
from pathlib import Path
import pandas as pd
from collections import namedtuple


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

    def read_all(self):
        outtext = ""
        for ts, value in self:
            line = f"{ts}\t{value}"
            outtext = outtext + line + "\n"

        return outtext

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


class PenParser():
    meta_data = namedtuple("metaDate", "sensor_number sensor_date")

    def __init__(self, file_path):
        self.file_path = file_path
        self.meta_data = self.get_file_metadata()
        self.df = None

    def get_sensor_number(self):
        file_format = r".*Pen(?P<sensor_number>\d+).*"
        match = re.match(file_format, str(self.file_path))
        return match.group("sensor_number")

    def get_sensor_date(self):
        with PenReader(self.file_path) as reader:
            ts, _ = next(reader)
        return ts

    def get_file_metadata(self):
        md = self.meta_data(self.get_sensor_number(), self.get_sensor_date())
        return md

    def load_to_df(self):
        data = []
        with PenReader(self.file_path)as reader:
            for ts, value in reader:
                data.append([ts, value])
        df = pd.DataFrame(data, columns=["ts", "value"])
        df["sensor_number"] = self.meta_data.sensor_number
        self.df = df

    def to_csv(self, path_or_buf=None, usedate=False, *args, **kwargs):
        path_or_buff = Path(path_or_buf)
        if usedate:
            if not path_or_buff.is_dir():
                raise Exception("Can't use a filepath in path_or_buff and usedate=True")
            else:
                format = "%Y%m%d"
                strdate = self.meta_data.sensor_date.strftime(format)
                path_or_buff = path_or_buff.joinpath(strdate).with_suffix(".csv")

        self.df.to_csv(path_or_buf=path_or_buff, *args, **kwargs)


class PenZipReader():
    def __init__(self, zippath):
        pass
