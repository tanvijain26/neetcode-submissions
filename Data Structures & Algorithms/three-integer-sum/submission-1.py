class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        for i in range(len(nums)):
            seen=set()
            for j in range(i+1,len(nums)):
                k=-(nums[i]+nums[j])
                if k in seen:
                    triplet=[nums[i],nums[j],k]
                    triplet.sort()
                    if triplet not in ans:
                        ans.append(triplet)
                seen.add(nums[j])
        return ans