# Square Array Values
# squareArrayVals(arr)
# Square each value in a given array, returning that same array with changed values.

def square_array_values(arr):
    squared = []
    for nums in arr:
        squared.append(nums * nums)
    return squared

print(square_array_values([1,2,3,4,5]))