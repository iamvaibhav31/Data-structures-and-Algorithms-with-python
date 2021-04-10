
"""
collision in hashig is when hash key(created by a hash funtion) is pointing to word the same index in which the data is alredy present is cause a dataover  writing in hashtable

we can handal the collision handling by using this two method:-
                    best case               worst case
1. chaining           O(1)                      O(n)
2. leaniar probing    O(1)                      O(1)

"""

# METHOR - 1 ( Chaining )
class hashtable(object):
    def __init__(self): # CREATIING A HASH TABLE
        self.length = 100
        self.array = [[] for i in range(self.length)]
    
    def hash_function(self , key): # HASH FUNCTION
        
        sum = 0
        key = str(key)
        
        for i in key:
            sum+=ord(i)
        
        return sum % self.length  # RETURNING A HASH KEY

    
    
    def __setitem__(self , key , value):
        
        """ 
        
        ADDING THE KEY VALUE PAIR IN A HASH TABLE USING HASH KEY
        
        """
        
        hash_fun_value = self.hash_function(key) # HASH KEY
        found = False
        
        for index , element in enumerate(self.array[hash_fun_value]):
            if len(element) == 2 and element[0] == key:
                self.array[hash_fun_value][index] = (key,value)
                found = True

        if not found:
            self.array[hash_fun_value].append((key,value))

    
    
    def __getitem__(self , key):
        
        """
        
        GETTING THE VALUE USING THE KEY
        
        """
       
       hash_fun_value = self.hash_function(key)  # HASH KEY
       
       for ele in self.array[hash_fun_value]:
           if  ele[0] == key:
               return ele[1]
       

    def __delitem__(self,key):
        """
        
        DELETING THE ITEM IN THE HASH TABLE
        
        """
        hash_fun_value = self.hash_function(key) # HASH KEY
        for index , element in enumerate(self.array[hash_fun_value]):
            if element[0] == key:
                del self.array[hash_fun_value][index]
    
  
    

if __name__ == "__main__":

    h = hashtable()

    h[1212312] =123124124
    h["vaibhav"] = 21
    h["qfiafhiaha"] = "sdfef"
    h["march 6"] =131
    h["march 17"] = 544564
    print(h.hash_function("march 6"))
    print(h.hash_function("march 17"))
    print(h.hash_function("qfiafhiaha"))
    print(h.hash_function("vaibhav"))
    print(h[1212312])
    print(h.array)
