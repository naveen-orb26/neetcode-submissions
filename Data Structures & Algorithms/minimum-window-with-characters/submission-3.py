class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s)<len(t):
            return ""
        counter = Counter(t)
        stores = defaultdict(int)
        have = 0
        need = len(counter)

        resultlen = float("inf")
        resultrange = (-1,-1)
        left = 0

        for right in range(len(s)):
            char = s[right]
            stores[char]+=1
            if char in counter and counter[char]==stores[char]:
                have+=1
            
            while have == need:
                if (right-left+1)<resultlen:
                    resultlen = right -left +1
                    resultrange = (left,right)
                leftchar = s[left]
                stores[leftchar]-=1
                if (leftchar in counter and stores[leftchar]<counter[leftchar]):
                    have-=1
                left+=1
        l,r = resultrange
        return s[l:r+1] if resultlen!=float("inf") else ""

