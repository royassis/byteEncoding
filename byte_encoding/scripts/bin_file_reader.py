from pathlib import Path
from ZipIterators import ZipFileHandleIterator
from FileOrEquivalentIterators import BytesArrayIterator
import logging

logging.basicConfig(level=logging.INFO)

path_to_zip = Path(r"C:\Users\Roy\Downloads\wserver102-08-2020.zip")
with ZipFileHandleIterator(path_to_zip) as z:
    for archandle in z:
        data = archandle.read()
        for segment in BytesArrayIterator(data):
            print(segment)
