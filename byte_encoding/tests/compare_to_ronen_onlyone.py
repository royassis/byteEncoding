import hashlib
import pandas as pd
import datetime

file1 = r"C:\Users\Roy\PycharmProjects\byte_encoding\byte_encoding\data\20170909_Pen2_AnotherTry.txt"
file2 = r"C:\Users\Roy\PycharmProjects\byte_encoding\byte_encoding\data\20170909_ronen.txt"

df1 = pd.read_csv(file1, delimiter = "\t", names = ["ts","value"])
df2 = pd.read_csv(file2, delimiter = "\t", names = ["sensor","ts","value"])
df2 = df2[df2.sensor == 2].drop("sensor", axis = 1)

print(df1.shape, df2.shape)

dateformat = "%Y-%m-%d %H:%M:%S"

df1["ts"] = df1["ts"].apply(lambda x : datetime.datetime.strptime(x, dateformat))
df2["ts"] = df2["ts"].apply(lambda x : datetime.datetime.strptime(x, dateformat))

df1 = df1.sort_values("ts").reset_index()
df2 = df2.sort_values("ts").reset_index()

diff = pd.concat([df1,df2]).drop_duplicates(keep=False)

mergeindex = df1.merge(df2, left_index = True, right_index = True)
cond = mergeindex["ts_x"] != mergeindex["ts_y"]
compare = mergeindex.loc[cond, ["ts_x","ts_y"]]

print(max(compare["ts_x"] -  compare["ts_y"]))


