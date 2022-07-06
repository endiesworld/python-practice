class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('d')

a.next = b
b.next = c
c.next = d


def print_list(head):
    current = head

    while current is not None:
        print(f'Linked list value is: {current.value}')
        current = current.next
    return None


def print_recus(head):
    if head is None:
        return None
    print(f'Recursive call Linked list value is: {head.value}')
    return print_recus(head.next)


def reverser_linked(head):
    prev = None
    current = head
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev


print_list(a)
print_recus(a)
