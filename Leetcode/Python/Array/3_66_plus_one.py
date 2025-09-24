"""You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits."""

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        #number = int(''.join(map(str,digits)))
        #vSum = list(map(int,str(number+1)))
        ##print(type(vSum))
        #return vSum
        #print(number)
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + 1 != 10:
                digits[i] += 1
                print("first if",digits)
                return digits
            digits[i] = 0
            print(digits[i])
            print("before 2nd if",digits)
            print("value of i",i)

            if i == 0:
                print("value of third i",i)
                print("third if",digits)
                return [1] + digits
                

digits = [9,9]
sol=Solution()
print(sol.plusOne(digits))
#Output: [1,2,4]
#digits = [4,3,2,1] Output:[4,3,2,2]
#digits = [9] Output: [1,0]

