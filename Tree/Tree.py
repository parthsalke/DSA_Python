#Tree (Hierarchy)
class Tree:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def add_child(self,child):
        child.parent=self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces= " " * self.get_level() * 5
        prefix= spaces + "|____" if self.parent else""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_tree():
    root=Tree("Electronics")

    laptop=Tree("Laptop")
    laptop.add_child(Tree("Mac"))
    laptop.add_child(Tree("HP"))
    laptop.add_child(Tree("Microsoft"))

    phones=Tree("Phones")
    phones.add_child(Tree("iPhone"))
    phones.add_child(Tree("Pixel"))
    phones.add_child(Tree("OnePlus"))

    tv=Tree("TV")
    tv.add_child(Tree("LG"))
    tv.add_child(Tree("Sony"))

    root.add_child(laptop)
    root.add_child(phones)
    root.add_child(tv)

    root.print_tree()

if __name__=="__main__":
    build_tree()