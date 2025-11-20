class Solution:
    def maxProfit(self, prices: List[int]) -> int:                
        if not prices:
            return 0
            
        left = 0  # buy pointer
        right = 1  # sell pointer
        max_profit = 0
        
        while right < len(prices):
            if prices[left] < prices[right]:
                # Calculate profit
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                # Move left pointer to current right position
                # (found a new potential minimum price)
                left = right
            right += 1
            
        return max_profit
                  
