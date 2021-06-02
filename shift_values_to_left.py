# Shift Array Values Left
# shiftArrayValsLeft(arr)
# Given an array, move all values forward (to the left) by one index, dropping the first value and leaving a 0 (zero) value at the end of the array.

def shift_array_vals_left(arr):
    temp = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[len(arr)-1] = 0
    return arr

print(shift_array_vals_left([1,2,3,4,5]))
print(shift_array_vals_left([2,3,4,5,0]))
print(shift_array_vals_left([3,4,5,0,0]))
