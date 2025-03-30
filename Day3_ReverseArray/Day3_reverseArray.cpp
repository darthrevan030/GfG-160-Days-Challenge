#include <iostream>
#include <vector>
using namespace std;

// function to reverse an array
void reverseArray(vector<int> &arr) {
    int n = arr.size();
    
    // Iterate over the first half and for every index i,
    // swap arr[i] with arr[n - i - 1]
    for(int i = 0; i < n/2; i++) {
        swap(arr[i], arr[n - i - 1]);
    }
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    reverseArray(arr);

    for(int i = 0; i < arr.size(); i++) 
        cout << arr[i] << " ";
    return 0;
}