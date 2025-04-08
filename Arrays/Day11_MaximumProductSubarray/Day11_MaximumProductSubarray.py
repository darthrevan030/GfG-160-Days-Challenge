'''
Given an array arr[] that contains positive and negative integers (may contain 0 as well). 
Find the maximum product that we can get in a sub-array of arr[].

Note: It is guaranteed that the output fits in a 32-bit integer.
'''

def maxProduct(arr):
    n = len(arr)

    curMin = arr[0]
    curMax = arr[0]
    maxProd = arr[0]

    for i in range(1, n):
        curMax = max(curMax * arr[i], arr[i], curMin * arr[i])

        curMin = min(curMax * arr[i], arr[i], curMin * arr[i])

        maxProd = max(curMax, curMin)

    return maxProd

if __name__ == "__main__":
    arr = [-2, 6, -3, -10, 0, 2]
    print(maxProduct(arr))

    arr2 = [-1, -3, -10, 0, 6]
    print(maxProduct(arr2))

    arr3 = [2, 3, 4] 
    print(maxProduct(arr3))