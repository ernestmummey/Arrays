# Swap String for Array Negative Values
# swapStringForArrayNegativeVals(arr)
# Given an array of numbers, replace any negative values with the string 'Dojo'.

def swap_string_for_negative_vals(arr):
    for i in range(len(arr)):
        if(arr[i] < 0):
            print('Dojo')
        else:
            print(arr[i])
    return arr

print(swap_string_for_negative_vals([2,-5,-7, 12, 5, -3]))
print(swap_string_for_negative_vals([-1,1,-1,1,-1,1]))
print(swap_string_for_negative_vals([-0.1, 5, 7, 8, -0.7, 0.8]))