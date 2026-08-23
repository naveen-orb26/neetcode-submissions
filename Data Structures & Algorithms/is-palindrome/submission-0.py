class Solution:
    def isPalindrome(self, s: str) -> bool:
        st="".join(char.lower() for char in s if char.isalnum())
        print(st)
        return st==st[::-1]
        