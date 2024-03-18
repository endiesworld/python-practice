class Stack:
    def __init__(self):
        self.item = []
    
    def push(self, item):
        self.item.append(item)
        
    def pop(self):
        return self.item.pop()
    
    def isEmpty(self):
        return not self.item
    
    def peek(self):
        return self.item[-1]
    
    def __str__(self):
        return str(self.item)
    
    
if __name__ == '__main__':
    data = Stack()
    string = 'software'
    for char in string:
        data.push(char)
        
    reversed_str = ''
    print("data", data)
    print("is empty", data.isEmpty())
    while not data.isEmpty():
        reversed_str += data.pop()
        
    print(reversed_str)
            