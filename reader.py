"""
octeon_locale reader
"""
import os.path
from pprint import pprint
def read(path):
    with open(os.path.normpath(path), encoding="unicode_escape") as f:
        data = f.read().split("--- ")[1:]
        readed = {}
        for string in data:
            readed[string.split("\n")[0]] = "\n".join(string.split("\n")[1:])[:-1]
        return readed

if __name__ == '__main__':
    pprint(read("core/en.octeon_locale"))