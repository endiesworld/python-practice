from input_output import keyboard_input_int

# from input_output import *   (Brings in everything, and you can access each method individually)
# import input_output (Brings in everything, and you can access using file_name.method_name())
user_input = keyboard_input_int(user_message='Please enter your age')

print(f'you are {user_input} years old')
