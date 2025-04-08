'''
Given an array arr[] that contains positive and negative integers (may contain 0 as well). 
Find the maximum product that we can get in a sub-array of arr[].

Note: It is guaranteed that the output fits in a 32-bit integer.
'''

def maxProduct(arr):
    n = len(arr)

    result = arr[0]
    maxEnding = arr[0]

    for i in range(1, n):
        maxEnding = max(maxEnding * arr[i], arr[i])

        result = max(maxEnding, result)

    return result

if __name__ == "__main__":
    arr = [-2, 6, -3, -10, 0, 2]
    print(maxProduct(arr))

    arr2 = [-1, -3, -10, 0, 6]
    print(maxProduct(arr2))

    arr3 = [2, 3, 4] 
    print(maxProduct(arr3))