'''
Given an array of positive integers arr[], return the second largest element from the array. 
If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element
'''

'''
The idea is to keep track of the largest and second largest element while traversing the array. 
Initialize largest and secondLargest with -1. Now, for any index i,

If arr[i] > largest, update secondLargest with largest and largest with arr[i].
Else If arr[i] < largest and arr[i] > secondLargest, update secondLargest with arr[i].
'''

#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        n = len(arr)

        largest = -1
        secondLargest = -1

        # finding the second largest element
        for i in range(n):

            # If arr[i] > largest, update second largest with
            # largest and largest with arr[i]
            if arr[i] > largest:
                secondLargest = largest
                largest = arr[i]
        
            # If arr[i] < largest and arr[i] > second largest, 
            # update second largest with arr[i]
            elif arr[i] < largest and arr[i] > secondLargest:
                secondLargest = arr[i]

        return secondLargest

#{ 
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends