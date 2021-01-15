from pathlib import Path
from helpers import PenReader
import zipfile
import tempfile
import pandas as pd

# path_to_zip = Path(r"C:\Users\Roy\PycharmProjects\byte_encoding\byte_encoding\data\wserver101-Week-36-Year-2017.zip")
#
# tempdir = Path(tempfile.mkdtemp())
#
# with zipfile.ZipFile(path_to_zip) as ziphandle:
#     ziphandle.extractall(tempdir)
#
# for file in tempdir.rglob("*Pen*"):
#     print(file)
#     with PenReader(file) as penfile:
#         for line in penfile:
#             print(line)
#     print("\n\n")


path_to_pen = Path(r"C:\Users\Roy\PycharmProjects\byte_encoding\byte_encoding\data\Pen2_20170909_raw")

with PenReader(path_to_pen) as penfile:
    print(penfile.read_all())
