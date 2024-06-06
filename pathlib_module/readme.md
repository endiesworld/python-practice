# pathlib

A module that allows one to deal with path in windows or in linux(posix). You do not have to worry on what os your code will run on i.e:
    windows = ('C:\Users\endie\Desktop\my_folder\my_file.txt')
    linux = ('/home/endie/Desktop/my_folder/my_file.txt')
    macOS = ('/Users/endie/Desktop/my_folder/my_file.txt')
pathlib has basically two different sections:
1). PurePath (Basically for path manipulation e.g joining and extracting path ).
    This is the base class for all path objects. It represents a path without any filesystem-specific semantics. There are basically two different options to chose from when carrying out path manipulation.
    PurePosixPath and PureWindowsPath: These classes inherit from PurePath and provide platform-specific path manipulation. PurePosixPath is used for POSIX systems (Linux, macOS), while PureWindowsPath is used for Windows.
2). Path(Basically for interacting with the filesystem that the application is running on).
    This class inherits from PurePath and provides a concrete path that is specific to a particular filesystem. It includes methods for interacting with the filesystem, such as creating directories and files.
    PosixPath and WindowsPath: These classes inherit from Path and provide platform-specific path manipulation. PosixPath is used for POSIX systems (Linux, macOS), while WindowsPath is used for Windows.
