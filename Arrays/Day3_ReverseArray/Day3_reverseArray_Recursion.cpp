// C++ Program to reverse an array using Recursion

/*
You are given an array of integers arr[]. Your task is to reverse the given array.
Note: Modify the array in place.
*/


#include <iostream>
#include <vector>
using namespace std;

// recursive function to reverse an array from l to r
void reverseArrayRec(vector<int> &arr, int l, int r) {
    if(l >= r)
        return;

    // Swap the elements at the ends
    swap(arr[l], arr[r]);

    // Recur for the remaining array
    reverseArrayRec(arr, l + 1, r - 1);
}

// function to reverse an array
void reverseArray(vector<int> &arr) {
    int n = arr.size();
    reverseArrayRec(arr, 0, n - 1);
}

int main() {
    vector<int> arr = { 1, 4, 3, 2, 6, 5 };

    reverseArray(arr);

    for(int i = 0; i < arr.size(); i++) 
        cout << arr[i] << " ";
    return 0;
}