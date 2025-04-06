'''
Given an array arr[]. You need to find and return the maximum sum from all the sub-arrays.

Approach:
    - Traverse through the array only once
    - Initialise 2 variables maxEnding and result at arr[0]
    - Each element of the array you advance you compare maxEnding + arr[i] with just arr[i] to see if the sum of the current sub-array
    is bigger than the next element on its own
    - If maxEnding + arr[i] bigger then the current sub-array is the largest, update result to the new sum
    - If arr[i] is bigger than the current sub-array then update result and maxEnding to the new sum and begin formation of new sub-array
    - 
'''

def maxSubArraySum(arr):

    n = len(arr)
    result = arr[0]
    maxEnding = arr[0]

    for i in range(1, n):
        maxEnding = max(maxEnding + arr[i], arr[i])

        result = max(maxEnding, result)
    
    return result


if __name__ == "__main__":
    arr = [2, 3, -8, 7, -1, 2, 3]
    print(maxSubArraySum(arr))

    arr2 = [-2, -4]
    print(maxSubArraySum(arr2))

    arr3 = [5, 4, 1, 7, 8]
    print(maxSubArraySum(arr3))