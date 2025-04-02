'''
You are given an array of integers arr[]. Your task is to reverse the given array.
Note: Modify the array in place.
'''

# Python Program to reverse an array using inbuilt methods

# function to reverse an array
def reverse_array(arr):
    arr.reverse()

if __name__ == "__main__":
    arr = [1, 4, 3, 2, 6, 5]

    reverse_array(arr)
    print(" ".join(map(str, arr)))