##Given an array nums and a value val, remove all instances of that value
##in-place and return the new length.
##Do not allocate extra space for another array,
##you must do this by modifying the input array in-place with O(1) extra memory.
##The order of elements can be changed.
##It doesn't matter what you leave beyond the new length.

class Solution:
    def removeElement(self, nums, val) -> int:
        if len(nums) == 0:
            return 0
        
        count = 0
        while count != (len(nums)):
            if nums[count] == val:
                nums.pop(count)
            else:
                count += 1
        return len(nums)
            
# Solved 10/1/2020 with no help from 'Solution' or 'Discussion'
# However, I sought out better solutions in 'Discuss'
# Because my code was not very fast (only faster than 73.33 % of solutions)


## I should have thought of the below:
## from https://leetcode.com/problems/remove-element/discuss/867340/Python3-28ms
## class Solution:
##    def removeElement(self, nums: List[int], val: int) -> int:
##        while val in nums:
##            nums.remove(val)
##        
##        return len(nums)
