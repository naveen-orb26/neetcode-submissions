class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1len = len(s1)
        left = 0
        s1hash = [0]*26
        s2hash = [0]*26
        for i in s1:
            s1hash[ord(i)-ord('a')]+=1
        for right in range(len(s2)):
            s2hash[ord(s2[right])-ord('a')]+=1
            if right-left+1 > s1len:
                s2hash[ord(s2[left])-ord('a')]-=1
                left+=1
            if s2hash==s1hash:
                return True
        return False