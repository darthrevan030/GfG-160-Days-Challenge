// C Program to move all zeros to end using one traversal

#include <stdio.h>

// Function which pushes all zeros to end of array
void pushZerosToEnd(int arr[], int n) {

    // Pointer to track the position for next non-zero element
    int count = 0;

    for (int i = 0; i < n; i++) {

        // If the current element is non-zero
        if (arr[i] != 0) {

            // Swap the current element with the 0 at index 'count'
            int temp = arr[i];
            arr[i] = arr[count];
            arr[count] = temp;

            // Move 'count' pointer to the next position
            count++;
        }
    }
}

int main() {
    int arr[] = {1, 2, 0, 4, 3, 0, 5, 0};
    int size = sizeof(arr) / sizeof(arr[0]);
    
    pushZerosToEnd(arr, size);
    
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    
    return 0;
}