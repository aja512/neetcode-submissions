class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        totalLen = len(nums1) + len(nums2)
        half = totalLen // 2

        if len(B) < len(A):
            A, B = B, A

        left, right = 0, len(A) - 1
        while True:
            i = (left + right) // 2
            j = half - i - 2

            AL = A[i] if i >= 0 else float("-infinity")
            BL = B[j] if j >= 0 else float("-infinity")
            AR = A[i + 1] if (i + 1) < len(A) else float("infinity")
            BR = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if AL <= BR and BL <= AR:
                if totalLen % 2:
                    return min(AR, BR)
                return (max(AL, BL) + min(AR, BR)) / 2
            elif AL > BR:
                right = i - 1
            else:
                left = i + 1

