# Print Max, Min, Average Array Values
# printMaxMinAverageArrayVals(arr)
# Given an array, print the max, min and average values for that array.

def max_min_average(arr):
    max = arr[0]
    min = arr[0]
    sum = 0

    for i in range(len(arr)):
        if(arr[i] > max):
            max = arr[i]
        if(arr[i] < min):
            min = arr[i]
        sum = sum + arr[i]

    avg = sum / len(arr)
    return [max, min, avg]

print(max_min_average([1,3,2,6,5,7]))
print(max_min_average([-1,3,25,70,1]))
print(max_min_average([-3, -2, -7, -10]))
print(max_min_average([50, 1.2, 60, 4.4, 5.6]))

