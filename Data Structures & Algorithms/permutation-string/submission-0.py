class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
         - have 2 frequency arrays, one for s1 and the other for s2
         - first, fill out the frequency array for s1 and also for the first 
            len(s1) characters for s2, this can be done using a singular for 
            loop
         - next, we run a loop through s2, with a sliding window of fixed
            length len(s1)
            - we compare freq_s2 == freq_s1, if this is ever true then we
                return True
            - if not true, then we decrement the count of the left-most char
                and increment the count of the next char on the right
         '''

        if (len(s1) > len(s2)):
            return False
        if (s1 == s2):
            return True

        s1_freqs, s2_freqs = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1_freqs[ord(s1[i]) - ord('a')] += 1
            s2_freqs[ord(s2[i]) - ord('a')] += 1
        
        if s1_freqs == s2_freqs:
            return True
        
        left = 0
        for right in range(len(s1), len(s2)):
            s2_freqs[ord(s2[left]) - ord('a')] -= 1
            left += 1
            s2_freqs[ord(s2[right]) - ord('a')] += 1

            if s1_freqs == s2_freqs:
                return True

        return False

