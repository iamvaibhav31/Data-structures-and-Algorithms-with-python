class deque(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self,item):
        self.items.append(item)
    
    def addRear(self , item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)

    def __len__(self):
        return len(self.items)

    def showall(self):
        for i in self.items:
            print(i)


if __name__ == '__main__':
    d = deque()
    d.addFront("vaibhav")
    d.addRear("sharma")
    print(len(d))
    d.showall()
    print("\n")
    d.removeFront()
    d.removeRear()
    print(len(d))
    print("\n")
    d.showall()