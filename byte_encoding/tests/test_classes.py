from myclasses import PenReader

path = r"C:\Users\Roy\PycharmProjects\byte_encoding\byte_encoding\tests\fixtures\Pen2_20170909_raw"

p = PenReader(path)

with PenReader(path) as p:
    data = p.read_all()
print(len(data))

data = []
with PenReader(path) as p:
    for result in p :
        data.append(result)
    print(len(data))


data = []
with PenReader(path) as p:
    for result in p.read_line() :
        data.append(result)
    print(len(data))


