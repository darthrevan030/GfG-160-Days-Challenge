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

if __name__ == "__main__":
    arr = [1, 5, 8, 10]
    print(getMinDiff(arr, 2))