from pathlib import Path

class FileStream:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        
    def __enter__(self):
        self.filestream = open(self.path, self.mode)
        return self.filestream
    
    def __exit__(self, exc_type, exc_msg, trace_back):
        self.filestream.close()
        
        
def write_to_file(filename_path, data):
    print("writing to file")
    with FileStream(filename_path, 'w') as f:
        f.write(data)
    
    print("Done writing to file and the file is now:", f.closed)
    

def read_file(filename_path):
    print("Reading from file")
    with FileStream(filename_path, 'r') as f:
        print(f.read())
    
    print("Done reading from file and the file is now:", f.closed)
    
    
if __name__ == '__main__':
    data = "Hi I am Emmanuel Okoro, and currently experimenting with python's context manager"
    file_path = Path.cwd().joinpath("test_file.txt")
    file_path.touch()
    
    write_to_file(file_path, data)
    read_file(file_path)
    
    