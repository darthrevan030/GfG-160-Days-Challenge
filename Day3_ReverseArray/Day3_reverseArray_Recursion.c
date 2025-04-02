// C Program to reverse an array using Recursion
/*
You are given an array of integers arr[]. Your task is to reverse the given array.
Note: Modify the array in place.
*/

#include <stdio.h>

// recursive function to reverse an array from l to r
void reverseArrayRec(int arr[], int l, int r) {
    if(l >= r)
        return;

    // Swap the elements at the ends
    int temp = arr[l];
    arr[l] = arr[r];
    arr[r] = temp;

    // Recur for the remaining array
    reverseArrayRec(arr, l + 1, r - 1);
}

// function to reverse an array
void reverseArray(int arr[], int n) {
    reverseArrayRec(arr, 0, n - 1);
}

int main() {
    int arr[] = { 1, 4, 3, 2, 6, 5 };
    int n = sizeof(arr) / sizeof(arr[0]);

    reverseArray(arr, n);

    for(int i = 0; i < n; i++) 
        printf("%d ", arr[i]);
    
    return 0;
}