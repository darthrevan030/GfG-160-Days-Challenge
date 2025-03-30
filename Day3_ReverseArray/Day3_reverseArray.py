'''
You are given an array of integers arr[]. Your task is to reverse the given array.
Note: Modify the array in place.'''

class Solution:
	def reverseArray(self, arr):
		# code here
		n = len(arr)
		
		for i in range(n//2):
			arr[i], arr[n-1-i] = arr[n-1-i], arr[i]

if __name__ == "__main__":
	arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	solution = Solution()
	solution.reverseArray(arr)
	
	for num in arr:
		print(num, end = " ")