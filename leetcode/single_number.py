from collections import defaultdict
from typing import List
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:

# Input: [2,2,1]
# Output: 1
# Example 2:

# Input: [4,1,2,1,2]
# Output: 4

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        check = defaultdict(int)
        for n in nums:
            check[n] += 1
        
        for n in check:
            if check[n] == 1:
                print(n)
                return n
                    
test = Solution()
test.singleNumber([4,1,2,1,2])