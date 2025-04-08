'''
Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. 
Do the mentioned change in the array in place.
Note: Consider the array as circular.

Reversal Algorithm:
    Given arr = [1, 2, 3, 4, 5, 6] and assume d = 2
    - Think of the array as divided into 2 parts: 
        - From the initial till d --> Chunk 1
        - The remaining array --> Chunk 2
            arr = [1, 2, 3, 4, 5, 6]
                   ^  ^  |        |
                Chunk 1   Chunk 2
    - We are looking to swap the positions of the 2 arrays
        arr = [3, 4, 5, 6, 1, 2]
               |        |  ^  ^  
                Chunk 2   Chunk 1   
    - How to do that:
        - Reverse the array
            arr = [6, 5, 4, 3, 2, 1]
                   ^  ^  |        |
                 Chunk 1   Chunk 2
        - Reverse the 2 chunks separately
            arr = [3, 4, 5, 6, 1, 2]
                   |        |  ^  ^  
                     Chunk 2   Chunk 1 


Time complexity: O(n)
Space complexity: O(1)
'''

import math

def rotateArr(arr, d):
    # helper function to reverse an array between 2 indexes
    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    n = len(arr)

    d %= n # handle the case here d > n

    # reverse first d elements
    reverse(arr, 0, d -1)

    # reverse remaining n - d elements
    reverse(arr, d, n - 1)

    # reverse the entire array
    reverse(arr, 0, n -1)



    

if __name__ == "__main__":
    ar = [1, 2, 3, 4, 5]
    d = 2
    rotateArr(ar, d)
    print(ar)

    ar = [7, 3, 9, 1]
    d = 9
    rotateArr(ar, d)
    print(ar)