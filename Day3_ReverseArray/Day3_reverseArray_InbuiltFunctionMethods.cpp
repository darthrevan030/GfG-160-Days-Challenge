// C++ Program to reverse an array using inbuilt methods

/*
You are given an array of integers arr[]. Your task is to reverse the given array.
Note: Modify the array in place.
*/


#include <iostream>
#include <vector>
#include <algorithm> 
using namespace std;

// function to reverse an array
void reverseArray(vector<int> &arr) {
    reverse(arr.begin(), arr.end());
}

int main() {
    vector<int> arr = { 1, 4, 3, 2, 6, 5 };

    reverseArray(arr);
    for(int i = 0; i < arr.size(); i++) 
        cout << arr[i] << " ";
    return 0;
}