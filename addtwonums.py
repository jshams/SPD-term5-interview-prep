# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

'''
Restate the question:
    Given two linked lists with digits as the values of the nodes in reverse order, 
    return the sum of the two linked lists in the same reversed order format. 
    The format of the linked list is reversed so 1 -> 2 -> 3 represents 321. 
    An example input is 1 -> 2 -> 3 , 3 - > 4 -> 5. 
    This is also 321 + 543 = 864 so you would return 4 -> 6 -> 8. 
    There can also be no trailing zeroes except for when the number is 0 and there is one.

Clarifying questions:
    Can any of the numbers be negative?
    How is the linked list given?
        - Am I given an ll object?
        - Am I given just the head?
    How should I return the new ll?
        - Should I return the head
        - Should I return the whole ll object?

Assumptions:
    Numbers cannot be negative
    input is always a linked list of numbers

Think out loud:
    To do this we have to first translate these linked list representations into numbers, 
    add them up, then put them back into this linked list format, and return that. 
    This approach is great, but we need to translate the linked list to an int, then translate it back. 
    What if instead we could skip this step and use the adding process we learned in 2nd grade. 
    This is adding the numbers by their placement from back to front 
    (exactly how they're given to us) and if the sum is above 10 add 1 to the next place.
'''

class Solution(object):
    def addTwoNumbers(self, node1, node2):
        head = None
        remainder = value = 0
        curr_node = None
        # iterate over both linked lists while at least one has more nodes
        while node1 is not None or node2 is not None:
            # check if both linked lists have more nodes
            if node1 is not None and node2 is not None:
                # if so add the two values and if there is a remainder add it too
                remainder, value = divmod(node1.val + node2.val + remainder, 10)
                # move to the next nodes
                node1 = node1.next
                node2 = node2.next
            # otherwise check if only the first linked list has more nodes
            elif node1 is not None:
                # if so add the value and the remainder if there is one
                remainder, value = divmod(node1.val + remainder, 10)
                # move to the next node
                node1 = node1.next
            # otherwise check if only the second linked list has more nodes
            elif node2 is not None:
                # if so add the value and the remainder if there is one
                remainder, value = divmod(node2.val + remainder, 10)
                # move to the next node
                node2 = node2.next
            # check if the head is none (first iteration)
            if head is None:
                # if so create a list node of the head because we need to return the head
                head = ListNode(value)
                # and set the current noe to equal the head
                curr_node = head
            else:
                # otherwise (any iteration after the first)
                # create a new node with our value and have curr node point to it
                curr_node.next = ListNode(value)
                # move currnode to its next (the node we just created)
                curr_node = curr_node.next
        # check if there is still a remainder
        if remainder == 1:
            # if so create a new node of the remainder which will always be 1
            curr_node.next = ListNode(remainder)
        # return the head
        return head

        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

