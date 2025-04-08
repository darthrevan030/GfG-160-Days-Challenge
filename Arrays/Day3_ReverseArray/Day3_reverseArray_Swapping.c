// C Program to reverse an array by swapping elements

/*
You are given an array of integers arr[]. Your task is to reverse the given array.
Note: Modify the array in place.
*/


#include <stdio.h>

// function to reverse an array
void reverseArray(int arr[], int n) {
    
    // Iterate over the first half and for every index i,
    // swap arr[i] with arr[n - i - 1]
    for (int i = 0; i < n / 2; i++) {
        int temp = arr[i];
        arr[i] = arr[n - i - 1];
        arr[n - i - 1] = temp;
    }
}

int main() {
    int arr[] = { 1, 4, 3, 2, 6, 5 };
    int n = sizeof(arr) / sizeof(arr[0]);

    reverseArray(arr, n);

    for (int i = 0; i < n; i++) 
        printf("%d ", arr[i]);
    
    return 0;
}