from pathlib import Path
from helpers import  PenParser, PenZipReader


path_to_zip = Path(r"C:\Users\Roy\PycharmProjects\byte_encoding\byte_encoding\data\wserver101-Week-36-Year-2017.zip")
with PenZipReader(path_to_zip) as z:
    for uncompressed_temp_file in z:
        p = PenParser(uncompressed_temp_file)
        p.to_csv("temps.csv")

