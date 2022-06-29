from calendar import c


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


data = [-10, -3, 0, 5, 9]


def processing(root):
    stack = [root]

    while (len(stack) > 0):
        current = stack.pop()  # pop the node at the top of the stack out
        print(current.value)
        # current.left points to the left node
        #  .value refers to the value in the node
        # current.right points to the left node
        #  .value refers to the value in the node
        # Adds the right node to stack
        if (current.right):
            stack.append(current.right)

        if (current.left):
            stack.append(current.left)
    return None


def bst_ops(arr):
    mid = len(arr) // 2
    root = Node(arr[mid])
    left_side = arr[:mid]
    right_side = arr[mid+1:]
    counter = -1
    while counter < mid:
        pass


root = Node(0)
node_L_1 = Node(-3)
node_L_2 = Node(-10)
node_R_1 = Node(9)
node_R_2 = Node(5)

root.left = node_L_1
root.right = node_R_1
node_L_1.left = node_L_2
node_R_1.left = node_R_2

processing(root)
