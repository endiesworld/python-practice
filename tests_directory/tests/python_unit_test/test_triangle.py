import unittest
from triangle import equilateral_triangle, fn_triangles

class TestTriangle(unittest.TestCase):
    # Test when all sides are equal
    def test_equilateral_triangle_false(self):
        self.assertEqual(equilateral_triangle(2, 3, 5), False)
        
    def test_equilateral_triangle_true(self):
        self.assertEqual(equilateral_triangle(5, 5, 5), True)
    
    
    # def test_fn_triangles_error_without_context(self):
    #     self.assertRaises(ValueError, fn_triangles, 1,3,5)
        
    # def test_fn_triangles_error_with_context(self):
    #     with self.assertRaises(ValueError) as message:
    #         fn_triangles(1,3,5) 
    #     self.assertEqual(str(message.exception), "Invalid triangle sides.")
    
    
    

if __name__ == '__main__':
    unittest.main()