class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for each string, we would count the frequency of each character
        # {a: 1, c: 1, t:1},  {p: 1, o: 1, t: 1, s: 1}
        # {{a: 1, c: 1, t:1} : ["act", "cat"]}
        # defaultdict(list)

        frequencies = defaultdict(list)
        
        for string in strs:
            freq = [0] * 26
            for char in string:
                freq[ord(char) - ord('a')] += 1
            
            frequencies[tuple(freq)].append(string)

        ans = []
        for key in frequencies:
            ans.append(frequencies[key])
        
        return ans
