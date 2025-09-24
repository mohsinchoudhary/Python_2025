class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        begin_index = 0
        end_index = len(nums)-1
        #print(end_index)



#// is  floor division operator.
#result1 = 7 // 3  # Output: 2 (7 divided by 3 is 2.33..., rounded down to 2)
#result2 = 10 // 4 # Output: 2 (10 divided by 4 is 2.5, rounded down to 2)
#result3 = -7 // 3 # Output: -3 (-7 divided by 3 is -2.33..., rounded down to -3)
        while begin_index<=end_index:
            mid_index = (begin_index+end_index) // 2
            print("midpoint idx :",mid_index)
            midpoint_value = nums[mid_index]
            #print(midpoint_value)
            if midpoint_value == target:
                return mid_index
            elif midpoint_value > target:
                end_index = mid_index - 1
            else:
                begin_index = mid_index + 1
        return begin_index


sol = Solution()
nums = [1,3,5,6]
target = 4
print(sol.searchInsert(nums,target))


#nums = [1,3,5,6], target = 2
#nums = [1,3,5,6], target = 7