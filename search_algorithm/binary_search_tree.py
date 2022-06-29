from calendar import c


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


data = [-10, -3, 0, 5, 9]


def processing(root):
    stack = [root]
    print(stack)

    while (len(stack) > 0):
        current = stack.pop()
        if(current.left):
            print(current.left)
            stack.append(current.left)
        if(current.right):
            print(current.right)
            stack.append(current.right)


root = Node(0)
node_L_1 = Node(-3)
node_L_2 = Node(-10)
node_R_1 = Node(9)
node_R_2 = Node(5)

root.left = node_L_1
root.right = node_R_1
node_L_1.right = node_L_2
node_R_1.right = node_R_2

processing(root)
