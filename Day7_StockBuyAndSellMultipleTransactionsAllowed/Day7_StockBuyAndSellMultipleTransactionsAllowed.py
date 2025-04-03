'''
The cost of stock on each day is given in an array price[]. Each day you may decide to either
buy or sell the stock i at price[i], you can even buy and sell the stock on the same day. 
Find the maximum profit that you can get.

Note: A stock can only be sold if it has been bought previously and multiple stocks cannot be held on any given day.
'''

from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        n = len(arr)
        
        profit = 0
        locMax = prices[0]
        locMin = prices[0]

        i = 0

        while i < n - 1:
            while i < n - 1 and prices[i] >= prices[i + 1]:
                i += 1
            locMin = prices[i]
            while i < n - 1 and prices[i] <= prices[i + 1]:
                i += 1
            locMax = prices[i]

            profit += (locMax - locMin)
        
        return profit


if __name__ == "__main__":
    arr = [100, 180, 260, 310, 40, 535, 695]
    solution = Solution()
    result = solution.maximumProfit(arr)
    print(result)