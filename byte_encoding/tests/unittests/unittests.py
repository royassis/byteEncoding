import unittest
from myclasses import PenFileReader

path = r"/tests/fixtures/Pen2_20170909_raw"

class TestPenReader(unittest.TestCase):

    def class_inits(self):
        try:
            PenFileReader(path)
        except:
            self.fail()

    def test_read_all(self):
        with PenFileReader(path) as p:
            data = p.read_all()
        self.assertGreater(len(data), 0)

    def test_read_all_no_err(self):
        try:
            with PenFileReader(path) as p:
                data = p.read_all()
        except:
            self.fail()

    def test_iter(self):
        data = []
        with PenFileReader(path) as p:
            for result in p :
                data.append(result)
        self.assertGreater(len(data), 0)

    def test_iter_no_err(self):
        try:
            with PenFileReader(path) as p:
                for _ in p :
                    pass
        except:
            self.fail()


if __name__ == '__main__':
    unittest.main()