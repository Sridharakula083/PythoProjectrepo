class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class Linkedlist:
    def __init__(self):
        self.head=None
    def traversal(self):
        if self.head == None:
            print("Linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.ref

    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head==None:
            new_node=self.head
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref = new_node

    def after_node(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print("Node is not present")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref=new_node

    def insert_empty(self,data):
        if self.head != None:
            print("Linked list is not empty")
        else:
            new_node=Node(data)
            self.head=new_node

    def delete_begin(self):
        if self.head == None:
            print("NO item to delete")
        else:
            self.head=self.head.ref

    def delete_end(self):
        if self.head==None:
            print("No iteams to delete at the end")
        elif self.head.ref == None:
            self.head=None
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None

    def delete_middle(self,x):
        if self.head == None:
            print("List is empty")
        elif x == self.head.data:
            self.head=self.head.ref
        else:
            n=self.head
            while n.ref is not None:
                if x==n.ref.data:
                    break
                n=n.ref
            if n.ref is None:
                print("node is not present")
            else:
                n.ref = n.ref.ref

LL1=Linkedlist()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(150)
LL1.add_begin(100)
LL1.delete_middle(20)
LL1.traversal()
