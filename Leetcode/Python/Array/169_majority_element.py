"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 Follow-up: Could you solve the problem in linear time and in O(1) space? -> This means o(n) time and 1 variable space for o(1)

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        hash = {}
        for i in nums:
            hash[i] = 1+hash.get(i,0)
        return max(hash,key=hash.get)
        print(hash)


nums = [2,2,1,1,1,2,2,3]
sol=Solution()
print(sol.majorityElement(nums))