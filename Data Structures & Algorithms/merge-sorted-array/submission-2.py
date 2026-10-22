class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # get pointers to start at the ends of both at proper index, with third pointer
        # at end of nums1, put the max of the two there, the ncontinue
        i, j, k = m - 1, n - 1, m + n - 1
        while n > 0:         
            if nums2[j] >= nums1[i] or m == 0:
                nums1[k] = nums2[j]
                j -= 1
                n -= 1
            elif nums2[j] < nums1[i] and m > 0:
                nums1[k] = nums1[i]
                i -= 1
                m -= 1
            k -= 1
        