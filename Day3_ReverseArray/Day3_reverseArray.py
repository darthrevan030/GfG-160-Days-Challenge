'''
You are given an array of integers arr[]. Your task is to reverse the given array.
Note: Modify the array in place.'''

class Solution:

def reverseArray(self, arr):

if __name__ == "__main__":
	arr = [1, 2, 0, 4, 3, 0, 5, 5, 0, 3, 2]
	solution = Solution()
	solution.reverseArray(arr)
	
	for num in arr:
		print(num, end = " ")