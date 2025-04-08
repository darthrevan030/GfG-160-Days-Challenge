// C++ Code to left rotate an array using Reversal Algorithm

/*
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
*/


#include <iostream>
#include <vector>

using namespace std;

// Function to rotate an array by d elements to the left
void rotateArr(vector<int>& arr, int d) {
    int n = arr.size();

    // Handle the case where d > size of array
    d %= n;

    // Reverse the first d elements
    reverse(arr.begin(), arr.begin() + d);

    // Reverse the remaining n-d elements
    reverse(arr.begin() + d, arr.end());

    // Reverse the entire array
    reverse(arr.begin(), arr.end());
}

int main() {
    vector<int> arr = { 1, 2, 3, 4, 5, 6 };
    int d = 2;
    
    rotateArr(arr, d);

    for (int i = 0; i < arr.size(); i++) 
        cout << arr[i] << " ";
    return 0;
}