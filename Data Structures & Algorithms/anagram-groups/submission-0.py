class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        hashmap = defaultdict(list)
        for string in strs:
            counts = [0] * 26
            for char in string:
                counts[ord(char) - ord('a')] += 1
            hashmap[tuple(counts)].append(string)
        
        for key in hashmap:
            ans.append(hashmap[key])
        
        return ans