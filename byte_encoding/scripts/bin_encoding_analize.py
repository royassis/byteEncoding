"""
Reading and converting encoded data to datetime and float
"""
import datetime
import array

# Path to bin file
p = "40bytes_from_original.bin"

# Read 8*4 bytes
with open(p, "rb") as fp:
    all = fp.read(32)

# read 8*4 bytes in chunks
for i in range(0, len(all), 8):
    eight_bytes = all[i:i + 8]
    print(list(all[i:i + 8]))

# Print chunks
with open(p, "rb") as fp:
    d1 = fp.read(8)
    v1 = fp.read(8)
    d2 = fp.read(8)
    v2 = fp.read(8)

# Convery bytes to double
doubles_sequence1 = array.array('d', d1)[0]
doubles_sequence2 = array.array('d', d2)[0]

seconds1 = (doubles_sequence1 - 25569) * 86400.0
seconds2 = (doubles_sequence2 - 25569) * 86400.0

# Print bytes converted to datetime
print(datetime.datetime.utcfromtimestamp(seconds1))
print(datetime.datetime.utcfromtimestamp(seconds2))
