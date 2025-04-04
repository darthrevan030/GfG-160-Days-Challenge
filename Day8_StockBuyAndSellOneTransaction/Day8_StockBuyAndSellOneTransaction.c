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

// C Program to solve stock buy and sell
// using one traversal

#include <stdio.h>

int maxProfit(int prices[], int size) {
    int minSoFar = prices[0];
    int res = 0;

    for (int i = 1; i < size; i++) {
    
        // Update the minimum value seen so far 
      	// if we see smaller
        if (prices[i] < minSoFar) {
            minSoFar = prices[i];
        }

        // Update result if we get more profit                
        if (prices[i] - minSoFar > res)
            res = prices[i] - minSoFar;
    }
    return res;
}

int main() {
    int prices[] = {7, 10, 1, 3, 6, 9, 2};
    int size = sizeof(prices) / sizeof(prices[0]);
    printf("%d\n", maxProfit(prices, size));
    return 0;
}