"""
A client we are working with encoded data in bytes.

Use this code to extract information about sensors measurements
encoded in repeted sequences of 8 bytes.

[timestamp [8bytes] , measurement [8bytes] ]*
"""

import datetime
import array
from typing import Generator, Union, Any


def byte_to_double(new_bytearr: bytearray) -> float:
    """
    Wrapper for array.array()

    :param new_bytearr: 8 byte chunck representing Double
    :return: float
    """
    return array.array('d', new_bytearr)[0]


def bytes_to_datetime(new_bytearr: bytearray) -> datetime:
    """
    Converts eight bytes to datetime

    :param new_bytearr: 8 byte chunck representing Double
    :return: datetime object
    """
    doubles_sequence = byte_to_double(new_bytearr)
    seconds = (doubles_sequence - 25569) * 86400.0
    dt_obj = datetime.datetime.utcfromtimestamp(seconds)

    return dt_obj.strftime("%Y-%m-%d-%H-%M-%S")


def read_bytes_generator(p: str) -> Generator[list[Union[str, float]], Any, None]:
    """
    :param p: string representing filepath
    :return: generator
    """
    double_bytes = 8

    with open(p, "rb") as fp:
        while True:
            datetime_bytes = fp.read(double_bytes)
            measure_bytes = fp.read(double_bytes)

            if len(measure_bytes) != 8 or len(datetime_bytes) != 8:
                break

            dt = bytes_to_datetime(datetime_bytes)
            measure = byte_to_double(measure_bytes)

            yield ([dt, measure])


def main():
    p = "40bytes_from_original.txt"
    bytesgen = read_bytes_generator(p)

    for i in bytesgen:
        print(i)


if __name__ == "__main__":
    main()
