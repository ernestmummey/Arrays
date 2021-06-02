# Zero Out Array Negative Numbers
# zeroOutArrayNegativeVals(arr)
# Return the given array, after setting any negative values to zero.

def zero_out_neg_arr_vals(arr):
    for i in range(len(arr)):
        if(arr[i] < 0):
            arr[i] = 0
    return arr

print(zero_out_neg_arr_vals([-1,9,-3,-4,6]))
print(zero_out_neg_arr_vals([-0.1, 53, -53, 0.4]))
print(zero_out_neg_arr_vals([-1,1,-1,1,-1]))