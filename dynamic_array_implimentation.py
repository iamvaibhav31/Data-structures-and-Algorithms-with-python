import ctypes

class DynamicArray():

    def __init__(self):
        self.n = 0  # default index where the element wass insert 
        self.capacity = 1 # capacity of store the element
        self.A = self.make_array(self.capacity) 

    def __len__(self):
        return self.n

    """  They are implemented by __getitem__() and __setitem__() methods. But, these methods are used only in indexed attributes like 
    arrays dictionaries, lists e.t.c. """
    
    def __getitem__(self,k):

        if not 0<= k < self.n:
            return IndexError("_!_K IS OUT OF BOUND_!_")

        return self.A[k]

    def append(self,ele): # This function is To add the element in array
        
        if self.n == self.capacity:
            self._resize(2*self.capacity)

        self.A[self.n]=ele
        self.n +=1
# this symbol was ( _ ) denote that this 'resize' is a private function
    def _resize(self,new_cap):  # This fuction is To resize the array automatically when index of element and capacity is equal 
        B = self.make_array(new_cap)

        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_cap

    def make_array(self , new_cap):
        return (new_cap*ctypes.py_object)()


if __name__ == "__main__":

    arr = DynamicArray()

    arr.append(21)
    print(len(arr))
    arr.append(31)
    print(len(arr))
    print(arr[0])
    print(arr[1])
    print(arr[2])
