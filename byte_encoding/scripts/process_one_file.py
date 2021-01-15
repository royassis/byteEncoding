from pathlib import Path
import helpers

filepath= Path (r"C:\Users\Roy\PycharmProjects\byte_encoding\byte_encoding\data\Pen2_20170909_raw")
with open(filepath, "rb") as fp:
    data = fp.read()


out_path = r"C:\Users\Roy\PycharmProjects\byte_encoding\byte_encoding\data\20170909_Pen2_AnotherTry.txt"
outstr = ""
value_size = 8
with open(out_path, "w") as fp:
    idx = 0
    while True:
        s1 = idx * value_size * 2
        e1 = s1 + value_size
        s2 = e1
        e2 = s2 + value_size

        try:
            ts = helpers.bytes_to_datetime( data[s1 : e1], timeformat = "%Y-%m-%d %H:%M:%S")
            value= helpers.byte_to_double( data[s2 : e2])

            line = f"{ts}\t{value}\n"
            print(line)
            fp.write(line)
            idx = idx + 1
        except IndexError as e:
            break


