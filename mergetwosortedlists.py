'''
Problem:
    Merge two sorted linked lists and return it as a new list.
    The new list should be made by splicing together the nodes of the first two lists.

Example:
    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4

Restatement:
    Given two linked lists in sorted order, return a new linked list that is in sorted 
    containing the contents of both lists passed in. If there are duplicates, add them twice.

Clarifying Questions:
    How will the linked lists be given?
        - Will I be given the head?
        - The whole list with an attribute head
        - Is the linked list iterable?
    
Assumptions:
    I will assume both lists are sorted
    I will assume all items of the lists are comparable with each other

Think out loud:
    Possible solutions:
        1. I could merge both and then sort them
        2. I could put all them into an array, sort them, them create a linked list in that order
        3. I can iterate over both linked lists simultaneously and add to the new linked list
            depending on which values are lower
    
Rationale/tradeoffs:
    I'll chose number 3 because it only takes O(n) time and O(n) memory where the others require
    sorting which takes O(log(n)) time alone. 
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        node1 = l1
        node2 = l2
        curr_node = None
        if l1 is None or l2 is None:
            if l1 is None:
                return l2
            else:
                return l1
        if l1.val > l2.val:
            curr_node = ListNode(node2.val)
            head = curr_node
            node2 = node2.next
        else:
            curr_node = ListNode(node1.val)
            head = curr_node
            node1 = node1.next
        while node1 is not None or node2 is not None:
            if node1 is not None and node2 is not None:
                if node1.val < node2.val:
                    curr_node.next = ListNode(node1.val)
                    curr_node = curr_node.next
                    node1 = node1.next
                else:
                    curr_node.next = ListNode(node2.val)
                    curr_node = curr_node.next
                    node2 = node2.next
            elif node1 is not None:
                curr_node.next = ListNode(node1.val)
                curr_node = curr_node.next
                node1 = node1.next
            elif node2 is not None:
                curr_node.next = ListNode(node2.val)
                curr_node = curr_node.next
                node2 = node2.next
        return head
        
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        