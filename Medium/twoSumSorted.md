# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

## Example 1:

**Input**: numbers = [2,7,11,15], target = 9  
**Output**: [1,2]  
**Explanation**: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

## Example 2:

**Input**: numbers = [2,3,4], target = 6  
**Output**: [1,3]  
**Explanation**: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

## Example 3:

**Input**: numbers = [-1,0], target = -1  
**Output**: [1,2]  
**Explanation**: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

---

## ❌ Attempted Solution (Using Dictionary – Violates Constant Space Constraint)

```python
from typing import List

# This solution uses a dictionary to track previously seen values.
# It has O(n) time complexity, but O(n) space complexity — violating the "constant extra space" constraint.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output = []
        seen_idx_dic = {}
        for idx, num in enumerate(numbers):
            x = target - num 
            if x in seen_idx_dic:
                output = [seen_idx_dic[x] + 1, idx + 1]  # +1 to convert to 1-indexed
                return output
            else:
                seen_idx_dic[num] = idx 
        return
```
## ❌ Why This Is Incorrect:
- Although this method efficiently finds the solution in O(n) time, it uses a dictionary (seen_idx_dic), which requires O(n) extra space.

- The problem explicitly requires using only constant extra space, so this approach violates that constraint and would likely be rejected in a strict environment.

## ✅ Correct Solution (Two-Pointer – Meets All Constraints)
```python
from typing import List

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
```
## ✅ Why This Is Correct:
- It leverages the fact that the input list is sorted, allowing a two-pointer search.

- Uses only two variables (left and right), which means it consumes O(1) extra space.

- Runs in O(n) time, satisfying both performance and space constraints.

- Returns the correct 1-indexed result as required.

| Aspect                          | Dictionary-Based Solution (❌) | Two-Pointer Solution (✅) |
| ------------------------------- | ----------------------------- | ------------------------ |
| Time Complexity                 | O(n)                          | O(n)                     |
| Space Complexity                | O(n)                          | O(1)                     |
| Meets Constant Space Constraint | ❌ No                          | ✅ Yes                    |
| Uses Sorted Array Property      | ❌ No                          | ✅ Yes                    |
| Returns 1-indexed Output        | ✅ Yes                         | ✅ Yes                    |
| Problem Accepted                | ❌ Likely Rejected             | ✅ Accepted               |
## ✅ Conclusion:
To meet all the constraints — especially the constant space requirement — the two-pointer solution is the correct and optimal approach.

Avoid using additional data structures like dictionaries or sets unless the problem explicitly allows extra space. The two-pointer method is simple, efficient, and leverages the sorted nature of the input for performance and correctness.