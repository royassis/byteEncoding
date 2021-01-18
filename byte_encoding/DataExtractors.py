from abc import ABC
import re
from collections import namedtuple
from byte_encoding.FileOrEquivalentIterators import FileIterator
import datetime

class BaseMetaDataExtractor(ABC):
    meta_data = None

    def __init__(self, stuff):
        pass

    def get_metadata(self, stuff):
        pass

    def get_sensor_number(self):
        pass

    def get_sensor_date(self):
        pass

    def get_file_metadata(self):
        pass

class FileMetaDataExtractor(BaseMetaDataExtractor):
    meta_data = namedtuple("metaDate", "sensor_number sensor_date")

    def __init__(self, file_path):
        self.file_path = file_path
        self.meta_data = self.get_file_metadata()

    def get_sensor_number(self):
        file_format = r".*Pen(?P<sensor_number>\d+).*"
        match = re.match(file_format, str(self.file_path))
        if match:
            return match.group("sensor_number")

    def get_sensor_date(self):
        match = re.match(".*(?P<date>\d{4} \d\d? \d\d?).*",self.file_path)
        if match:
            date = match.group("date")
            date = datetime.datetime.strptime(date, "%Y %m %d")
        return date

    def get_file_metadata(self):
        md = self.meta_data(self.get_sensor_number(), self.get_sensor_date())
        return md

class ZipMetaDataExtractor():
    pass
