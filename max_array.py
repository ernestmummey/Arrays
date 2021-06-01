# Print Max of Array
# printMaxOfArray(arr)
# Given an array, find and print its largest element.
def printMaxOfArray(arr):
    max = arr[0];
    for i in range(len(arr)):
        if(arr[i] > max):
            max = arr[i];
    return max

############################################################
# Test cases
############################################################

# print(printMaxOfArray([1,3,5,9,2]))
# print(printMaxOfArray([20,30,2,5,15]))
# print(printMaxOfArray([100,4,600,7,-1]))
# print(printMaxOfArray([-2,-3,-10,-1]))
# print(printMaxOfArray([-1, 5, -3, 50, 1]))
