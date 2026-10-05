class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp=prices[0]
        res=0
        for i in range(len(prices)):
            minp=min(minp,prices[i])
            res=max(res,prices[i]-minp)
        return res