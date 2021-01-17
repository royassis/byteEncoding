from pathlib import Path
from MiscCode import Pen
from ZipIterators import ZipFileExtractorIterator
import logging

logging.basicConfig(level=logging.INFO)

path_to_zip = Path(r"C:\Users\Roy\PycharmProjects\byte_encoding\byte_encoding\data\wserver101-Week-36-Year-2017.zip")
with ZipFileExtractorIterator(path_to_zip) as z:
    for uncompressed_temp_file in z:
        logging.info(f"Processing {uncompressed_temp_file}")
        Pen(uncompressed_temp_file).load_to_df().to_csv(usedate=True, mode="a", header=False, path_or_buf="temp2/")
