"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ptr = l1
        l1_store = []
        while(ptr):
            l1_store.append(ptr.val)
            ptr = ptr.next
        
        ptr_2 = l2
        l2_store = []
        while(ptr_2):
            l2_store.append(ptr_2.val)
            ptr_2 = ptr_2.next

        # print(l1_store, l2_store )

        l1_len = len(l1_store)
        l2_len = len(l2_store)

        if l1_len > l2_len:
            space = l1_len - l2_len
            for _ in range(space):
                l2_store.append(0)
                l2_len += 1
            
        if l1_len < l2_len:
            space = l2_len - l1_len
            for _ in range(space):
                l1_store.append(0)
                l1_len += 1
        
        nodes = []
        rem = 0

        for i in range(l2_len):
            sum = l1_store[i] + l2_store[i] + rem
            if sum > 9:
                rem = sum // 10 
                sum -= 10
            else:
                rem = 0
            
            nodes.append(ListNode(sum))
        if rem > 0:
            nodes.append(ListNode(rem))
        
        prev_node = nodes[0]
        head = nodes[0]
        for node in nodes[1:]:
            prev_node.next = node
            prev_node = node


        return head