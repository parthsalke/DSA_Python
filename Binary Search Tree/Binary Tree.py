class BinarySearchTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if data==self.data:
            return

        #if data less than root,left
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BinarySearchTree(data)
        else:
            # if data greater than root, right
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinarySearchTree(data)

    def inorder(self):
        elements=[]

        #visit left tree
        if self.left:
            elements+=self.left.inorder()

        #visit root node
        elements.append(self.data)

        #visit right tree
        if self.right:
            elements+=self.right.inorder()

        return elements

    def preorder(self):
        elements=[]

        elements.append(self.data)
        if self.left:
            elements+=self.left.preorder()
        if self.right:
            elements+=self.right.preorder()
        return elements

    def postorder(self):
        elements = []

        if self.left:
            elements += self.left.preorder()
        if self.right:
            elements += self.right.preorder()
        elements.append(self.data)
        return elements

    def search(self,val):
        if self.data==val:
            return True
        if val<self.data:
            #left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val>self.data:
            #right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False

    def min(self):
        if self.left is None:
            return self.data
        return self.left.min()

    def max(self):
        if self.right is None:
            return self.data
        return self.right.max()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

def build_tree(elements):
    root=BinarySearchTree(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__=='__main__':
    '''countries=['India','USA','Switzerland','UK','Italy','Canada']
    country_tree=build_tree(countries)
    print(country_tree.search("UK"))
    print(country_tree.search("Sweden"))
    '''

    numbers=[3,54,2,65,13,52,12,9]
    numbers_tree=build_tree(numbers)
    print("Inorder:",numbers_tree.inorder())
    print("Preorder:",numbers_tree.preorder())
    print("Postorder:",numbers_tree.postorder())
    print("Check if number is present:",numbers_tree.search(54))
    print("Minimum number: ",numbers_tree.min())
    print("Maximum number: ",numbers_tree.max())
    print("Sum of numbers: ",numbers_tree.calculate_sum())


