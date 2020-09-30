# Given a sorted array nums, remove the duplicates in-place
# such that each element appears only once and returns the new length.

#Do not allocate extra space for another array,
# you must do this by modifying the input array in-place with O(1) extra memory.

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) == 0:
            return 0
        
        count = 0
        while count != (len(nums) -1):
            if nums[count] == nums[count+1]:
                nums.pop(count)
            else:
                count += 1
        print(nums)
        return len(nums)
            
# Solved 9/30/2020 with no help from 'Solution' or 'Discussion'
