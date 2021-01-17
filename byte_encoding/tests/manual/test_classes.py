from myclasses import PenFileReader

path = r"/tests/fixtures/Pen2_20170909_raw"

p = PenFileReader(path)

with PenFileReader(path) as p:
    data = p.read_all()
print(len(data))

data = []
with PenFileReader(path) as p:
    for result in p :
        data.append(result)
    print(len(data))



