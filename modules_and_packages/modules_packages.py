from input_output import keyboard_input_int

# from input_output import *   (Brings in everything, and you can access each method individually)
# import input_output (Brings in everything, and you can access using file_name.method_name())
""" 
    By default python interpreter will check for the file in the current directory only, 
    and we need to set the file path manually to import the modules from another directory.
    # https://www.geeksforgeeks.org/python-import-module-from-different-directory/
"""

user_input = keyboard_input_int(user_message='Please enter your age')

print(f'you are {user_input} years old')
