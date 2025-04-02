/*
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
*/


#include <stdio.h>
#include <stdlib.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void reverse(int arr[], int start, int end) {
    while (start < end) {
        swap(&arr[start], &arr[end]);
        start++;
        end--;
    }
}

void nextPermutation(int *arr, int n) {
    // Find the pivot index
    int pivot = -1;
    for (int i = n - 2; i >= 0; i--) {
        if (arr[i] < arr[i + 1]) {
            pivot = i;
            break;
        }
    }

    // If pivot point does not exist, 
    // reverse the whole array
    if (pivot == -1) {
        reverse(arr, 0, n - 1);
        return;
    }

    // Find the element from the right that
    // is greater than pivot
    for (int i = n - 1; i > pivot; i--) {
        if (arr[i] > arr[pivot]) {
            swap(&arr[i], &arr[pivot]);
            break;
        }
    }

    // Reverse the elements from pivot + 1 to the end
    reverse(arr, pivot + 1, n - 1);
}

int main() {
    int arr[] = { 2, 4, 1, 7, 5, 0 };
    int n = sizeof(arr) / sizeof(arr[0]);

    nextPermutation(arr, n);

    // Print the result
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}