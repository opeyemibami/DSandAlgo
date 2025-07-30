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
    
# Solution 2 (using a dictionary for better performance)
# This solution has a time complexity of O(n) and is more efficient.
# It uses a dictionary to store the indices of the numbers, allowing for quick lookups.
# Uncomment the code below to use this solution.

# from typing import List
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