class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        symbols = {")":"(","}":"{","]":"["}
        for i in s:
            if i in symbols:
                if stack and stack[-1]==symbols[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack