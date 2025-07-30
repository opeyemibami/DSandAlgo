# A fancy string is a string where no three consecutive characters are equal.

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Example 1:

**Input**: nums = [2,7,11,15], target = 9

**Output**: [0,1]

**Explanation**:
Because nums[0] + nums[1] == 9, we return [0, 1].

## Example 2:

**Input**: nums = [3,2,4], target = 6

**Output**: [1,2]

## Example 3:

**Input**: nums = [3,3], target = 6
**Output**: [0,1]


**Solution1**:
```py
from typing import List
# Solution 1 (brute force)
# This solution has a time complexity of O(n^2) and is not optimal for large lists.
# It iterates through each element and checks for pairs that sum to the target.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        if(len(nums)==2):
            return [0,1]
        for i,first in enumerate(nums):
            rest = nums[i+1:]
            for n in rest:
                if((first+n ==target) and (first!=n)):
                    output = [i,nums.index(n)]
                    return output
                elif((first+n ==target) and (first==n)):
                    first_instance_index = i
                    for k in range(first_instance_index+1,len(nums)):
                        if nums[k]==first:
                            output = [i,k]
                            return output
        return output
```


**Solution2**:
```py
#Solution2 (using a dictionary for better performance)
# This solution has a time complexity of O(n) and is more efficient.
# It uses a dictionary to store the indices of the numbers, allowing for quick lookups.
# Solved like algebra x + y = target where y = [y1,y1....yn]
# Uncomment the code below to use this solution.
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenNumIdx_dic = {}
        output = []
        for idx,num in enumerate(nums):
            x = target - num
            if x in seenNumIdx_dic:
                output = [idx,seenNumIdx_dic[x]]
                return output
            else:
                seenNumIdx_dic[num]=idx

        return output
```