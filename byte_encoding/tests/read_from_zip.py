import zipfile
from pathlib import Path
from myclasses import PenReader
from utils import zfile_read_sain
import os

p = Path(r"C:\Users\Roy\PycharmProjects\byte_encoding\byte_encoding\tests\fixtures\wserver102-Week-53-Year-2020.zip")
z = zipfile.ZipFile(p)
nl = z.namelist()
onefile = nl[-12]

filehandle = z.open(onefile)

for ts, val in zfile_read_sain(filehandle):
    print(ts, val)
