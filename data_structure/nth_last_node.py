from linked_list import LinkedList

"""
For example: given a linked list with the following elements 1 -> 2 -> 3 -> 4 -> 5, return the 2nd to last element. 
The answer would be element 4.
In order to do this, you’ll need some way of knowing how far you are from the end of the list itself. 
However, in a singly linked list, there’s no easy way to iterate back through the list when you find the end.

"""

# FIRST APPROACH, but heavy on memory
def list_nth_last(linked_list, n):
    linked_list_as_list = []
    current_node = linked_list.head_node
    while current_node:
        linked_list_as_list.append(current_node)
        current_node = current_node.get_next_node()
    return linked_list_as_list[len(linked_list_as_list) - n]


# SECOND APPROACH
def nth_last_node(linked_list, n):
    tail_seeker = linked_list.head_node
    tail_position = 1
    nth_node = None
    nth_node_position = 0
    while tail_seeker:
        
        if (tail_position - nth_node_position) == n + 1:
            if nth_node is None:
                nth_node = linked_list.head_node
            else:
                nth_node = nth_node.get_next_node()
            nth_node_position += 1
        tail_seeker = tail_seeker.get_next_node()
        tail_position += 1
    return nth_node.value


def main():
    lkd_list = LinkedList()
    for i in range(10):
       lkd_list.insert_beginning(i+1)

    print(lkd_list.stringify_list())
 
    print(nth_last_node(lkd_list, 4))

if __name__ == '__main__':
    main()