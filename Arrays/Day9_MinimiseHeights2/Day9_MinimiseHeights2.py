'''
Given an array arr[] denoting heights of N towers and a positive integer K.

For each tower, you must perform exactly one of the following operations exactly once.
    - Increase the height of the tower by K
    - Decrease the height of the tower by K

Find out the minimum possible difference between the height of the shortest and tallest 
towers after you have modified each tower.

You can find a slight modification of the problem here: https://practice.geeksforgeeks.org/problems/minimize-the-heights-i/1/

Note: It is compulsory to increase or decrease the height by K for each tower. After the operation, 
the resultant array should not contain any negative integers.

Approach:
- Sort the array
- Assume maximum is arr[n -1]
- Assume minimum is arr[0]
- Subtract k from the large numbers
- Add k to the smaller numbers
- How to decide whether to add or subtract:
    - Base Case:
        diff = (arr[0] + k) - (arr[n - 1] - k) --> idea being that once k is added or subtracted, the initially larger 
        number becomes the smaller number
    - Check if by adding k the number becomes negative or not
        - If it does, add k to the number and move on to the next number
    - Keep checking as above until we find the point in the array where subtracting k does not turn the number negative
    - Once found:
        - Compare the old maximum (arr[n-1]) to the new maximum (the number that is 1 before the point where 
        subtracting k from the number does not turn it negative anymore) to find the new maximum
        - Compare the old minimum (arr[0]) to the new minimum (the number that is the 1st to not turn negative
        when subtracting k from it) to find the new minimum
        - Compare the difference between the old set of max/min and the new set of max/
            - If the difference is smaller, that is the answer

'''

def getMinDiff(arr, k):
    n = len(arr)
    arr.sort()

    diff = arr[n - 1] - arr[0]

    for i in range(1, n):
        if arr[i] - k < 0:
            continue

        minHeight = min(arr[0] + k, arr[i] - k)

        maxHeight = max(arr[i - 1] + k, arr[n - 1] - k)

        diff = min(diff, maxHeight - minHeight)

    return diff

if __name__ == "__main__":
    arr = [1, 5, 8, 10]
    print(getMinDiff(arr, 2))

    arr2 = [3, 9, 12, 16, 20]
    print(getMinDiff(arr2, 3))