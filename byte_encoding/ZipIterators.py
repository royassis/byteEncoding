from pathlib import Path
import re
import zipfile
import os
from abc import ABC

class ZipExtractorUtils:
    @staticmethod
    def clean_filelist(filelist):
        paths = [path for path in filelist if re.match(".*Pen.*", path)]
        return paths


class BaseZipIterator(ABC):
    def __init__(self, zip_path):
        self.zip_path = Path(zip_path)
        self.zip_handle = None
        self.file_list = None
        self.list_len = None
        self.file_location = 0

    def __enter__(self):
        self.zip_handle = zipfile.ZipFile(self.zip_path)
        self.file_list = ZipExtractorUtils.clean_filelist(self.zip_handle.namelist())
        self.list_len = len(self.file_list)
        return self

    def __exit__(self, type, val, tb):
        self.zip_handle.close()

    def __iter__(self):
        return self

    def __next__(self):
        pass


class ZipFileExtractorIterator(BaseZipIterator):
    """Each iteration cycle involves extracting archfile to a tempfile and returning the temphadnle
    when cycle if done - delete the tempfile"""
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

class ZipFileHandleIterator(BaseZipIterator):
    """Each iteration cycle involves extracting archfile to a tempfile and returning the temphadnle
    when cycle if done - delete the tempfile"""
    def __next__(self):
        try:
            self.archname_handle.close()
        except:
            pass

        if self.file_location == self.list_len:
            raise StopIteration
        else:
            file_name = self.file_list[self.file_location]
            self.file_location = self.file_location + 1
            self.archname_handle = self.zip_handle.open(file_name)
            return self.archname_handle