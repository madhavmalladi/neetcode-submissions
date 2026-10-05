class Solution(object):
    def isValid(self, s):
        stack = []
        for char in s:
            if (char=='(' or char=='[' or char=='{'):
                stack.append(char)
            elif (char==')'):
                if stack:
                    if (stack[-1] != '('):
                        return False
                    else:
                        stack.pop()
                elif not stack:
                    return False
            elif (char==']'):
                if stack:
                    if (stack[-1] != '['):
                        return False
                    else:
                        stack.pop()
                elif not stack:
                    return False
            elif (char=='}'):
                if stack:
                    if (stack[-1] != '{'):
                        return False
                    else:
                        stack.pop()
                elif not stack:
                    return False
        if (len(stack) == 0):
            return True
        return False
        