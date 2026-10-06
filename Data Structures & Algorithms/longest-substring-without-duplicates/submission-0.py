class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt=0
        res=0
        seen=set()
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[cnt])
                cnt+=1
            seen.add(s[i])
            res=max(res,i-cnt+1)
        return res
        