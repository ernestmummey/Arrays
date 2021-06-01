# Print Ints and Sum 0-255
# printIntsAndSum0To255()
# Print integers from 0 to 255, and with each integer print the sum so far.
sum = 0
for nums in range(256):
    print(nums)
    sum = sum + nums
    print(sum)