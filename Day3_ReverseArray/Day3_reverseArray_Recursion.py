# Python Program to reverse an array using Recursion

'''
You are given an array of integers arr[]. Your task is to reverse the given array.
Note: Modify the array in place.
'''

# recursive function to reverse an array from l to r
def reverseArrayRec(arr, l, r):
    if l >= r:
        return

    # Swap the elements at the ends
    arr[l], arr[r] = arr[r], arr[l]

    # Recur for the remaining array
    reverseArrayRec(arr, l + 1, r - 1)

# function to reverse an array
def reverseArray(arr):
    n = len(arr)
    reverseArrayRec(arr, 0, n - 1)

if __name__ == "__main__":
    arr = [1, 4, 3, 2, 6, 5]

    reverseArray(arr)

    for i in range(len(arr)):
        print(arr[i], end=" ")