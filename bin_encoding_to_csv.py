import datetime
import array

def byte_to_double(new_bytearr):
    return array.array('d', new_bytearr)[0]

def bytes_to_datetime(new_bytearr):
    doubles_sequence = byte_to_double(new_bytearr)
    seconds = (doubles_sequence - 25569) * 86400.0
    dt_obj = datetime.datetime.utcfromtimestamp(seconds)

    return dt_obj.strftime("%Y-%m-%d-%H-%M-%S")

def read_bytes_generator(p):
    double_bytes = 8

    with open(p, "rb") as fp:
        while True:
            datetime_bytes = fp.read(double_bytes)
            measure_bytes = fp.read(double_bytes)

            if len(measure_bytes) != 8 or len(datetime_bytes) != 8:
                break

            dt = bytes_to_datetime(datetime_bytes)
            measure = byte_to_double(measure_bytes)

            yield([dt, measure])

p = "40bytes_from_original.txt"
bytesgen = read_bytes_generator(p)

for i in bytesgen:
    print(i)