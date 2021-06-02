# Print Average of Array
# printAverageOfArray(arr)
# Analyze an array’s values and print the average.

def print_average_of_array(arr):
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i]

    average = sum / len(arr)
    return average

print(print_average_of_array([1,3,4,6,7,8]))
print(print_average_of_array([-1,3,25,70,1]))
print(print_average_of_array([-3, -2, -7, -10]))
print(print_average_of_array([50, 1.2, 60, 4.4, 5.6]))