from error import error
from Geography_point import GeographyPoint


def parse_point(elem):
    if not elem[0].isdigit() or not elem[1].isdigit() or not elem[2].isdigit():
        error('There is not number in coordinates')
    return GeographyPoint(float(elem[0]), float(elem[1]), float(elem[2]))


def read_map(filename):
    reader = []
    with open(filename) as file:
        info = file.readline()
    info = [x for x in info.split() if x]
    for elem in info:
        if elem[0] != '(' or elem[-1] != ')':
            error('No brackets around coordinates')
        elem = elem[1:-1]
        tmp_elem = elem.split(',')
        if len(tmp_elem) != 3:
            error('There is not 3 coordinates')
        reader.append(parse_point(tmp_elem))
    return reader
