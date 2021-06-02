# Return Array Count Greater than Y
# returnArrayCountGreaterThanY(arr, y)
# Given an array and a value Y, count and print the number of array values greater than Y.

def array_greater_than_y(arr, y):
    count = 0
    for i in range(len(arr)):
        if(arr[i] > y):
            count = count + 1
            print(f"This is the number of array value greater than y:  {count}")
    return count

print(array_greater_than_y([1,3,5,6,9], 2))
print(array_greater_than_y([-1,-4,-7,-20], -3))
print(array_greater_than_y([0.2, 0.3, 0.7, 1.1], 0.4))
print(array_greater_than_y([-1, 5.2, 7, 0, 12], 2))
