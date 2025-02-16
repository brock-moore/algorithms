import random

def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quicksort(left) + [pivot] + quicksort(right)

def quicksort_2(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    left = [i for i in arr[1:] if i < pivot]
    right = [i for i in arr[1:] if i >= pivot]
    return quicksort_2(left) + [pivot] + quicksort_2(right)

def quicksort_rand(arr):
    if len(arr) < 2:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    arr[pivot_index] = arr[len(arr) - 1]

    left = [i for i in (arr[0:len(arr) - 1]) if i <= pivot]
    right = [i for i in (arr[0:len(arr) - 1]) if i > pivot]
    
    return quicksort_rand(left) + [pivot] + quicksort_rand(right)

print(quicksort_rand([5,3,4,8,2,9,4,0,1,12]))