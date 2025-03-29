'''
Given an array of positive integers arr[], return the second largest element from the array. 
If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element
'''

'''
The idea is to sort the array in non-decreasing order. Now, we know that the largest element will be at index n - 1. 
So, starting from index (n - 2), traverse the remaining array in reverse order. As soon as we encounter an element which 
is not equal to the largest element, return it as the second largest element in the array. 
If all the elements are equal to the largest element, return -1.
'''

#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        n = len(arr)
        arr.sort()
        
        for i in range(n - 2, -1, -1):
            if arr[i] != arr[n-1]:
                return arr[i]
        
        return -1

if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    print(Solution.getSecondLargest(arr))