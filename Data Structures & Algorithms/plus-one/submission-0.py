class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        for digit in digits:
            string += str(digit)
        num = int(string)
        num += 1
        string = str(num)
        res = []
        for char in string:
            res.append(int(char))
        return res