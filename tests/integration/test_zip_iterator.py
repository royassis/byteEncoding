import unittest
from ZipIterators import ZipFileExtractorIterator, ZipFileHandleIterator
from pathlib import Path

path = Path(r"/tests/fixtures/Pen2_20170909_raw")
zpath = Path(r"/tests/fixtures/wserver102-Week-53-Year-2020.zip")

class TestZipFileExtractorIterator(unittest.TestCase):

    def test_sain_ZipFileExtractorIterator(self):
        with ZipFileExtractorIterator(zpath) as ziter:
            for stuff in ziter:
                print(stuff)

    def test_sain_ZipFileHandleIterator(self):
        with ZipFileHandleIterator(zpath) as ziter:
            for stuff in ziter:
                print(stuff)

if __name__ == '__main__':
    unittest.main()