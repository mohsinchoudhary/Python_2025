class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        if n==0:
            return nums1
        end_idx = len(nums1)-1
        while m>0 and n >0:
            if nums2[n-1] >= nums1[m-1]:
                nums1[end_idx] = nums2[n-1]
                n = n-1
            else:
                nums1[end_idx] = nums1[m-1]
                m=m-1
            end_idx = end_idx - 1
        while n>0:
            nums1[end_idx]=nums2[n-1]
            n=n-1
            end_idx = end_idx -1

sol = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3 
n = 3
#Output: [1,2,2,3,5,6]

#nums1 = [1], m = 1, nums2 = [], n = 0 #output [1]
print(sol.merge(nums1,m,nums2,n))


        #i=0
        #j=0
        #for i in range(final_array):
        #while i<=final_array:
        #    if nums1[i]<=nums2[j]:
        #        nums1.insert(i,nums2[j])
        #        j = j+1
        #    i=i+1
        #return nums1