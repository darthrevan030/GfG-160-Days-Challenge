#include <iostream>
#include <vector>
using namespace std;


void pushZerosToEnd(vector<int> &arr){
    int count = 0;

    for (int i = 0; i < arr.size(); i++){
        if (arr[i] != 0){
            swap(arr[i], arr[count]);
            count++;
        }
    }
}


int main(){
    vector<int> arr = {1, 2, 0, 4, 3, 0, 5, 5, 0, 3, 2};
    pushZerosToEnd(arr);

    for (int num : arr){
        cout << num << " ";
    }
}