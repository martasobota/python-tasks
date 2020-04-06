# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: 
# Starting with any positive integer, replace the number by the sum of the squares of its digits, 
# and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
# Those numbers for which this process ends in 1 are happy numbers.

class Solution:
    def isHappy(self, n: int) -> bool:
        result = 0
        to_sq = [int(i) for i in str(n)]
        for num in to_sq:
            result += num **2
        if result == 1 or result == 7:
            return True
        else:
            if result < 10 or result == 0:
                return False
            else:
                return self.isHappy(result)

test = Solution()
test.isHappy(19)
test.isHappy(1111111)