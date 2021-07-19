# This week’s question:
# Given an unsorted array of integers and a number n, find the number of continuous subarrays having sum exactly equal n. Return -1 if none exist.
#
# Example:
# $ subarraySum([10, 2, -2, -20, 10], -10)
# 3 //arr[-...3], arr[1...4], arr[3...4]

def subarraySum(array, match):
    counter = 0
    for i in range(0,len(array) - 1):
        x  = array[i]
        if x == match:
            counter += 1
            continue
        for e in range(1, len(array) - i):
            x = x + array[i + e]
            if x == match:
                counter += 1
                break
    if counter == 0:
        print(-1)
    else:
        print(counter)

arr = [-10, 2, -2, -20, 10]
m = -10

subarraySum(arr, m)