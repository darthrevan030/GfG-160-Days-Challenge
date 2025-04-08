/*
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
*/

#include <iostream>
#include <vector>
#include <numeric> // tp be able to use inbuilt greatest common denominator function

using namespace std;

// Function to rotate an array by d elements to the left
void rotateArr(vector<int>& arr, int d) {
    int n = arr.size();

    // Handle the case where d > size of array
    d %= n;

    int cycles = gcd(n, d);

    for (int i = 0; i < cycles; i++){
        int startElement = arr[i];
        int cur = i;

        while(true){
            int next = (cur + d) % n;

            if (next == i){
                break;
            }

            arr[cur] = arr[next];
            cur = next;
        }

        arr[cur] = startElement;
    }

}

int main() {
    vector<int> arr = { 1, 2, 3, 4, 5, 6 };
    int d = 2;
    
    rotateArr(arr, d);

    for (int i = 0; i < arr.size(); i++) 
        cout << arr[i] << " ";
    return 0;
}