class BST:
    def __init__(self,key):
        self.key = key
        self.lnode = None
        self.rnode = None

    def insert(self,data):
        if self.key == None:
            self.key=data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.lnode:
                self.lnode.insert(data)
            else:
                self.lnode = BST(data)
        else:
            if self.rnode:
                self.rnode.insert(data)
            else:
                self.rnode = BST(data)

    def search(self,data):
        if self.key == data:
            print("Node is found")
            return
        if self.key > data:
            if self.lnode:
                self.lnode.search(data)
            else:
                print("Node is not found")
        else:
            if self.rnode:
                self.rnode.search(data)
            else:
                print("Node is not found")

    def preorder(self):
        print(self.key,end=" ")
        if self.lnode:
            self.lnode.preorder()
        if self.rnode:
            self.rnode.preorder()

    def inorder(self):
        if self.lnode:
            self.lnode.inorder()
        print(self.key,end=" ")
        if self.rnode:
            self.rnode.inorder()

    def postorder(self):
        if self.lnode:
            self.lnode.postorder()
        if self.rnode:
            self.rnode.postorder()
        print(self.key,end=" ")

    def min_node(self):
        curr = self
        while curr.lnode:
            curr = curr.lnode
        print(curr.key)

    def max_node(self):
        curr = self
        while curr.rnode:
            curr = curr.rnode
        print(curr.key)


root = BST(10)
lst = [6,5,4,7,8,4,3,9]
for i in lst:
    root.insert(i)
#print("PRE-ORDER")
#root.preorder()

#print("IN-ORDER")
#root.inorder()
#print()
#print("POST-ORDER")
#root.postorder()

root.min_node()
root.max_node()
