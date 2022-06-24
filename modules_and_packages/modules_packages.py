from input_output import keyboard_input_int

# from input_output import *   (Brings in everything, and you can access each method individually)
# import input_output (Brings in everything, and you can access using file_name.method_name())
""" 
    By default python interpreter will check for the file in the current directory only, 
    and we need to set the file path manually to import the modules from another directory.
    # https://www.geeksforgeeks.org/python-import-module-from-different-directory/
"""

"""
    The __name__ is a special built-in variable which evaluates to the name of the current module. 
    However, if a module is being run directly (from command line), then __name__ instead is set to the string “__main__”.
"""

user_input = keyboard_input_int(user_message='Please enter your age')

print(f'you are {user_input} years old')
print(
    f'***This code is running directly in the modules_packages.py file with module name module is {__name__}***')
