

def fn_triangles(side_1: int, side_2: int, side_3: int)->str:
    #  TODO: implement zero-length and negative lengths test
    
    if(invalid_triangles(side_1, side_2, side_3)):
        raise ValueError("Invalid triangle sides.")
    
    
def invalid_triangles(side_1: int, side_2: int, side_3: int)->bool:
    sum_1_2 = side_1 + side_2
    sum_1_3 = side_1 + side_3
    sum_2_3 = side_2 + side_3
    
    if(sum_1_2 < side_3):
        return True
    if(sum_1_3 < side_2):
        return True
    if(sum_2_3 < side_1):
        return True
    
    return False
    
def equilateral_triangle(side_1: int, side_2: int, side_3: int)->bool:
    if((side_1 == side_2) and ( side_1 == side_3)):
        return True
    return False

def isosceles_triangle(side_1: int, side_2: int, side_3: int)->bool:
    if((side_1 == side_2) or ( side_1 == side_3) or ( side_2 == side_3)):
        return True
    return False