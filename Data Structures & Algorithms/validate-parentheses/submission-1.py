class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for l in s:
            if l == "(" or l == "{" or l == "[":
                stack.append(l)
            elif l==")" and stack and stack[-1] == "(":
                stack.pop()
            elif l=="}" and stack and stack[-1] == "{":
                stack.pop()
            elif l=="]" and stack and stack[-1] == "[":
                stack.pop()
            else:
                return False
        return len(stack) == 0

        