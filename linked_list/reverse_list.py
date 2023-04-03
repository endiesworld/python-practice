def reorder_students(L):
    """
    Input: L | linked list with head L.head and size L.size
    Output: None |
    This function should modify list L to reverse its last half.
    Your solution should NOT instantiate:
        - any additional linked list nodes
        - any other non-constant-sized data structures
    a -> b -> c -> d -> e -> f -> g -> h -> i -> j
    """
    # if(L.next == None):
    #     return None
    # current = L
    # next = L.next
    # next.next = current
    # current.next = None
    prev = None
    current = L
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    
    return prev