class Solution:
  def maxProfit(self, prices) -> int:
    max_profit = 0
    for i in range(len(prices)):
      if (i != 0 and prices[i] > prices[i - 1]):
        max_profit += prices[i] - prices[i - 1]
    return max_profit
  
solution = Solution()
print(solution.maxProfit([1, 2, 3, 4, 5]))