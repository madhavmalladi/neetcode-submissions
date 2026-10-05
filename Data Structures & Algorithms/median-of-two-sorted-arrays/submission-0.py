class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total_len = len(A) + len(B)
        half = total_len // 2

        # make sure that A is the smaller array
        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 # array A
            j = half - i - 2 # array B (-2 because both arrays are 0-indexed)

            ALeft = A[i] if i >= 0 else float('-inf')
            ARight = A[i + 1] if (i+1) < len(A) else float('inf')
            BLeft = B[j] if j >= 0 else float('-inf')
            BRight = B[j + 1] if (j+1) < len(B) else float('inf')

            if ALeft <= BRight and BLeft <= ARight: # left partition is correct
                if total_len % 2 == 1: # odd
                    return min(ARight, BRight)
                else: # even
                    return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
            elif ALeft > BRight:
                r = i - 1
            else:
                l = i + 1

