from decorators import uppercase_operator


@uppercase_operator
def greet():
    return "hello world"


print(greet())