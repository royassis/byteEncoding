"""
A client we are working with encoded data in bytes.

Use this code to extract information about sensors measurements
encoded in repeted sequences of 8 bytes.

[timestamp [8bytes] , measurement [8bytes] ]*
"""

from typing import Generator, Union, Any
import helpers

def read_bytes_generator(zippath: str) -> Generator[list[Union[str, float]], Any, None]:
    """
    Returns a generator to read timestamp, measurement data
    encoded in binary format.

    :param p: string representing filepath
    :return: generator
    """
    double_bytes = 8

    # Get filehandle from zip
    filehandle = helpers.get_file_handle_from_zip(zippath)

    while True:
        # Read from file
        datetime_bytes = filehandle.read(double_bytes)
        measure_bytes = filehandle.read(double_bytes)

        # End of file
        if len(measure_bytes) != 8 or len(datetime_bytes) != 8:
            break

        # Convert bytes to stuff
        dt = helpers.bytes_to_datetime(datetime_bytes)
        measure = helpers.byte_to_double(measure_bytes)

        # return stuff
        yield ([dt, measure])


def main():
    # Path to zip
    pathtozip = "data/40bytes_from_original.zip"

    # Generator
    bytesgen = read_bytes_generator(pathtozip)

    # each iteration returns list([dt, measure])
    for stuff in bytesgen:
        print(stuff)


if __name__ == "__main__":
    main()
