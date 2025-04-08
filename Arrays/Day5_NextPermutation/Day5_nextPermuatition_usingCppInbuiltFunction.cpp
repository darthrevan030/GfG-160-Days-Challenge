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
*/

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<int> arr = { 2,4,1,7,5,0 };
    next_permutation(arr.begin(), arr.end());
    for (int num : arr)
        cout << num << " ";
    return 0;
}