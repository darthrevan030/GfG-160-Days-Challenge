'''
Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. 
Do the mentioned change in the array in place.
Note: Consider the array as circular.
'''
'''
Time complexity: O()
Space complexity: O()
'''

def rotateArr(arr, d):
    

if __name__ == "__main__":
    ar = [1, 2, 3, 4, 5]
    d = 2
    rotateArr(ar, d)
    print(ar)

    ar = [7, 3, 9, 1]
    d = 9
    rotateArr(ar, d)
    print(ar)