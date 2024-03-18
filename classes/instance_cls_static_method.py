import math

class Pizza:
    def __init__(self, radius: int,  ingredents: list):
        self.radius = radius
        self.ingredents = ingredents
        
    @classmethod
    def margherita(cls):
        radius = 5
        ingredents = ['mozzarella', 'tomatoes', 'cheese']
        return cls(radius, ingredents )      
    
    @classmethod
    def prosciutto(cls):
        radius = 8
        ingredents = ['mozzarella', 'tomatoes', 'cheese', 'ham', 'pineapple']
        return cls(radius, ingredents )
                                                                                 
    def area_of_pizza(self):
        return self.area(self.radius)
    
    @staticmethod
    def area(radius):
        return radius**2 * math.pi  
    
    def __repr__(self) -> str:
        return (f"(Pizza-size: {self.area_of_pizza()}, Pizza-ingredents: {self.ingredents})")        
    
if __name__ == "__main__":
    marg_pizza = Pizza.margherita()        
    pros_pizza = Pizza.prosciutto()             
    
    print(marg_pizza)      
    print(pros_pizza)  
    
    print(marg_pizza.area_of_pizza())     
    
    print(f"The area of pizza with 20 radius is: {Pizza.area(20)}")                                          
    
    
"""
Class Method:
    These methods operate on the class itself rather than instances of the class. 
    They have access to class variables but not instance variables. They are defined using the @classmethod decorator.
    Use cases:
        Alternative Constructors: Class methods are often used as alternative constructors. They provide ways to create instances using different input formats or configurations and also implement the 'DRY' principle.
        Accessing Class Variables: Class methods have access to class variables, making them useful for operations that involve class-level data but don't require access to instance data.
        Factory Methods: Class methods can be used to create instances of subclasses or other related classes, acting as factory functions.

Instance Methods:
    These methods operate on instances of the class and have access to instance variables. 
    The first parameter of an instance method is always self, which refers to the instance itself.
    Use Cases:
        Manipulating Instance Data: Instance methods can access and manipulate instance variables, allowing them to perform operations specific to individual instances.
        Encapsulating Behavior: Instance methods encapsulate behavior associated with individual instances. 
        For example, a drive() method in a Car class could encapsulate the behavior of driving a specific car instance.
        
Static Method:
    These methods don't depend on the instance or class state. They are defined using the @staticmethod decorator. 
    They are similar to regular functions but are logically related to the class.
    Use Cases:
        Utility Functions: Static methods are often used for utility functions that are related to the class but don't depend on instance or class state. 
        These functions can perform tasks that are relevant to the class but don't require access to instance or class variables.
        Grouping Functions: Static methods can be used to group related functions within a class, making the code more organized and easier to understand
 
"""
        