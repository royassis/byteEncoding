import hashlib
import pandas as pd
import datetime

file1 = r"C:\Users\Roy\PycharmProjects\byte_encoding\byte_encoding\data\20170909_mine.txt"
file2 = r"C:\Users\Roy\PycharmProjects\byte_encoding\byte_encoding\data\20170909_ronen.txt"

def get_md5(file):
    with open(file) as file_to_check:
        data = file_to_check.read()
    return hashlib.md5(data.encode("utf8")).hexdigest()

h1 = get_md5(file1)
h2 = get_md5(file2)

print(h2 == h1)

names = ["sensor","ts","value"]
df1 = pd.read_csv(file1, delimiter = "\t", names = names)
df2 = pd.read_csv(file2, delimiter = "\t", names = names)

# df1["ts"] == df1["ts"].apply(lambda x : datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))
# df2["ts"] == df2["ts"].apply(lambda x : datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))
df1["frame"] = 1
df2["frame"] = 2

diff = pd.concat([df1,df2]).drop_duplicates(subset = names, keep=False)

2423799
diff.sort_values(["sensor","ts","frame"])

cond1 = (df1["sensor"] == 2) & (df1["ts"] == "2017-09-09 00:00:39")
cond2 = df2["ts"] == "2017-09-09 00:00:39"

df1[df2.sensor == 2].ts.head(50)
df2[df2.sensor == 2].ts.head(50)

df1.loc[11937189]
df2.loc[11937189]

format = "%Y-%m-%d %H:%M:%S"

mergeindex = df1.merge(df2, left_index = True, right_index = True)
cond = mergeindex["ts_x"] != mergeindex["ts_y"]
compare = mergeindex.loc[cond, ["ts_x","ts_y"]]


compare["ts_x"] = compare["ts_x"].apply(lambda x : datetime.datetime.strptime(x, format))
compare["ts_y"] = compare["ts_y"].apply(lambda x : datetime.datetime.strptime(x, format))

max(compare["ts_x"] -  compare["ts_y"])


"""
Summary

My output and Ronen's have the same number of entries
Each sensor have the same number of entires
Merging on index the value and sensor columns are identical

The only difference is a 1 sec difference in a few places
"""
