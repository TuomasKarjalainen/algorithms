class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None


class DoublyLinkedList:
    def __init__(self):
        self.start_node = None
    
    def addNode_in_emptylist(self, data):
        if self.start_node is None:
            newNode = Node(data)
            self.start_node =newNode
        else:
            print("The list is empty")

    def addNode_at_start(self, data):
        if self.start_node is None:
            newNode = Node(data)
            self.start_node = newNode
            print("Node inserted")
            return
        newNode = Node(data)
        newNode.nref = self.start_node
        self.start_node.pref = newNode
        self.start_node = newNode


    def print_traverse_list(self):
        if self.start_node is None:
            print("The list has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item , " ")
                n = n.nref


    def deleteNode_at_start(self):
        if self.start_node is None:
            print("The list has no element delete")
            return
        if self.start_node.nref is None:
            self.start_node = None
            return
        self.start_node = self.start_node.nref
        self.start_prev = None

    def deleteNode_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            self.start_node = None
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        n.pref.nref = None


DLL = DoublyLinkedList()
DLL.addNode_in_emptylist(1)
DLL.addNode_at_start(2)
DLL.addNode_at_start(4)
DLL.addNode_at_start(8)
DLL.print_traverse_list()