class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_sum = 0
        abs_min = prices[0]
        for i in range(1,len(prices)):
            if prices[i] - abs_min > current_sum :
                current_sum = prices[i] - abs_min
            if prices[i] < abs_min:
                abs_min = prices[i]
        return current_sum