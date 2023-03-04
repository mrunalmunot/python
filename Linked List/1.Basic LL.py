class Node:
    # Creating a Node
    def __init__(self, item :int) -> None:
        self.item = item
        self.next = None
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
if __name__ == '__main__':
    ll = LinkedList()
    
    ll.head = Node(item = 1)
    second = Node(item = 2)
    third = Node(item = 3)
    
    # Connecting Nodes
    ll.head.next = second
    second.next = third

    # Printing elements of Linked List
    while ll.head != None:
        print(ll.head.item, end=' -> ')
        ll.head = ll.head.next
    print(None)