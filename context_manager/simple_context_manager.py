from random import sample
from string import ascii_letters
from pathlib import Path
import time


def write_to_file(filename=None):
    filename: str = filename
    if not filename:
        filename = "".join(sample(ascii_letters, 15)) + '.txt'
        
    concrete_file = Path.cwd().joinpath(filename)
    concrete_file.touch()
    
    with open(concrete_file, 'w') as f:
        f.write('Hello, world\n')
        f.write('This random file will be deleted in 20secs.')
        f.flush()
        time.sleep(5)
        
    with open(concrete_file, 'r') as f:
        print(f.readlines())
        
    concrete_file.unlink()

if __name__ == '__main__':
    write_to_file()