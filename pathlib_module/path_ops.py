"""
When working with the Path class from the pathlib module, you can define paths in two ways:
    Relative Path:
    A relative path is a path that is relative to the current working directory (cwd). Here, '.' denotes the current directory whil '..' denotes the parent directory.
    It doesn't start with a root directory or a drive letter. Instead, it starts from the current directory and navigates to the desired location.
    Absolute Path:
    An absolute path is a path that starts from the root directory or a drive letter and navigates to the desired location. 
    It is independent of the current working directory.
"""

from pathlib import Path


if __name__ == '__main__':
    current_dir = Path.cwd()
    curr_2 = Path('.')

    print(current_dir)
    print(curr_2)
    print(f"is current_dir == curr_2: {current_dir == curr_2}")
    
    print("============== Using absolute() method ==================")
    
    print(current_dir.absolute())
    print(curr_2.absolute())
    print(f"is current_dir.absolute() == curr_2.absolute(): {current_dir.absolute() == curr_2.absolute()}")