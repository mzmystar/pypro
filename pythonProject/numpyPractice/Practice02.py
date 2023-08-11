# -*- coding: UTF-8 -*-
from typing import List

# 买卖股票的最佳时机
class Practice02:

    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                profit = prices[i + 1] - prices[i]
        return profit


if __name__ == '__main__':
    test = Practice02
    profits = test.maxProfit(test, [6, 5, 4, 3, 2, 1])
    print(profits)
