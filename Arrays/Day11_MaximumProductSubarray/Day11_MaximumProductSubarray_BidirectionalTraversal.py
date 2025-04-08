'''
Given an array arr[] that contains positive and negative integers (may contain 0 as well). 
Find the maximum product that we can get in a sub-array of arr[].

Note: It is guaranteed that the output fits in a 32-bit integer.
'''

def maxProduct(arr):
    n = len(arr)

    left2right = 1
    right2left = 1
    maxProd = float('-inf')

    for i in range(n):
        if left2right == 0:
            left2right = 1
        if right2left == 0:
            right2left = 1
        
        left2right *= arr[i]

        j = n - i - 1

        right2left *= arr[j]

        maxProd = max(left2right, right2left, maxProd)
        
    return maxProd

if __name__ == "__main__":
    arr = [-2, 6, -3, -10, 0, 2] # 180
    print(maxProduct(arr))

    arr2 = [-1, -3, -10, 0, 6] # 30
    print(maxProduct(arr2))

    arr3 = [2, 3, 4] # 24
    print(maxProduct(arr3))