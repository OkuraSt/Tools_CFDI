from bs4 import BeautifulSoup
from os.path import join as join_path, dirname, abspath


def parse_xml(path):
    with open(path) as file:
        xml_object = BeautifulSoup(file.read(), "lxml")
        return xml_object


if __name__ == '__main__':
    current_directory = dirname(abspath(__file__))
    filename = join_path(current_directory, '..\\xmls\\2469.xml')
    xml = parse_xml(filename)
    print xml
