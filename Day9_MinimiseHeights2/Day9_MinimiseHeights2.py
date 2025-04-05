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
'''

def getMinDiff(arr, k):
    n = len(arr)

    tallest = arr[0]
    shortest = arr[0]

    diff = 0

    i = 0

    while i < n - 1:
        
        while i < n - 1 and arr[i] >= arr[i + 1]:
                i += 1
        shortest = arr[i] + k 
        while i < n - 1 and arr[i] <= arr[i + 1]:
                i += 1
        tallest = arr[i] - k
    
    diff = tallest - shortest

    return diff

if __name__ == "__main__":
    arr = [1, 5, 8, 10]
    print(getMinDiff(arr, 2))

    arr2 = [3, 9, 12, 16, 20]
    print(getMinDiff(arr2, 3))