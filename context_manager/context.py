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
        if not filename:
            filename = "".join(sample(ascii_letters, 10))
            filename = filename + '.txt'
        self.file = Path(filename)
        print(f"The current file path is: {self.file}")
        print(f"Does {self.file} exist:{self.file.is_file()}")
        
    def __enter__(self):
        self.file.parent.mkdir(parents=True, exist_ok=True)
        
        #I file exist, delete it
        if self.file.exists():
            self.file.unlink()
            
        # Recreate the file
        self.file.touch()
        return self.file.open("w")
        
    def __exit__(self, *args):
        self.file.unlink()    
        
        
with TempFile() as tf:
    tf.write(" This is a tempfile context manager test\n File will be deleted shortly\n")
    tf.flush()
    time.sleep(20)
        
    