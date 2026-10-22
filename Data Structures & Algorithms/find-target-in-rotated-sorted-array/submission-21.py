class Solution:
    def search(self, nums: List[int], target: int) -> int:
                
        '''
        input: sorted rotated list(int) + target (int) 
        output: index (int) of the target if it's there, -1 if not 
        '''

        # grab the midpoint using binary search, l and r. we'll compare left bounds to the mid to see if that side is the sorted side. if it's not the sorted side, we know the other side is, and we'll compare the bounds of the sorted side with the target. move l, r accordingly 

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2 
            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]: # if left side is sorted, see if target is within it 
                if target >= nums[l] and target < nums[m]:
                    r = m - 1
                    continue 
                else:
                    l = m + 1
            else: # else, right side is sorted, compare that side
                if target > nums[m] and target <= nums[r]: # if within right side
                    l = m + 1
                else: # otherwise, it's less than midpoint or greater than end of right side
                    r = m - 1

        # if l > r, we've searched the array, and we return -1
        return -1 
