"""
Two Pointers Moving in Parallel
Consider the following problem:

Create a method that returns the nth last element of a singly linked list.

For example: given a linked list with the following elements 1 -> 2 -> 3 -> 4 -> 5, return the 2nd to last element. The answer would be element 4.
"""

"""
    Approaches
    One thing that might first come to mind is to use a list to store a representation of the linked list, and then to obtain the nth to last element from this list. While this approach results in an easy-to-read implementation, it could also use up lots of memory maintaining a dual representation of the same data. If the linked list has one million nodes, 
    we’ll need one million pointers in a list to keep track of it! An approach like this results in an extra O(n) space being allocated.

    The code for this approach would look like the following:
"""

def list_nth_last(linked_list, n):
    linked_list_as_list = []
    current_node = linked_list.head_node
    while current_node:
        linked_list_as_list.append(current_node)
        current_node = current_node.get_next_node()
    return linked_list_as_list[len(linked_list_as_list) - n]

"""
    The above code is simple and easy to understand, but it has a space complexity of O(n) because we are storing the linked list in a list. 
    We can do better than this by using two pointers moving in parallel.
    The two-pointer technique is a simple and effective tool for solving linked list problems.
    The idea is to have two pointers, p1 and p2, both starting at the head of the linked list.
    We move p2 forward by n elements, and then move both pointers in parallel until p2 reaches the end of the linked list.
    At this point, p1 will be pointing to the nth last element of the linked list.
    The code for this approach would look like the following:
"""
"""
    nth last pointer = None
    tail pointer = linked list head
    count = 1

    while tail pointer exists
        move tail pointer forward
        increment count

        if count >= n + 1
            if nth last pointer is None
            set nth last pointer to head
            else
            move nth last pointer forward

    return nth last pointer
"""

def nth_last_node(linked_list, n):
    current = None
    tail_seeker = linked_list.head_node
    count = 1
    while tail_seeker:
        tail_seeker = tail_seeker.get_next_node()
        count += 1
        if count >= n + 1:
            if current is None:
                current = linked_list.head_node
            else:
                current = current.get_next_node()
    return current