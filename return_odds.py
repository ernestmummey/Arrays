# Return Odds Array 1-255
# returnOddsArray1To255()
# Create an array with all the odd integers between 1 and 255 (inclusive).
def returnOddsArray1To255():
    for nums in range(1, 256):
        if(nums % 2 == 1):
            print(nums)
    return nums

print(returnOddsArray1To255())
