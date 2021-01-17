"""
File containing helper function
"""
import re
from pathlib import Path
import pandas as pd
from collections import namedtuple
import zipfile
import os
from utils import process_sgement
import io
from config import SEGMENT_SIZE

class PenReader():

    def __init__(self, file_path):
        self._path = file_path
        self.__file_object = None

    def read_all(self):
        with  open(self._path, "rb") as fp:
            raw_data = fp.read()

        self.__file_object = io.BytesIO(raw_data)

        data = [segment for segment in self]

        return data

    def __enter__(self):
        self.__file_object = open(self._path, "rb")
        return self

    def __exit__(self, type, val, tb):
        self.__file_object.close()

    def __iter__(self):
        return self

    def __next__(self):
        segment_bytes = self.__file_object.read(SEGMENT_SIZE)

        if self.__file_object is None or segment_bytes == b'':
            raise StopIteration
        else:
            timestamp, value = process_sgement(segment_bytes)

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

        return self

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
    def __init__(self, zip_path):
        self.zip_path = Path(zip_path)
        self.zip_handle = None
        self.file_list = None
        self.list_len = None
        self.file_location = 0
        self.extracted = None

    def clean_filelist(self, filelist):
        paths = [path for path in filelist if re.match(".*Pen.*", path)]
        return paths

    def __enter__(self):
        self.zip_handle = zipfile.ZipFile(self.zip_path)
        self.file_list = self.clean_filelist(self.zip_handle.namelist())
        self.list_len = len(self.file_list)
        return self

    def __exit__(self, type, val, tb):
        self.zip_handle.close()

    def __iter__(self):
        return self

    def __next__(self):
        try:
            os.remove(self.extracted)
        except:
            pass
        if self.file_location == self.list_len:
            raise StopIteration
        else:
            file_name = self.file_list[self.file_location]
            self.file_location = self.file_location + 1
            self.extracted = self.zip_handle.extract(file_name, "temp")
            return self.extracted
