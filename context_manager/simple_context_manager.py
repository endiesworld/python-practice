from random import sample
from string import ascii_letters
from pathlib import Path
import time


def write_to_file(filename=None):
    filename: str = filename
    if not filename:
        filename = "".join(sample(ascii_letters, 15))
    
    with open(filename, 'w') as f:
        f.write('Hello, world')
        f.write('This random file will be deleted in 20secs.')
        f.flush()
        time.sleep(21)

if __name__ == '__main__':
    write_to_file()