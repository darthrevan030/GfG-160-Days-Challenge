'''
Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. 
Do the mentioned change in the array in place.
Note: Consider the array as circular.

Juggling Algorithm:
    Given arr = [1, 2, 3, 4, 5, 6]
    - Form chunks of d size (Assume d = 2 for this explanation)
        arr = [[1, 2], [3, 4], [5, 6]] --> Not actually made into 2D array, just for visual purposes
    - Shift pieces of each chunk into the place where it would be rotated to
        - Shift 1st piece first
            arr = [[3, 2], [5, 4], [1, 6]] --> 3 iterations to reach here
        - Once done with 1st piece, do the 2nd piece
            arr = [[3, 4], [5, 6], [1, 2]] --> 3 iterations to reach here
        - How to shift pieces:
            - Keep track of the current and next index
            - arr[cur] = arr[next]
            - Shift the next index by d
            - Shift cur index to where next index was
            - Repeat until cur index is at the end and next index loops over to the front (because of the use of modulo)
            - Repeat d more times
        


Time complexity: O(n)
Space complexity: O(1)
'''

import math

def rotateArr(arr, d):
    n = len(arr)

    d %= n # handle the case for when d > n

    cycles = math.gcd(n, d) # calculate number of cycles by finding the greatest common divisor

    for i in range(cycles):
        startElement = arr[i] # start element of current cycle

        cur = i #start index of current cycle

        # rotate elements till we reach start of cycle
        while True: 
            next = (cur + d) % n

            if next == i:
                break
            
            # update the next index with the current index
            arr[cur] = arr[next]
            cur = next

        # copy the starting element of the current cycle at the end of the cycle
        arr[cur] = startElement

if __name__ == "__main__":
    ar = [1, 2, 3, 4, 5]
    d = 2
    rotateArr(ar, d)
    print(ar)

    ar = [7, 3, 9, 1]
    d = 9
    rotateArr(ar, d)
    print(ar)