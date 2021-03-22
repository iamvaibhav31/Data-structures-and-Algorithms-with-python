class queue(object):
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def showall(self):
        for i in self.items:
            print(i)

if __name__ == '__main__':
    q = queue()
    q.enqueue(12)
    q.enqueue(13)
    q.enqueue(14)
    print(q.isEmpty())
    print(q.size())
    q.dequeue()
    print("\n")
    print(q.size())
    print("\n")
    q.showall()
