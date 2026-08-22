class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dictionary = {}
        for num in nums:
            count_dictionary[num] = 1 + count_dictionary.get(num,0)

        freq = [[] for _ in range(len(nums)+1)]
        for n,c in count_dictionary.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res