'''
You are given an array arr[] of non-negative integers. 
Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. 
The operation must be performed in place, meaning you should not use extra space for another array.
'''

'''
Use a two-pointer technique:
One pointer (count) keeps track of the position where the next non-zero element should be placed.
The other pointer (i) iterates through the array to find non-zero elements.

Implementation:
Initialize count = 0. This pointer will track the index where the next non-zero element should be placed.

Traverse the array using a for loop:
    - If the current element (arr[i]) is non-zero:
        - Swap arr[i] with arr[count]. This places the non-zero element at the correct position.
        - Increment count to move to the next position for the next non-zero element.
Zeros are naturally pushed to the end because count only moves forward when a non-zero element is encountered, leaving zeros behind.
'''

class Solution:
	def pushZerosToEnd(self,arr):
		# code here
		count = 0
		
		for i in range(len(arr)):
			if arr[i] != 0:
				arr[i], arr[count] = arr[count], arr[i]
				count += 1

if __name__ == "__main__":
	arr = [1, 2, 0, 4, 3, 0, 5, 5, 0, 3, 2]
	solution = Solution()
	solution.pushZerosToEnd(arr)
	
	for num in arr:
		print(num, end = " ")