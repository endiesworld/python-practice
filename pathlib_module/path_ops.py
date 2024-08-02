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




def generate_random_text_file(length):
    import random
    import string
    
    letters = string.ascii_letters + string.digits
    random_text = ''.join(random.choice(letters) for i in range(length))
    return random_text + '.txt'


def general_path_methods():
    current_dir = Path.cwd() # current directory cwd() points to the directory where the python command runs
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
    
    
"""
File manipulation can also be used on files that do not exist yet in the filesystem. 
For this reason, we make use of the 'Pure paths'
"""
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
    
    new_path = Path.home() /'dir1'/'dir2'/'dir3'/'text_file.txt'
    print(f"The newly created directory and file is: {new_path}")
    
    # Decomposing parts of the path with the 'parts' attribute
    decomposed  = my_path.parts
    print(f"The parts of the path 'my_path' are: {decomposed}")
    print(f"The parts of the path 'new_path' are: {new_path.parts}")
    
    print("============ Using the parents property of the Path object")
    #Accessing the parent of a path with the 'parents' property. you can also use 'parent' if our interest is for just one
    for index, parent in enumerate(Path.cwd().parents):
        print(f"{index}: {parent}")
        
    for index, parent in enumerate(new_path.parents):
        print(f"{index}: {parent}")


def concrete_method_in_detail(filename='text_file.txt'):
    with open(filename, 'r') as f:
        print("========= Reading files the conventional way =========")
        print(f.readlines())

    my_file = Path.cwd().joinpath(filename)
    with open(my_file, 'r') as f:
        print("========= Reading files the Path object =========")
        print(f.readlines())
    
    new_dir = Path.cwd().joinpath('dir1')
    
    try:
        new_dir.mkdir()
    except FileExistsError as e:
        print(e)
        
    print(f"Does the directory 'dir1' exist ? : {new_dir.is_dir()}")
    
    filename = generate_random_text_file(8)
    new_file_path = new_dir.joinpath(filename) 
    
    while Path(new_file_path).is_file():
        filename = generate_random_text_file(8)
        new_file_path = new_dir.joinpath(filename)
    
    print(f"Creating new file: {new_file_path}")
    new_file_path.touch()
    print(f"Does new_file_path file exist ? : {new_file_path.is_file()}")
    
    with open(new_file_path, 'w') as f:
        f.write('Testing the python Path class from the pathlib module \n')
        
    with open(new_file_path, 'r') as f:
        print(f.readlines())
    
    # Delete the random file created
    new_file_path.unlink()
    print(f"Does new_file_path directory exist ? : {new_file_path.exists()}")
    
    try:
    #Delete the dir1 created. Note the dir1 must be empty before it is deleted.
        new_dir.rmdir()
    except FileNotFoundError as e:
        print(e)
        
    print(f"Does new_dir directory exist ? : {new_dir.exists()}")


if __name__ == '__main__':
    # general_path_methods()
    # file_ops()
    # path_manipulation()
    concrete_method_in_detail()