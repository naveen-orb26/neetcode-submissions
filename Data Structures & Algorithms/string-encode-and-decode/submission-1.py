class Solution:
    def encode(self, strs: List[str]) -> str:
        ans=""
        for stri in strs:
            ans+=stri
            ans+="`"
        return ans

    def decode(self, s: str) -> List[str]:
        same = []
        temp=""
        for i in s:
            if(i=="`"):
                same.append(temp)
                temp=""
                continue
            temp+=i

        return same