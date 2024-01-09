class Stack:
    
    def __init__(self, data=None, size=10):
        self.MAX_SIZE = size # Maximum size of stack 10  
        self.current_size = 0
        self.arr = []  
        if data is not None:
            self.arr.append(data)
            self.current_size += 1
            
    
    def push(self, data):
        if self.current_size == self.MAX_SIZE:
            return "Memory full"
        self.arr.append(data)
        self.current_size += 1
        return None
    
    def pop(self):
        if self.current_size == 0:
            return "Memory empty"
        self.current_size -= 1
        return self.arr.pop()
    
    def length(self):
        return self.current_size
    
    


# my_stack = Stack(5, 5)
# for data in range(2, 70, 2):
#     value = my_stack.push(data)
#     if value :
#         print("Stack limit reached at :" ,data)
#         break
    

# for _ in range(100):
#     value = my_stack.pop()
#     if value == 1:
#         break
#     print(value)
    


class StackOfStack:
    
    def __init__(self, stacks=5, sub_stack_size=3):
        self.stack_holder = []
        self.sub_stack_size = stacks
        self.current_sub_stack = 0
        for i in range(stacks):
            self.stack_holder.append(Stack(size=sub_stack_size))
            
    def push(self, data): 
        output = self.stack_holder[self.current_sub_stack].push(data)
        if  output == "Memory full":
            if self.current_sub_stack == self.sub_stack_size -1:
                return "Memory full"
            self.current_sub_stack += 1
            self.stack_holder[self.current_sub_stack].push(data)
        return None
        
    def pop(self):
        output = self.stack_holder[self.current_sub_stack].pop()
        if output == "Memory empty":
            if self.current_sub_stack == 0:
                return "Memory empty"
            self.current_sub_stack -= 1
            return self.stack_holder[self.current_sub_stack].pop()
        
        return output
        
    def pop_at(self, index):
        if index - 1 > self.sub_stack_size:
            return "Index out of bounds"
        current_index = self.current_sub_stack
        self.current_sub_stack  = index - 1
        output = self.stack_holder[self.current_sub_stack].pop()
        self.current_sub_stack = current_index
        return output
            



my_stack_of_stack = StackOfStack()
previous_data = 0
for data in range(2, 70, 2):
    value = my_stack_of_stack.push(data)
    if value :
        print("Stack limit reached at :" ,previous_data)
        break
    previous_data = data


print("Pop from sub-stack : ", my_stack_of_stack.pop_at(1))

for _ in range(100):
    value = my_stack_of_stack.pop()
    if value == "Memory empty":
        print(value)
        break
    print(value)