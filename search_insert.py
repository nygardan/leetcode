# Given a sorted array of distinct integers and a target value,
# return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums, target) -> int:
        for n in nums:
            if n == target or target < n:
                return nums.index(n)
        return len(nums)

# Accepted 10-28-2020 on the first try with no help!
                       
            
                
                
