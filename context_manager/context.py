"""
    Context managers provide a clean interface for obaining and releasing resources.
    To do this, we need to add the magic method __enter__ and __exit__ to the class of function.
"""
import time

from typing import Any
from random import sample
from string import ascii_letters
from pathlib import Path


class TempFile:
    def __init__(self, filename=None) -> None:
        print("Entering init...")
        if not filename:
            filename = "".join(sample(ascii_letters, 10))
            filename = filename + '.txt'
        self.file = Path(filename)
        self.file_handle = None  # Initialize the file handle to None
        print(f"The current file path is: {self.file}")
        print(f"Does {self.file} exist:{self.file.is_file()}")
        
    def __enter__(self):
        print("Entering __enter__...")
        print(f"The current self.file.parent path is: {self.file.parent}")
        print(f"Does self.file.parents exist:{self.file.parents}")
        self.file.parent.mkdir(parents=True, exist_ok=True)
        
        #If file exist, delete it
        if self.file.exists():
            self.file.unlink()
            
        # Recreate the file and open it
        self.file.touch()
        return self.file.open("w")
        
    
    def __exit__(self, *args):
        print("Entering __exit__...")
        self.file.unlink()
        # retries = 5
        # while retries > 0:
        #     try:
        #         self.file.unlink()
        #         break
        #     except PermissionError:
        #         retries -= 1
        #         time.sleep(0.5)  # Wait half a second before retrying
        #     if retries == 0:
        #         print(f"Failed to delete {self.file} after multiple attempts.")
        
        
# with TempFile() as tf:
#     tf.write(" This is a tempfile context manager test\n File will be deleted shortly\n")
#     tf.flush()
#     time.sleep(2)
        

class Except:
    def __init__(self, *exc_types, message=None):
        self.exc_types = exc_types
        self.message = message
        
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_message, exc_trace_back):
        if exc_type in self.exc_types:
            if self.message and self.message in exc_message.args:
                return True
            elif self.message:
                return
            return True
        raise Exception(f"Expected one of {self.exc_types} Exceptions.")
        
    