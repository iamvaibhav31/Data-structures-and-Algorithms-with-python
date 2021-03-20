class stack(object):
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def push(self,items):
        self.items.append(items)
    
    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]
    
    def Size(self):
        return len(self.items)

    def showall(self):
        for i in self.items:
            print(i)
    
    def total(self):
       
        if self.isEmpty() == True:
            return 0
        else:
            current_sum = self.items[0]
            max_sum  = self.items[0]
            
            for num in self.items[1:]:
                current_sum = max(current_sum + num , num)
                max_sum = max(current_sum , max_sum)
            
            return max_sum 



if __name__ == '__main__':
    s = stack()

    s.push(12)
    s.push(13)
    s.push(14)
    s.push(15)
    print(s.peek())
    print(s.isEmpty())
    print(s.Size())
    s.pop()
    print(s.peek())
    print(s.isEmpty())
    print(s.Size())
    s.showall()
    print(s.total())