class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        open_set = {"{", "(", "["}

        for char in s:
            # opening parenthesis
            if (char in open_set):
                stack.append(char)
            # closing parenthesis
            elif (char in hashmap):
                if (not stack):
                    return False
                elif (stack.pop() == hashmap[char]):
                    continue
                else:
                    return False
        
        if (not stack):
            return True
        
        return False
            