class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, next_node):
        self.next_node = next_node

# Create your LinkedList class below:

class LinkedList:
    def __init__(self, value = None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node
    
    def insert_beginning(self, new_value):
        new_node = Node(new_value) 
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    
    def stringify_list(self):
        list = ''
        ptr = self.head_node
        while(ptr != None):
            list = list+str(ptr.value)+'\n'
            ptr = ptr.get_next_node()
        return list
    
    def remove_node(self, value_to_remove):
        current_node = self.head_node
        if(current_node.get_value() == value_to_remove):
            self.head_node = self.head_node.get_next_node()
        else:
            past_node = current_node
            while(current_node):
                if(current_node.get_value() == value_to_remove):
                    past_node.set_next_node(current_node.get_next_node())
                    current_node = None
                else:
                    past_node = current_node
                    current_node = current_node.get_next_node()
        


if __name__ == '__main__':
    ll = LinkedList(5)
    ll.insert_beginning(70)
    ll.insert_beginning(5675)
    ll.insert_beginning(90)
    print(ll.stringify_list())
    ll.remove_node(5675)
    print("********************************")
    print(ll.stringify_list())