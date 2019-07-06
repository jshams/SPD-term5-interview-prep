'''
Write a function to insert a node at the front of a Singly Linked-List

Examples:
LinkedList: 1->2 , Head = 1

insert_at_front(1) ==> 1->1->2

insert_at_front(2) ==> 2->1->2

insert_at_front(3) ==> 3->1->2
'''

class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None
        
    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head
    
    def reverse(self):
        prev_node = None
        node = self.head
        next_node = node.next if node is not None else None
        if node is not None:
            while node.next is not None:
                node.next = prev_node
                prev_node = node
                node = next_node
                next_node = node.next
            node.next = prev_node
            self.head = node