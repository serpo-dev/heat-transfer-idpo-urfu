import sys

def search(arr, val, low, high):
    left = arr[0]
    right = arr[len(arr) - 1]
    if (val < left) or (val > right):
        raise ValueError("The input value is out of interpolation limits.")

    mid = (low + high) // 2
    if (arr[mid] == val): 
            return mid, True
    if (high > low):
        if (arr[mid] < val): 
            return search(arr, val, mid + 1, high)
        else:
            return search(arr, val, low, mid)
    else: 
        return mid, False if (low == high) else IndexError('The error happened in a binary search in "low == high" condition.')
    
sys.modules[__name__] = search