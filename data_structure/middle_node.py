from linked_list import LinkedList

"""
    
    Given the linked list with the following elements 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7, the middle node would be the element with value 4.
"""

def middle_node(linked_list):
    current_ptr = linked_list.head_node
    middle_node_ptr = linked_list.head_node
    current_ptr_move_count = 0
    
    while current_ptr:
        if current_ptr_move_count == 2:
            middle_node_ptr = middle_node_ptr.get_next_node()
            current_ptr_move_count = 0
        current_ptr = current_ptr.get_next_node()
        current_ptr_move_count += 1
    
    return middle_node_ptr.value



def main():
    lkd_list = LinkedList()
    for i in range(7):
       lkd_list.insert_beginning(i+1)

    print(lkd_list.stringify_list())
 
    print(middle_node(lkd_list))

if __name__ == '__main__':
    main()