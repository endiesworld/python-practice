"""
25. Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
"""



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reverse_engine(self, list_):
        
        return list_[::-1]

    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        
        temp_node_store = []
        new_head = None
        ptr = head
        counter = 0 
        current_node = None

        while ptr != None:
            temp_node_store.append(ptr.val)
            counter += 1
            
            if counter == k:
                temp_node_store = self.reverse_engine(temp_node_store)

                if new_head == None:
                    new_head = ListNode(temp_node_store[0])
                    current_node = new_head
                    temp_node_store = temp_node_store[1:]

                for data in temp_node_store:
                    node = ListNode(data)
                    current_node.next = node
                    current_node = node

                counter = 0
                temp_node_store = [] 

            ptr = ptr.next
        
        for data in temp_node_store:
            node = ListNode(data)
            current_node.next = node
            current_node = node

        
        return new_head