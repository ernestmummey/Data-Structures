class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class singleLinkedList:
    def __init__(self):
        self.head = None


# -----------------------------------------------------------------------
#   Adding a node to the end of the list(appending)
# -----------------------------------------------------------------------
    def append(self, data):
        new_node = Node(data)
        
        if(self.head is None):
            self.head = new_node
            return 

        head = self.head
        while(head.next):
            head = head.next

        head.next = new_node
        return head

# -----------------------------------------------------------------------
#   Adding a node to the end of the list(appending)
# -----------------------------------------------------------------------
    def push(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

# -----------------------------------------------------------------------
#   Adding a node to the end of the list(appending)
# -----------------------------------------------------------------------
    def insert_node(self, data):
        pass

# -----------------------------------------------------------------------
#   Utility function, Printing out the Singly Linked list
# -----------------------------------------------------------------------
    def printList(self):
        print_node = self.head
        while(print_node):
            print(print_node.data)
            print_node = print_node.next


llist = singleLinkedList()

llist.append(5)
llist.append(7)
llist.append(8)
llist.append(9)
llist.append(10)
llist.append(11)
llist.push(2)
llist.push(1)
llist.push(3)

llist.printList()
