/*
Given an array prices[] of length n, representing the prices of the stocks on different days. 
The task is to find the maximum profit possible by buying and selling the stocks on different days 
when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible 
to make a profit then return 0.

Note: Stock must be bought before being sold.

In order to maximize the profit, we need to minimize the cost price and maximize the selling price. 
So at every step, we keep track of the minimum buy price of stock encountered so far. 
For every price, we subtract with the minimum so far and if we get more profit than the current result, 
we update the result.
*/

// C++ Program to solve stock buy and sell
// using one traversal

#include <iostream>
#include <vector>
using namespace std;

int maxProfit(vector<int> &prices) {

    int minSoFar = prices[0], res = 0;

    for (int i = 1; i < prices.size(); i++) {

        // Update the minimum value seen so
        // far if we see smaller
        minSoFar = min(minSoFar, prices[i]);

        // Update result if we get more profit                
        res = max(res, prices[i] - minSoFar);
    }
    return res;
}

int main() {
    vector<int> prices = {7, 10, 1, 3, 6, 9, 2};
    cout << maxProfit(prices) << endl;
    return 0;
}