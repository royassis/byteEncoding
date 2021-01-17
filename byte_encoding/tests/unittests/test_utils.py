import unittest
from utils import zfile_read_sain

path = r"/tests/fixtures/Pen2_20170909_raw"

class TestPenReader(unittest.TestCase):

    def test_zfile_read_sain_not_breaks(self):
        try:
            for _ in zfile_read_sain(path):
                pass
        except:
            self.fail()

    def test_zfile_read_sain_returns_data(self):
        data = []
        for datapoint in zfile_read_sain(path):
            data.append(datapoint)
        self.assertGreater(len(data), 0)

if __name__ == '__main__':
    unittest.main()