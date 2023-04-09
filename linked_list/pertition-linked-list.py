"""
    Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
    before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
    to be after the elements less than x (see below). The partition element x can appear anywhere in the
    "right partition"; it does not need to appear between the left and right partitions.
    EXAMPLE
    Input:
    Output:
    3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
    3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
    Hints: #3, #24
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("partition_", type=int, help="the base")
args = parser.parse_args()

print(f" paertition is: {args.partition_}")

from link_list import make_link_list
from print_link_list import print_link_list

default_test = [3,5,8,5,10,2,1]
default_partition = args.partition_



def partition_list(head, partition):
    left = []
    right = [partition]
    pertition_counter = 0
 
    current = head
    while (current is not None):
        if (current.value < partition):
            left.append(current.value)
        elif(current.value == partition):
                pertition_counter += 1
                if (pertition_counter > 1):
                    right.append(current.value)
        else:
            right.append(current.value)
        current = current.next
        
    if left:
        left_head, left_tail = make_link_list(left)
        right_head, right_tail = make_link_list(right)
        left_tail.next = right_head
        return left_head
    else:
        right_head, right_tail = make_link_list(right)
        return right_head


head, tail = make_link_list(default_test)
print_link_list(head)

new_head = partition_list(head,default_partition)
print_link_list(new_head)