class Node:
    def __init__(self,data):
        self.value = data
        self.next = None



def make_link_list(arr):
    nodes = []
    counter = 1
    for data in (arr):
        nodes.append(Node(data))
        counter += 1
    for index, node in enumerate(nodes):
        if index != 0:
            nodes[index - 1].next = node
    return (nodes[0], nodes[-1])



def make_link_list_2(arr):
    head = None
    tail = None

    for index in range(len(arr)):
        if index == 0:
            head = Node(arr[index])
            tail = head
        else:
            tail.next = Node(arr[index])
            tail = tail.next
    return (head, tail)
            
