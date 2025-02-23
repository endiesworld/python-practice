# # from dataclasses import dataclass
# # from typing import NamedTuple
# # from collections import namedtuple
# from typing import List, Optional
# import json
# import uuid

# print(str(uuid.UUID('8cd89c38-d5ca-41ae-a838-0975cb9aa04b')))
# # @dataclass(frozen=True)
# # class Name:
# #     first_name: str
# #     surname: str

# # class Money(NamedTuple):
# #     currency: str
# #     value: int
    
    
# # Line = namedtuple('Line', ['sku', 'qty'])

# # class Person:
# #     def __init__(self, name: Name):
# #         self.name = name

# # def test_equality():
# #     print("*******************Value Object base test*************")
# #     print(Money('gbp', 10) == Money('gbp', 10))
# #     print(Name('Harry', 'Percival') != Name('Bob', 'Gregory'))
# #     print(Line('RED-CHAIR', 5) == Line('RED-CHAIR', 5))
    

# # result = ord('m')    

# # print(f'**********ord of m is {result}**********')
# # def test_barry_is_harry():
# #     print("*******************Entity base test*************")
# #     harry = Person(Name("Harry", "Percival"))
# #     barry = harry

# #     barry.name = Name("Barry", "Percival")

# #     print(harry is barry and barry is harry)
    
# # if __name__ == "__main__":
# #     test_equality()
# #     test_barry_is_harry()



# type = 'value'

# def my_fnc(type: Optional[str] = None):
#     type_str = "TRUE" if not type else "type ILIKE '%{}%'".format(type)
    
#     return type_str


# print(my_fnc(type))


# print(json.dumps(CREATE_PROVIDER))

# how_many_snakes = 1
# snake_string = """
# Welcome to Python3!

#              ____
#             / . .\\
#             \  ---<
#              \  /
#    __________/ /
# -=:___________/

# """

# print(snake_string * how_many_snakes)

# # expression = eval(input("Enter an expression:"))

# # print('The result from the expression entered is: ', expression)

# names =  input("Enter student names:")
# assignments =  input("Enter student numbers of assignments pending:")
# grades =  input("Enter student current grades:")

# names = names.split(',')
# assignments = assignments.split(',')
# grades = grades.split(',')
# ## message string to be used for each student
# ## HINT: use .format() with this string in your for loop
# message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
# submit before you can graduate. Your current grade is {} and can increase \
# to {} if you submit all assignments before the due date.\n\n"

# ## write a for loop that iterates through each set of names, assignments, and grades to print each student's message

# for name, assignment, grade in zip(names, assignments, grades):
#     print(message.format(name, assignment, grade, str(int(grade) + int(assignment))))
# n = 6
# k = 2
# binomial_coefficient = 1
# for i in range(1, k + 1):
#     binomial_coefficient *= (n - i + 1) / i
    
# print(binomial_coefficient)


def factorial(x):
    x_improved = x + 1
    result = 1
    if(x < 2):
        return result
    for data in range(1, x_improved):
        result *= data
    return result

def swap_arr_element(arr: list):
    temp = arr[0]
    arr[0] = arr[1]
    arr[1] = temp

if __name__ == '__main__':
    myArray = [1, 2, 3, 4, 5]
    print("swapped array: " , myArray)
    swap_arr_element(myArray)
    print("swapped array: " , myArray)
    
    # result= factorial(5)
    
    # print(result)