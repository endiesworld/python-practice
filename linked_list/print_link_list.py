def print_link_list(head):
    current = head
    link_list = str(current.value)
    current = current.next
    while (current is not None):
        link_list += " -> " + str(current.value)
        current = current.next
    print(link_list)
    
    