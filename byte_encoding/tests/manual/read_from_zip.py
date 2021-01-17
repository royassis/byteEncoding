import zipfile
from pathlib import Path
from myclasses import PenFileReader
from utils import zfile_read_sain, filter_namelist, get_metadata_from_archname
import os
import time
import pandas as pd

p = Path(r"/tests/fixtures/wserver102-Week-53-Year-2020.zip")
z = zipfile.ZipFile(p)
filtered_namelist = filter_namelist(z.namelist())

for archname in filtered_namelist:
    print(archname)
    filehandle = z.open(archname)
    data = []
    for ts, val in zfile_read_sain(filehandle):
       data.append(ts,val, archname)

    md_obj = get_metadata_from_archname(archname)
    file_date = md_obj.date

    pd.DataFrame(data).to_csv(f"{file_date}.csv" ,mode="a",index= False,header= False)
