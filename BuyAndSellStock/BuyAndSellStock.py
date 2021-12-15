class Solution:
    def maxProfit(self, prices: List[int]) -> int:        
        newMin = float('Inf')
        newMax = float('-Inf')
        profit = 0
        
        for price in prices:
            if newMin == float('Inf') and newMax == float('-Inf'):
                newMin = price
                newMax = price
            
            if price < newMin:
                newMin = price
                newMax = price
            if price >= newMax:
                newMax = price
                if (newMax-newMin)>profit:
                    profit = newMax-newMin
        
        return profit
                