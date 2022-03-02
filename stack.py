class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self): 
        self.head = None

    
    def isempty(self): 
        if self.head == None: 
            return True
        else: 
            return False
    

    def push(self,data): 
          
        if self.head == None: 
            self.head=Node(data) 
              
        else: 
            newnode = Node(data) 
            newnode.next = self.head 
            self.head = newnode 

    def pop(self): 

        poppednode = self.head 
        self.head = self.head.next
        poppednode.next = None
        return poppednode.data 

    def peek(self): 

        if self.isempty():
            return None
        else:  
            return self.head.data 

    def display(self):

        iternode = self.head
        if self.isempty():
            print("Pino on tyhjä. Ei tulostettavaa.")
        else:
            while(iternode != None):
                print(iternode.data)
                iternode = iternode.next
            return

pino = Stack()
pino.push(1)
pino.push(2)
pino.push(3)
pino.push(4)

print()
pino.display()
print("Päälimmäinen alkio: ", pino.peek())
pino.pop()
print()
pino.display()
print("Päälimmäinen alkio: ", pino.peek())
pino.pop()
print()
pino.display()
print("Päälimmäinen alkio: ", pino.peek())
pino.pop()
print()
pino.display()
print("Päälimmäinen alkio: ", pino.peek())
pino.pop()
print()
pino.display()
print("Päälimmäinen alkio: ", pino.peek())
