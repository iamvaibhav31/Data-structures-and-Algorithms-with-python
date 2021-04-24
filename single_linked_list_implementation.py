class node(object):

    def __init__(self,value):
        self.value = value
        self.nextnode = None

class Linkedlist:
    def __init__(self):
        self.head = None


    def appand(self,data):
        new_node =  node(data)
        if self.head is None:
            self.head = new_node
            return

        cur = self.head
        while (cur.nextnode):
            cur = cur.nextnode
        cur.nextnode = new_node

    def push(self,data):
        new_node = node(data)
        new_node.nextnode = self.head
        self.head = new_node 

    def display(self):
        cur = self.head
        while (cur):
            print(cur.value)
            cur = cur.nextnode
    def reverse(self):
        previous = None
        current = self.head
        while current is not None:
            next = current.nextnode
            current.nextnode = previous
            previous = current
            current = next
        self.head = previous


if "__name__" == "__main__":  
    l = Linkedlist()

    l.appand(1)
    l.appand(2)
    l.appand(3)
    l.appand(4)
    l.appand(5)


    l.display()
    print("\n")
    l.reverse()
    print("\n")
    l.display()


"""
class node(object):

    def __init__(self,value):
        self.value = value
        self.nextnode = None

a = node(1)
b = node(2)
c = node(3)
a.nextnode = b
b.nextnode = c

print(a.value)
print(a.nextnode.value)
print(a.nextnode.nextnode.value)
print(b.nextnode.value)
print(c.nextnode)

"""

"""

Pros

-> link list have a same time to insert and deletion 
in any position , in comparision of array require 
O(n) time to do the same thing 

Cons

-> to access an element in linked list, you need to
take O(k) time to go from the head of the list to the
kth element in contrast array have constan time 
operation to access element in an array

"""
