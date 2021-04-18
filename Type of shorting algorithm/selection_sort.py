def selection_sort(array):
    
    for fillslot in range(len(array)-1,0,-1):
        
        position_of_max = 0
        
        for location in range(1,fillslot+1):
            if array[location] > array[position_of_max]:
                position_of_max = location

        array[fillslot] , array[position_of_max] = array[position_of_max] , array[fillslot]

    


arr = [1,3,9,45,34,21,5,6,85,47]
selection_sort(arr)        
print(arr)