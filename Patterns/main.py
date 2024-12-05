class BST:
    def __init__(self,key):
        self.key = key
        self.lnode = None
        self.rnode = None
    def insert(self,data):
        if self.key == None:
            self.key = data
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
            print("Data Found")
            return
        if data < self.key:
            if self.lnode:
                self.lnode.search(data)
            else:
                print("Data doesnot exist..")
        else:
            if self.rnode:
                self.rnode.search(data)
            else:
                print("Data doesnot exist")

    def preorder(self):
        print(self.key,end=" -> ")
        if self.lnode:
            self.lnode.preorder()
        if self.rnode:
            self.rnode.preorder()

    def inorder(self):
        if self.lnode:
            self.lnode.inorder()
        print(self.key,end=" -> ")
        if self.rnode:
            self.rnode.inorder()

    def postorder(self):
        if self.lnode:
            self.lnode.postorder()
        if self.rnode:
            self.rnode.postorder()
        print(self.key,end=" -> ")


root = BST(20)
list = [2,5,18,4,12]
for i in list:
    root.insert(i)
print("Pre-Order")
root.preorder()
print()
print("In-Order")
root.inorder()
print()
print("Post-Order")
root.postorder()
