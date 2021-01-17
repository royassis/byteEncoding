import zipfile
from pathlib import Path
from utils import PenGeneralIterator, filter_namelist
import os
import time
import pandas as pd

p = Path(r"C:\Users\Roy\PycharmProjects\byte_encoding\byte_encoding\tests\fixtures\wserver102-Week-53-Year-2020.zip")
z = zipfile.ZipFile(p)
filtered_namelist = filter_namelist(z.namelist())

for archname in filtered_namelist:
    print(archname)
    filehandle = z.open(archname)
    data = []
    for ts, val in PenGeneralIterator(filehandle):
       data.append(ts,val, archname)

    file_date = md_obj.date

    pd.DataFrame(data).to_csv(f"{file_date}.csv" ,mode="a",index= False,header= False)
