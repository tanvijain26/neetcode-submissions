class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        x=[]
        for i in nums:
            freq[i]=freq.get(i,0)+1
        
        x=sorted(freq,key=freq.get,reverse=True)
        return x[:k]