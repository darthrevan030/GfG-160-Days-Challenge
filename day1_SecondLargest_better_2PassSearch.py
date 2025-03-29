'''
Given an array of positive integers arr[], return the second largest element from the array. 
If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element
'''

'''
The approach is to traverse the array twice. In the first traversal, find the maximum element. 
In the second traversal, find the maximum element ignoring the one we found in the first traversal.
'''

#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        n = len(arr)

        largest = -1
        secondLargest = -1

        # Finding the largest element
        for i in range(n):
            if arr[i] > largest:
                largest = arr[i]

        # Finding the second largest element
        for i in range(n):
            
            # Update second largest if the current element is greater
            # than second largest and not equal to the largest
            if arr[i] > secondLargest and arr[i] != largest:
                secondLargest = arr[i]
        
        return secondLargest


#{ 
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    print(Solution.getSecondLargest(arr))