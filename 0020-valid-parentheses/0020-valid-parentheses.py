class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for char in s:
            if char =='(':
                stack.append(')')
            elif char=='{':
                stack.append('}')
            elif char=='[':
                stack.append(']')
            else:
                if not stack or stack[-1]!=char:
                    return False
                else:
                    stack.pop()
        return not stack
                
