"""
collision in hashig is when hash key(created by a hash funtion)is pointing to word the same index is cause a dataover writing in hashtable

we can handal the collision handling by using this two method:-
                          best case               worst case
1. linear chaining           O(1)                      O(n)
2. linear probing            O(1)                      O(1)

"""


# METHOR - 1  (___ linear chaining ___)
class linear_chaining_hashing(object): 
    def __init__(self):
        self.length = 100
        self.array = [[] for i in range(self.length)]
    
    def hash_function(self , key):
        sum = 0
        key = str(key)
        for i in key:
            sum+=ord(i)
        return sum % self.length

    def __setitem__(self , key , value):
        hash_key = self.hash_function(key)
        found = False
        for index , element in enumerate(self.array[hash_key]):
            if len(element) == 2 and element[0] == key:
                self.array[hash_key][index] = (key,value)
                found = True
        if not found:
            self.array[hash_key].append((key,value))

    def __getitem__(self , key):
       
       
       hash_key = self.hash_function(key) 
       
       for ele in self.array[hash_key]:
           if  ele[0] == key:
               return ele[1]
       

    def __delitem__(self,key):
        
        hash_key = self.hash_function(key)
        for index , element in enumerate(self.array[hash_key]):
            if element[0] == key:
                del self.array[hash_key][index]



# METHORD - 2 (___ linear probing ___)
class linear_probing_hashing(object): 
    
    def __init__(self):
        self.length = 100
        self.array = [None]*self.length 

    def hash_function(self , key):
        sum = 0
        key = str(key)
        for i in key:
            sum+=ord(i)
        return sum % self.length

    def __setitem__(self , key , value):
        hash_key = self.hash_function(key)
        found = False
        while  not found:
            if self.array[hash_key] is not None:
                if self.array[hash_key][0] == key:
                    self.array[hash_key] = (key,value)
                    found = True
                hash_key += 1
            else:
                self.array[hash_key] = (key,value)
                found = True
            
    def __getitem__(self , key):
       hash_key = self.hash_function(key) 
       found = False
       while  not found:
            if self.array[hash_key] is not None:
                if self.array[hash_key][0] == key:
                    found = True
                    return self.array[hash_key][1]
                hash_key += 1
            
    def __delitem__(self,key):
        hash_key = self.hash_function(key) 
        found = False
        while  not found:
            if self.array[hash_key] is not None:
                if self.array[hash_key][0] == key:
                    found = True
                    self.array[hash_key] = None
                hash_key += 1
            
            
                
if __name__ == "__main__":

    h = linear_chaining_hashing()
    f = linear_probing_hashing()
    
    f["abcde"] =131
    f["987zi"] = 544564
    f[1212312] =123124124
    f["vaibhav"] = 21
    f["qfiafhiaha"] = "sdfef"
    f["abcde"] = 1324
    print(f["987zi"])
    del f["vaibhav"]
    h[1212312] =123124124
    h["vaibhav"] = 21
    h["qfiafhiaha"] = "sdfef"
    h["abcde"] =131
    h["987zi"] = 544564

    
    print(h.array)
    print(f.array)
