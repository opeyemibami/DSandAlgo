from typing import List

# This solution uses a dictionary to track previously seen values.
# It has O(n) time complexity, but O(n) space complexity — violating the "constant extra space" constraint.

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         output = []
#         seen_idx_dic = {}
#         for idx, num in enumerate(numbers):
#             x = target - num 
#             if x in seen_idx_dic:
#                 output = [seen_idx_dic[x] + 1, idx + 1]  # +1 to convert to 1-indexed
#                 return output
#             else:
#                 seen_idx_dic[num] = idx 
#         return


# This is the optimal solution using the two-pointer approach.
# It runs in O(n) time and uses O(1) space, satisfying all problem constraints.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]  # Convert to 1-indexed
            elif total < target:
                left += 1
            else:
                right -= 1