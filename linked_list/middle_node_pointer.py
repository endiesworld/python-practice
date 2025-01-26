"""
    Pointers at Different Speeds
    Using two pointers moving in parallel was a good solution to the previous problem. However, there are other problems where having two pointers moving in parallel wouldn’t be as useful. Let’s take a look at one of those problems and consider a new strategy that uses two pointers moving at different speeds.

    Consider the following problem:

    Create a method that returns the middle node of a linked list.

    For example, given the linked list with the following elements 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7, the middle node would be the element with value 4.    

"""

# Approach

"""

The approach we’ll use to solve this problem is to have two pointers, p1 and p2, both starting at the head of the linked list. 
We’ll move p1 forward by one element and p2 forward by two elements. 
When p2 reaches the end of the linked list, p1 will be pointing to the middle element.

"""
"""
    fast pointer = linked list head
    slow pointer = linked list head
    while fast pointer is not None
        move fast pointer forward
        if the end of the linked list has not been reached
            move fast pointer forward
            move slow pointer forward
    return slow pointer
        
"""

def middle_node(linked_list):
    tail_node = linked_list.get_head_node()
    middle_node = linked_list.get_head_node()
    tail_node_count = 0
    
    while tail_node:
        tail_node = tail_node.get_next_node()
        tail_node_count += 1
        if tail_node_count % 2 == 0:
            middle_node = middle_node.get_next_node()
            
    return middle_node
        

#ALTERNATIVE SOLUTION
def middle_node(linked_list):
    fast_pointer = linked_list.head_node
    slow_pointer = linked_list.head_node
    while fast_pointer:
        fast_pointer = fast_pointer.get_next_node()
        if fast_pointer:
            fast_pointer = fast_pointer.get_next_node()
            slow_pointer = slow_pointer.get_next_node()
    return slow_pointer
