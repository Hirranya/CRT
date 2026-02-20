def Linear_Serch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
print(Linear_Serch([1, 2, 3, 4, 5], 3)) # Output: 2
