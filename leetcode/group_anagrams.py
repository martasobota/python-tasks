# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.

from collections import defaultdict
from typing import List
    

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in range(len(strs)):
            x = ''.join(sorted(strs[s]))
            if x not in result:
                result[x] = [strs[s]]
            else:
                result[x].append(strs[s])
        return result.values()
    
print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))