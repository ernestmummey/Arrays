# Print Array Values
# printArrayVals(arr)
# Iterate through a given array, printing each value.

def print_array_vals(arr):
    for i in range(len(arr)):
        print(arr[i])
    return arr

print(print_array_vals([1,2,3,4,5]))