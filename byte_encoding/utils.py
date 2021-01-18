import datetime
import array
from .config import VALUE_SIZE, SEGMENT_SIZE
import re
import io
import zipfile


def byte_to_double(new_bytearr: bytearray) -> float:
    """
    Wrapper for array.array()

    :param new_bytearr: 8 byte chunck representing Double
    :return: float
    """
    return array.array('d', new_bytearr)[0]


def bytes_to_datetime(new_bytearr: bytearray):
    """
    Converts eight bytes to datetime

    :param new_bytearr: 8 byte chunck representing Double
    :return: datetime object
    """
    doubles_sequence = byte_to_double(new_bytearr)
    seconds = (doubles_sequence - 25569) * 86400.0
    dt_obj = datetime.datetime.utcfromtimestamp(seconds)

    return dt_obj


def decode_sgement(raw_bytes):
    return bytes_to_datetime(raw_bytes[:VALUE_SIZE]), byte_to_double(raw_bytes[VALUE_SIZE:])


def basic_iteration_logic(hadnle):
    while True:
        data = hadnle.read(SEGMENT_SIZE)
        if len(data) == 0:
            break
        yield data


class RawIterators():
    @staticmethod
    def raw_data_iterator(data):
        virtual_filehandle = io.BytesIO(data)
        return basic_iteration_logic(virtual_filehandle)

    @staticmethod
    def raw_archfile_iterator(zfilehandle):
        return basic_iteration_logic(zfilehandle)

    @staticmethod
    def raw_filepath_iterator(filehandle):
        with open(filehandle, "rb") as f:
            return basic_iteration_logic(f)


def PenGeneralIterator(pen_iterable, pen_generator):
    for segment in pen_generator(pen_iterable):
        ts, val = decode_sgement(segment)
        yield ts, val


def filter_namelist(archnamelist):
    return [archfile for archfile in archnamelist if re.match(r".*Pen.*", archfile)]


def get_sensor_number(filename):
    file_format = r".*Pen(?P<sensor_number>\d+).*"
    match = re.match(file_format, str(filename))
    return match.group("sensor_number")


def get_sensor_date_from_data(filehandle):
    it = PenGeneralIterator(filehandle)
    ts, _ = it.__next__()
    return ts


def get_sensor_date_from_filepath(filepath):
    patten = r".*(\d{4} \d{2} \d{2}).*"
    dateformat = "%Y %m %d"

    match = re.match(patten, filepath)
    if match:
        datestr = match.groups()[0]
        dateobj = datetime.datetime.strptime(datestr, dateformat)
    return dateobj


def get_date_list_in_zip(zippate):
    date_list = set()
    z = zipfile.ZipFile(zippate)
    nl = z.namelist()
    for filepath in nl:
        dateobj = get_sensor_date_from_filepath(filepath)
        date_list.add(dateobj)

    return date_list
