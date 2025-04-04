'''
Given an array prices[] of length n, representing the prices of the stocks on different days. 
The task is to find the maximum profit possible by buying and selling the stocks on different days 
when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible 
to make a profit then return 0.

Note: Stock must be bought before being sold.

In order to maximize the profit, we need to minimize the cost price and maximize the selling price. 
So at every step, we keep track of the minimum buy price of stock encountered so far. 
For every price, we subtract with the minimum so far and if we get more profit than the current result, 
we update the result.
'''

def maxProfit(prices):
    n = len(prices)

    profit = 0
    minimum = prices[0]

    for i in range(n):
        minimum = min(minimum, prices[i])

        profit = max(profit, prices[i] - minimum)

    return profit


if __name__ == "__main__":
    prices = [7, 10, 1, 3, 6, 9, 2]
    print(maxProfit(prices))

    price = [7, 6, 4, 3, 1]
    print(maxProfit(price))

    prices2 = [1, 3, 6, 9, 11]
    print(maxProfit(prices2))