import zipfile
from pathlib import Path
from utils import zfile_read_sain, filter_namelist, get_sensor_number, get_sensor_date
import pandas as pd

p = Path(r"/tests/fixtures/wserver102-Week-53-Year-2020.zip")
z = zipfile.ZipFile(p)
filtered_namelist = filter_namelist(z.namelist())

for archname in filtered_namelist:
    print(archname)
    filehandle = z.open(archname)

    sensor_number = get_sensor_number(filehandle.name)
    file_date = get_sensor_date(filehandle).strftime("%Y%m%d")

    data = []
    for ts, val in zfile_read_sain(filehandle):
       data.append([ts,val, sensor_number])

    pd.DataFrame(data).to_csv(f"{file_date}.csv" ,mode="a",index= False,header= False)
