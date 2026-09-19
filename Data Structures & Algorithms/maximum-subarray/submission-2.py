class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i=0
        best=nums[0]
        sum=float("-inf")
        for i in range(len(nums)):
            sum=max(nums[i],nums[i]+sum)
            best=max(best,sum)
        return best
        