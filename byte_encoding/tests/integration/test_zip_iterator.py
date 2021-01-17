import unittest
from utils import PenGeneralIterator, RawIterators
from ZipIterators import ZipFileExtractorIterator
from pathlib import Path

path = Path(r"C:\Users\Roy\PycharmProjects\byte_encoding\byte_encoding\tests\fixtures\Pen2_20170909_raw")
zpath = Path(r"C:\Users\Roy\PycharmProjects\byte_encoding\byte_encoding\tests\fixtures\wserver102-Week-53-Year-2020.zip")

class TestZipFileExtractorIterator(unittest.TestCase):

    def test_sain(self):
        for _ in ZipFileExtractorIterator(zpath):
            pass

if __name__ == '__main__':
    unittest.main()