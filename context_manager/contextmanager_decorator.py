from contextlib import contextmanager
from pathlib import Path


@contextmanager
def filestream(file_path, mode):
    file = open(file_path, mode)
    yield file
    file.close()
    

def write_to_file(filename_path, data):
    print("writing to file")
    with filestream(filename_path, 'w') as f:
        f.write(data)
    
    print("Done writing to file and the file is now:", f.closed)
    

def read_file(filename_path):
    print("Reading from file")
    with filestream(filename_path, 'r') as f:
        print(f.read())
    
    print("Done reading from file and the file is now:", f.closed)
    

if __name__ == '__main__':
    data = "Hi I am Emmanuel Okoro, and currently experimenting with python's context manager using the @contextmanager decorator from the contextlib package"
    file_path = Path.cwd().joinpath("test_file.txt")
    file_path.touch()
    
    write_to_file(file_path, data)
    read_file(file_path)