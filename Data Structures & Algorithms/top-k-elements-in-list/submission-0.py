class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num]= 1+ counts.get(num,0)
        
        scount = sorted(counts.items(), key=lambda item:item[1], reverse=True)
        return [pair[0] for pair in scount[:k]]