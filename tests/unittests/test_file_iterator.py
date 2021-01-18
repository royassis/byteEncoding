import unittest
from byte_encoding.FileOrEquivalentIterators import FileIterator, BytesArrayIterator
from pathlib import Path


path = Path(r"C:\Users\Roy\PycharmProjects\byte_encoding\tests\fixtures\Pen2_20170909_raw")
with open(path.absolute(), "rb") as f:
    data = f.read()


class TestFileIterator(unittest.TestCase):

    def test_sain_FileIterator(self):
        with FileIterator(path.absolute()) as f:
            for _ in f:
                break

    def test_sain_BytesArrayIterator(self):

        for i in BytesArrayIterator(data):
            break


if __name__ == '__main__':
    unittest.main()