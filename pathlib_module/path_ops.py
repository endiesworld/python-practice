"""
When working with the Path class from the pathlib module, you can define paths in two ways:
    Relative Path:
    A relative path is a path that is relative to the current working directory (cwd). Here, '.' denotes the current directory whil '..' denotes the parent directory.
    It doesn't start with a root directory or a drive letter. Instead, it starts from the current directory and navigates to the desired location.
    Absolute Path:
    An absolute path is a path that starts from the root directory or a drive letter and navigates to the desired location. 
    It is independent of the current working directory.
"""
from datetime import datetime
from pathlib import Path

def general_path_methods():
    current_dir = Path.cwd()
    curr_2 = Path('.')

    print(current_dir)
    print(curr_2)
    print(f"is current_dir == curr_2: {current_dir == curr_2}")
    
    print("============== Comparing files dir with absolute() method ==================")
    
    print(current_dir.absolute())
    print(curr_2.absolute())
    print(f"is current_dir.absolute() == curr_2.absolute(): {current_dir.absolute() == curr_2.absolute()}")
    
    print("============== Comparing files dir with samefile() method ==================")
    print(current_dir.samefile(curr_2))
    
    print("============== Using the home() method ==================")
    print(Path.home())
    

def file_ops(filename = 'text_file.txt' ):
    filename = filename
    if not Path(filename).exists():
        with open(filename, 'w') as f:
            f.write('Testing the python Path class fron the pathlib module \n')
    else:
        with open(filename, 'a') as f:
            f.write(f'Added a new file content by this time {datetime.now()}\n')
        
    file = Path('text_file.txt')
    
    abs_file_path = file.absolute()
    print(f"The absolute path to the file is: {abs_file_path}")
    
    file_stat = file.stat()
    file_size = file_stat.st_size
    file_modified_time = file_stat.st_mtime
    print(f"The current file stat is: {file_stat}")
    print(f"The current file size is: {file_size}")
    print(f"The last modified time of the file: {datetime.fromtimestamp(file_modified_time)}")
    
    
def path_manipulation():
    my_path = Path('./dir/dir2/dir3/dir4')
    print(f"The direction of '/' processed for my_path is a function of the os: {my_path}")
    
    # Check for file or directory
    print(f"Is text_file.txt a file and exist: {Path('text_file.txt').is_file()}")
    print(f"Is text_file2.txt a file and exist: {Path('text_file2.txt').is_file()}")
    print(f"Is /Users/endie/Documents a directory and exist: {Path('/Users/endie/Documents').is_dir()}")

    #Creating a directory and file
    proposed_new_dir = Path.cwd().joinpath('new_dir', 'new_dir2', 'text_file.txt') # This doesn't create the path yet
    print(f"The newly created directory and file is: {proposed_new_dir}")
    
    # Using the joing path in production
    parts_of_file = ['dir1', 'dir2', 'dir3', 'my_file.txt']
    proposed_new_dir = Path.cwd().joinpath(*parts_of_file)
    print(f"The newly created directory and file is: {proposed_new_dir}")


if __name__ == '__main__':
    # general_path_methods()
    # file_ops()
    path_manipulation()