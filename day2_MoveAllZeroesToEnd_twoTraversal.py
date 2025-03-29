'''
You are given an array arr[] of non-negative integers. 
Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. 
The operation must be performed in place, meaning you should not use extra space for another array.
'''

'''
First Traversal: Shift non-zero elements
Traverse the array and maintain the count of non-zero elements. This count is initialized with 0 and keeps track 
of where the next non-zero element should be placed in the array. If the element is non-zero, place it at arr[count] 
and increment count by 1. After traversing all the elements, all non-zero elements will be shifted 
to the front while maintaining their original order.

Second Traversal: Fill remaining positions with zeros
After the first traversal, all non-zero elements will be at the start of the array and count will store the index 
where the first zero should be placed. Iterate from count to the end of array and fill all indices with 0.
'''

class Solution:
	def pushZerosToEnd(self,arr):
		# code here
		count = 0 # initialise pointer at the start of the array
		
		for i in range(len(arr)):
			if arr[i] != 0:
				arr[count] = arr[i]
				count += 1
			else:
				arr[count] = arr[i]

		while count < len(arr):
			arr[count] = 0
			count += 1

if __name__ == "__main__":
	arr = [1, 2, 0, 4, 3, 0, 5, 5, 0, 3, 2]
	solution = Solution()
	solution.pushZerosToEnd(arr)
	
	for num in arr:
		print(num, end = " ")