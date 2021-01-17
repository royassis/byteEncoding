import pandas as pd

file1 = r"C:\Users\Roy\PycharmProjects\byte_encoding\byte_encoding\data\20170909_ronen.txt"

names = ["number","ts","val"]
df1 = pd.read_csv(file1, delimiter = "\t", names= names)

df1[df1[["ts","number"]].duplicated(keep = False)]

if df1[["ts","number"]].duplicated().any():
    raise Exception ("duplicated timestemps")



