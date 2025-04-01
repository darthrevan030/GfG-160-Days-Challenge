'''
Given an array of integers arr[] representing a permutation, implement the next permutation that rearranges the numbers 
into the lexicographically next greater permutation. If no such permutation exists, rearrange the numbers into the lowest 
possible order (i.e., sorted in ascending order). 

Note - A permutation of an array of integers refers to a specific arrangement of its elements in a sequence or linear order.

Pattern: 
    To get the next permutation we change the number in a position which is as right as possible. The first number to be 
    moved is the rightmost number smaller than its next. The number to come in-place is the rightmost greater number on 
    right side of the pivot. Each permutation (except the very first) has an increasing suffix. Now if we change the pattern
    from the pivot point (where the increasing suffix breaks) to its next possible lexicographic representation we will get 
    the next greater permutation.

Implementation:
    - Iterate over the given array from end and find the first index (pivot) which doesn't follow the property of non-increasing suffix
    - If pivot index does not exist, then the given sequence is the largest as possible. So, reverse the complete array.
    - Otherwise, iterate the array from the end and find the successor (rightmost greater element) of the pivot in the suffix
    - Swap the pivot and the successor
    - Minimize the suffix part by reversing the array from pivot + 1 till n
'''

class Solution:
    def nextPermutation(self, arr):
        n = len(arr)
        pivot = -1

        # find the pivot
        for i in range(n - 2, -1, -1):
            if arr[i + 1] > arr[i]:
                pivot = i
                break

        # if pivot doesn't exist, reverse the array
        if pivot == -1:
            arr.reverse()
            return
        
        # find the successor and swap the successor and pivot
        for j in range(n - 1, pivot, -1):
            if arr[j] > arr[pivot]:
                arr[i], arr[pivot] = arr[pivot], arr[i]
                break
        
        # reverse the elements to the right of the pivot
        left = pivot + 1
        right = n - 1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -+ 1

        return arr

if __name__ == "__main__":
    arr = [2, 4, 1, 7, 5, 0]
    solution = Solution()
    result = solution.nextPermutation(arr)
    print(result)