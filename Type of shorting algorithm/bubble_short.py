def bubble_sort(array):
    for i in range(len(array)-1,0,-1):
        for j in range(i):

            if array[j] > array[j + 1]:
                temp = array[j]
                array[j]  = array[j + 1]
                array[j + 1] = temp

    return array

if __name__ =="__main__":
    arr = [5,6,35,23,25,2,35,25,2,3,5,55]
    print(bubble_sort(arr))