import unittest
from utils import PenGeneralIterator, RawIterators
from pathlib import Path
import zipfile

path = Path(r"C:\Users\Roy\PycharmProjects\byte_encoding\byte_encoding\tests\fixtures\Pen2_20170909_raw")
zpath = Path(r"C:\Users\Roy\PycharmProjects\byte_encoding\byte_encoding\tests\fixtures\wserver102-Week-53-Year-2020.zip")

class TestPenReader(unittest.TestCase):

    def test_all(self):
        data = []
        for datapoint in PenGeneralIterator(path, RawIterators.raw_filepath_iterator):
            data.append(datapoint)
        self.assertGreater(len(data), 20)

        with zipfile.ZipFile(path_to_zip) as z:
            for uncompressed_temp_file in z:
                logging.info(f"Processing {uncompressed_temp_file}")
                Pen(uncompressed_temp_file).load_to_df().to_csv(usedate=True, mode="a", header=False,
                                                                path_or_buf="temp2/")


if __name__ == '__main__':
    unittest.main()