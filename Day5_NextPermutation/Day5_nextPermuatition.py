'''
Given an array of integers arr[] representing a permutation, implement the next permutation that rearranges the numbers 
into the lexicographically next greater permutation. If no such permutation exists, rearrange the numbers into the lowest 
possible order (i.e., sorted in ascending order). 

Note - A permutation of an array of integers refers to a specific arrangement of its elements in a sequence or linear order.
'''
def nextPermutation(self, arr):
if __name__ == "__main__":
    arr = [2, 4, 1, 7, 5, 0]
    nextPermutation(arr)
    print(" ".join(map(str, arr)))