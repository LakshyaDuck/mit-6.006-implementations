from time import perf_counter_ns
from random import shuffle
from sortinghelper import *

def selection_sort(arr):
    leng = len(arr)
    for i in range(leng - 1):
        min = find_min(arr, i)
        swap(arr, i, min)

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    
    pivot = arr[0]
    less = [i for i in arr[1:] if i < pivot]
    greater = [i for i in arr[1:] if pivot < i]
    return quick_sort(less) + [pivot] + quick_sort(greater)

def merge_sort(arr):
    pass

def insertion_sort(arr):
    for i in range(1, len(arr)):
        pos = identify_position(arr, i)
        if pos != i:
            insert_at_from(arr, pos, i)

def counting_sort(arr):
    pass

def bst_sort(arr):
    pass

def radix_sort(arr):
    pass

def heap_sort(arr):
    pass

def avl_sort(arr):
    pass

def main():
    size = int(input("Size of an array: "))
    print("1: Random\n2: Already sorted\n3: Reversed array")
    array_condition = input("Array Condition: ")
    algorithm = input("First letter of algorithm or all: ")
    
    arr = list(range(size))
    
    if array_condition == "1":
        shuffle(arr)
    elif array_condition == "3":
        arr.reverse()
    elif array_condition not in ["1", "2", "3"]:
        print("Wrong input")
        exit(1)

    output = input("Output 'p' for only performance and 'a' for sorted array with performance: ")

    if algorithm == "all" or algorithm == "s":
        array = arr.copy()
        t0 = perf_counter_ns()
        selection_sort(array)
        t1 = perf_counter_ns()
        time_taken = t1-t0
        if output == "a":
            print(array)
        print("selection sort:" + str(time_taken))
    if algorithm == "all" or algorithm == "a":
        array = arr.copy()
        t0 = perf_counter_ns()
        avl_sort(array)
        t1 = perf_counter_ns()
        time_taken = t1-t0
        if output == "a":
            print(array)
        print("avl sort:" + str(time_taken))
    if algorithm == "all" or algorithm == "i":
        array = arr.copy()
        t0 = perf_counter_ns()
        insertion_sort(array)
        t1 = perf_counter_ns()
        time_taken = t1-t0
        if output == "a":
            print(array)
        print("insertion sort:" + str(time_taken))
    if algorithm == "all" or algorithm == "h":
        array = arr.copy()
        t0 = perf_counter_ns()
        heap_sort(array)
        t1 = perf_counter_ns()
        time_taken = t1-t0
        if output == "a":
            print(array)
        print("heap sort:" + str(time_taken))
    if algorithm == "all" or algorithm == "q":
        array = arr.copy()
        t0 = perf_counter_ns()
        array = quick_sort(array)
        t1 = perf_counter_ns()
        time_taken = t1-t0
        if output == "a":
            print(array)
        print("quick sort:" + str(time_taken))
    if algorithm == "all" or algorithm == "m":
        array = arr.copy()
        t0 = perf_counter_ns()
        merge_sort(array)
        t1 = perf_counter_ns()
        time_taken = t1-t0
        if output == "a":
            print(array)
        print("merge sort:" + str(time_taken))
    if algorithm == "all" or algorithm == "c":
        array = arr.copy()
        t0 = perf_counter_ns()
        counting_sort(array)
        t1 = perf_counter_ns()
        time_taken = t1-t0
        if output == "a":
            print(array)
        print("counting sort:" + str(time_taken))
    if algorithm == "all" or algorithm == "r":
        array = arr.copy()
        t0 = perf_counter_ns()
        radix_sort(array)
        t1 = perf_counter_ns()
        time_taken = t1-t0
        if output == "a":
            print(array)
        print("radix sort:" + str(time_taken))
    if algorithm == "all" or algorithm == "b":
        array = arr.copy()
        t0 = perf_counter_ns()
        bst_sort(array)
        t1 = perf_counter_ns()
        time_taken = t1-t0
        if output == "a":
            print(array)
        print("bst sort:" + str(time_taken))
        

main()