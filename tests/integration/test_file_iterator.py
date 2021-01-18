import unittest
from FileOrEquivalentIterators import FileIterator, BytesArrayIterator
from pathlib import Path

path = Path(r"/tests/fixtures/Pen2_20170909_raw")
zpath = Path(r"/tests/fixtures/wserver102-Week-53-Year-2020.zip")

with open(path, "rb") as f:
    data = f.read()

class TestFileIterator(unittest.TestCase):

    def test_sain_FileIterator(self):
        with FileIterator(path) as f:
            for _ in f:
                break

    def test_sain_BytesArrayIterator(self):

        with BytesArrayIterator(data) as f:
            for _ in f:
                break


if __name__ == '__main__':
    unittest.main()