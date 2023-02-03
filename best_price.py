"""https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan&id=level-1"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left, right = 0, 1
        max_profit = 0
        while right < len(prices):
            current_profit = prices[right] - prices[left]
            if current_profit > 0:
                max_profit = max(current_profit, max_profit)
            else:
                left = right
            right += 1
        return max_profit


s = Solution()
test = [1,4,2]
print(s.maxProfit(test))
