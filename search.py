from time import perf_counter_ns

def bninary_search_loop(arr, target, steps=0):
    low = 0
    high = len(arr) - 1
    mid = (low + high) // 2
    while high >= low:
        steps += 1
        if arr[mid] == target:
            return mid, steps
        elif arr[mid] > target:
            high = mid - 1
            mid = (low + high) // 2
        else:
            low = mid + 1
            mid = (low + high) // 2
    return None, steps

def linear_search(arr, target, steps=0):
    for i in range(len(arr)):
        steps += 1
        if arr[i] == target:
            return i, steps
    return None, steps

def bninary_search_recursion(arr, target, steps=0, low=None, high=None):
    if low == None or high == None:
        low = 0
        high = len(arr) - 1
    if low > high:
        return None, steps
    mid = (low + high) // 2
    steps += 1
    if arr[mid] == target:
        return mid, steps
    elif arr[mid] > target:
        return bninary_search_recursion(arr, target, steps, low=low, high=mid-1)
    else:
        return bninary_search_recursion(arr, target, steps=steps, low=mid+1, high=high)

def main():
    array = []
    size = int(input("Size of sorted array: "))
    for i in range(size):
        array.append(i)
    target = int(input(f"Number to be found from 0 to {size - 1}: "))

    t0 = perf_counter_ns()
    bsl = bninary_search_loop(array, target)
    t1 = perf_counter_ns()
    t2 = perf_counter_ns()
    ls = linear_search(array, target)
    t3 = perf_counter_ns()
    t4 = perf_counter_ns()
    bsr = bninary_search_recursion(array, target)
    t5 = perf_counter_ns()
    print("Readings")
    print("Algorithm used: (output, steps taken), time taken in ns")
    print(f"Binaray search using loop: {bsl}, {t1-t0}")
    print(f"Linear Search: {ls}, {t3-t2}")
    print(f"Binary search using recursion: {bsr}, {t5-t4}")

main()
