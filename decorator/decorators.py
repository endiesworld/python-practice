def uppercase_operator(func):
    def func_modifyer():
        modify_func = func()
        new_func = modify_func.upper()
        return new_func
    return func_modifyer