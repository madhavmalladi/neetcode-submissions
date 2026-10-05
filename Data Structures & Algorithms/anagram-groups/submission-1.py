from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strs = ["abc", "bca", "dcd"]
        # "abc": frequency array = [1,1,1,0,0,...,0]
        # "bca": freq array = [1,1,1,0,0,...,0]
        # "dcd": freq array = [0,0,1,2,0,0,0,...,0]
        # strsMap = {[1,1,1,0,0,...,0] : ["abc", "bca"],
        #            [0,0,1,2,0,0,0,...,0]: ["dcd"]}
        # ans = [] --> for key in strsMap: ans.append(strsMap[key])


        ans = []
        strsMap = defaultdict(list)

        for string in strs:
            frequency_arr = [0] * 26
            for char in string:
                frequency_arr[ord(char) - ord('a')] += 1
            strsMap[tuple(frequency_arr)].append(string)

        for key in strsMap:
            ans.append(strsMap[key])

        return ans
