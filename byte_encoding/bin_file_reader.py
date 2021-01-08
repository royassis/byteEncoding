"""
A client we are working with encoded data in bytes.

Use this code to extract information about sensors measurements
encoded in repeted sequences of 8 bytes.

[timestamp [8bytes] , measurement [8bytes] ]*
"""

from typing import Generator, Union, Any
import helpers


def get_data_generator(zippath: str) -> Generator[list[Union[str, float]], Any, None]:
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

        measure = helpers.MeasurePoint(datetime_bytes, measure_bytes)

        # return stuff
        yield (measure)


def main():
    # Path to zip
    path_to_zip = "data/40bytes_from_original.zip"

    # Generator
    zip_data_generator = get_data_generator(path_to_zip)

    # each iteration returns data object
    for data_point in zip_data_generator:
        print(data_point)


if __name__ == "__main__":
    main()
