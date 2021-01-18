import zipfile
from pathlib import Path
from utils import PenGeneralIterator, filter_namelist, get_sensor_number, get_sensor_date_from_data
import pandas as pd

p = Path(r"/data/wserver101-Week-36-Year-2017.zip")
z = zipfile.ZipFile(p)
filtered_namelist = filter_namelist(z.namelist())

for archname in filtered_namelist[:50]:
    print(archname)
    filehandle = z.open(archname)

    sensor_number = get_sensor_number(filehandle.name)
    file_date = get_sensor_date_from_data(filehandle).strftime("%Y%m%d")

    data = []
    for ts, val in PenGeneralIterator(filehandle):
        data.append([ts,val, sensor_number])

    # pd.DataFrame(data).to_csv(f"{file_date}.csv" ,mode="a",index= False,header= False)
