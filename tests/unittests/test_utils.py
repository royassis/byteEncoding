import unittest
from utils import PenGeneralIterator, RawIterators
from pathlib import Path
import zipfile

path = Path(r"/tests/fixtures/Pen2_20170909_raw")
zpath = Path(r"/tests/fixtures/wserver102-Week-53-Year-2020.zip")

class TestPenReader(unittest.TestCase):

    def test_pen_decoder_iterator_path(self):
        data = []
        for datapoint in PenGeneralIterator(path, RawIterators.raw_filepath_iterator):
            data.append(datapoint)
        self.assertGreater(len(data), 20)

    def test_pen_decoder_iterator_zpath(self):
        z = zipfile.ZipFile(zpath)
        archfile = z.namelist()[-20]
        archfilehandle = z.open(archfile)

        data = []
        for datapoint in PenGeneralIterator(archfilehandle, RawIterators.raw_archfile_iterator):
            data.append(datapoint)
        self.assertGreater(len(data), 0)

    def test_pen_decoder_iterator_data(self):
        z = zipfile.ZipFile(zpath)
        archfile = z.namelist()[-20]
        bytedata = z.read(archfile)

        data = []
        for datapoint in PenGeneralIterator(bytedata, RawIterators.raw_data_iterator):
            data.append(datapoint)
        self.assertGreater(len(data), 0)


if __name__ == '__main__':
    unittest.main()