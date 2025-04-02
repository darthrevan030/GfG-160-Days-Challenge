/*
You are given an array of integer arr[] where each number represents a vote to a candidate. 
Return the candidates that have votes greater than one-third of the total votes, If there's 
not a majority vote, return an empty array. 

Note: The answer should be returned in an increasing format.

The idea is based on the observation that there can be at most two majority elements, which appear more 
than n/3 times. so we can use Boyer-Moore’s Voting algorithm. As we iterate the array, We identify 
potential majority elements by keeping track of two candidates and their respective counts.

Steps:
    - Initialize two variables ele1 = -1 and ele2 = -1, for candidates and two variables cnt1 = 0 and cnt2 = 0, for counting.
    - In each iteration,
        - If an element is equal to any candidate, update that candidate's count.
        - If count of a candidate reaches zero then replace that candidate with current element.
        - If neither candidate matches and both counts are non zero, decrement the counts.
    - After this, in second pass we check if the chosen candidates appear more than n/3 times in the array. 
    - If they do then include them in result array.
    - Since any element than appears more than floor(n/3) times, will dominate over elements that appear less frequently.
    - Whenever we encounter a different element, we decrement the count of both the candidates. This maintains at most 
    two candidates in the array.

*/

// C++ program for finding the majority element in an array
// using Moore’s Voting algorithm

#include <iostream>
#include <vector>
#include <algorithm>
#include <limits.h>
using namespace std;

// Function to find Majority element in an array
vector<int> findMajority(vector<int> &arr) {
    int n = arr.size();

    // Initialize two candidates and their counts
    int ele1 = -1, ele2 = -1, cnt1 = 0, cnt2 = 0;

    for (int ele : arr) {

        // Increment count for candidate 1
        if (ele1 == ele) {
            cnt1++;
        }

        // Increment count for candidate 2
        else if (ele2 == ele) {
            cnt2++;
        }

        // New candidate 1 if count is zero
        else if (cnt1 == 0) {
            ele1 = ele;
            cnt1++;
        }

        // New candidate 2 if count is zero
        else if (cnt2 == 0) {
            ele2 = ele;
            cnt2++;
        }

        // Decrease counts if neither candidate
        else {
            cnt1--;
            cnt2--;
        }
    }

    vector<int> res;
    cnt1 = 0;
    cnt2 = 0;

    // Count the occurrences of candidates
    for (int ele : arr) {
        if (ele1 == ele) cnt1++;
        if (ele2 == ele) cnt2++;
    }

    // Add to result if they are majority elements
    if (cnt1 > n / 3) res.push_back(ele1);
    if (cnt2 > n / 3 && ele1 != ele2) res.push_back(ele2);
    
    if(res.size() == 2 && res[0] > res[1])
        swap(res[0], res[1]);
    return res;
}

int main() {
    vector<int> arr = {2, 2, 3, 1, 3, 2, 1, 1};
    vector<int> res = findMajority(arr);
    for (int ele : res) {
        cout << ele << " ";
    }
    return 0;
}