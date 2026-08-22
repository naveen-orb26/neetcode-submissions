class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        if len(s)!=len(t):
            return False
        n = len(s)
        for i in range(n):
            map1[s[i]] = 1 + map1.get(s[i],0)
            map2[t[i]] = 1 + map2.get(t[i],0)
        
        return map1==map2 

        