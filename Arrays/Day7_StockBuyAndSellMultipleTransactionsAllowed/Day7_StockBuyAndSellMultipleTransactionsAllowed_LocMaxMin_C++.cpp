/*
The cost of stock on each day is given in an array price[]. Each day you may decide to either
buy or sell the stock i at price[i], you can even buy and sell the stock on the same day. 
Find the maximum profit that you can get.

Note: A stock can only be sold if it has been bought previously and multiple stocks cannot be held on any given day.
*/

#include <iostream>
#include <vector>

using namespace std;

int maximumProfit(vector <int> &prices){
    int n = prices.size();

    int locMin = prices[0];
    int locMax = prices[0];

    int profit = 0;

    int i = 0;

    while (1 < n - 1){
        while (i < n - 1 && prices[i] >= prices[i +1]){
            i++;
        }
        locMin = prices[i];

        while(i < n - 1 && prices[i] <= prices[i + 1]){
            i++;
        }
        locMax = prices[i];
        
        profit += (locMax - locMin);
    }

    return profit;
}

int main(){
    vector<int> prices = { 100, 180, 260, 310, 40, 535, 695 };
    cout << maximumProfit(prices) << endl;
    return 0;
}

