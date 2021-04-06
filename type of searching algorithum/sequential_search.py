def unordered_list_seq_search(ele,arr):
    
    pos = 0
    found = False

    while pos<len(arr) and not found:
        if arr[pos] == ele:
            found = True
        else:
            pos+=1
    
    return found 

def ordered_list_seq_search(ele,arr):
    Pos = 0
    found = False
    stopped = False

    while Pos<len(arr) and not found and not stopped:

        if arr[Pos] == ele:
            found = True
        else:

            if arr[Pos] > ele :
                stopped = True
            else:
                Pos+=1

    return found



if __name__ == "__main__":
    print(unordered_list_seq_search(6,[1,2,3,8,7,6,5,4,10]))
    print(ordered_list_seq_search(6,[1,2,3,4,5,6,7,8,9,10]))
