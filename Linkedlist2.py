class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class linkedlist:
    def __init__(self):
        self.head=None

    def insert_start(self,node):
        node.next=self.head
        self.head=node

    def insert_end(self,node):
        if self.head is None:
            self.head=node
            return
        current_node=self.head
        while(current_node.next):
            current_node=current_node.next
        current_node.next=node

    def deleteNode(self, key):
        temp = self.head
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
            while (temp is not None):
                if temp.data == key:
                    break
                prev = temp
                temp = temp.next
            if (temp == None):
                return
            prev.next = temp.next
            temp = None

    def get_length(self):
        c=0
        temp=self.head
        while temp:
            c=c+1
            temp=temp.next
        return c

    def show(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr=self.head
        llstr=' '
        while itr:
            llstr += str(itr.data)+'-->'
            itr=itr.next
        print(llstr)

ll=linkedlist()
ll.insert_start(Node("B"))
ll.insert_start(Node("A"))
ll.show()
ll.insert_end(Node("C"))
ll.insert_end(Node("D"))
print("Length:",ll.get_length())
ll.show()
ll.deleteNode("C")
ll.show()
