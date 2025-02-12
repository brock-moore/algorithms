def recursive_sum(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + recursive_sum(arr[1:])
    
print(recursive_sum([1,3,5,7,9]))

def recursive_numItems(arr):
    if arr == []:
        return 0
    else:
        return 1 + recursive_numItems(arr[1:])
    
print(recursive_numItems(['a',1,5,'hello',-1]))
print(recursive_numItems([7]))

def recursive_max(arr):
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return arr[0]
    else:
        next_max = recursive_max(arr[1:])
        if next_max > arr[0]:
            return next_max
        return arr[0]
    
print(recursive_max([-5,1,3,2,6,4,-8,12,6]))