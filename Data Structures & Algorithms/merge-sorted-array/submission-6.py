class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, m + n - 1
        
        # we want to iterate while j >= 0
        while j >= 0:
            # we want to look at the i num because we want to make sure it still has its index too
            if nums1[i] > nums2[j] and i >= 0:
                # only then do we use that
                nums1[k] = nums1[i]
                i -= 1
            else: # if not that means nums2j greater OR i simply is below 0 
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        