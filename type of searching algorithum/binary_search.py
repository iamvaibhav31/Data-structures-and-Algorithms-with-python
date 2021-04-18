def binary_search_using_loop(ele , arr):
    first = 0
    last = len(arr) - 1

    found = False

    while  first <= last and not found:
        
        mid = (first + last)//2

        if arr[mid] == ele:
            found = True
        else:
            if ele < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    
    return found

def binary_search_using_recurtion(ele,arr):
    
    if  len(arr) == 0:
        return False
    else:
        mid = len(arr)//2

        if arr[mid] == ele:
            return True
        else:
            if ele < arr[mid]:
                binary_search_using_recurtion(ele,arr[:mid])
            else:
                binary_search_using_recurtion(ele,arr[mid+1:])