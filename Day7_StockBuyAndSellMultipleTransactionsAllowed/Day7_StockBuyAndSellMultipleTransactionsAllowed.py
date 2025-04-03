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

        for i in range(n-1):
            if prices[i + 1] < prices[i]:
                locMax = prices[i]
            if locMin > prices[i]:
                locMin = prices[i]
            
            profit += (locMax - locMin)
        
        return profit


if __name__ == "__main__":
    arr = [100, 180, 260, 310, 40, 535, 695]
    solution = Solution()
    result = solution.maximumProfit(arr)
    print(result)