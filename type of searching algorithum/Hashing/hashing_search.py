class hashtable(object):
    def __init__(self):
        self.length = 100
        self.array = [None]*self.length
    
    def get_hash(self , key):
        sum = 0
        key = str(key)
        for i in key:
            sum+=ord(i)

        return sum % self.length

    def __setitem__(self , key , value):
        h = self.get_hash(key)
        self.array[h] = value

    def __getitem__(self , key):
       h = self.get_hash(key) 
       return self.array[h]

    def __delitem__(self,key):
        h = self.get_hash(key)
        self.array[h] = None 
