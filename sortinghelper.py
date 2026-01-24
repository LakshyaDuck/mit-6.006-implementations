from heaps import Heap

def find_min(arr, i):
    min = i
    for j in range(i, len(arr)):
        if arr[min] > arr[j]:
            min = j
    return min

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def identify_position(arr, i):
    for j in range(i - 1, -1, -1):
        if arr[j] < arr[i]:
            return j + 1
    return 0
        
def insert_at_from(arr, pos, i):
    temp = arr[i]
    for k in range(i, pos, -1):
        arr[k] = arr[k-1]
    arr[pos] = temp

