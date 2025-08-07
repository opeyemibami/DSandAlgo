# Roman to Integer

Roman numerals are represented by seven different symbols:

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

For example:
- `2` is written as `II` (1 + 1)
- `12` is written as `XII` (10 + 1 + 1)
- `27` is written as `XXVII` (10 + 10 + 5 + 1 + 1)

### Subtractive Rules

In some cases, a smaller numeral comes before a larger one, indicating subtraction:

- `IV` = 4 (5 - 1)
- `IX` = 9 (10 - 1)
- `XL` = 40 (50 - 10)
- `XC` = 90 (100 - 10)
- `CD` = 400 (500 - 100)
- `CM` = 900 (1000 - 100)

---

## Problem Statement

Given a Roman numeral string, convert it to an integer.

### Constraints:

- `1 <= s.length <= 15`
- `s` contains only the characters `'I', 'V', 'X', 'L', 'C', 'D', 'M'`
- It is guaranteed that `s` is a valid Roman numeral in the range `[1, 3999]`

---

## 🧪 Examples

### Example 1:

**Input**: `s = "III"`  
**Output**: `3`  
**Explanation**: `III = 1 + 1 + 1 = 3`

---

### Example 2:

**Input**: `s = "LVIII"`  
**Output**: `58`  
**Explanation**: `L = 50`, `V = 5`, `III = 3` → Total = `50 + 5 + 3 = 58`

---

### Example 3:

**Input**: `s = "MCMXCIV"`  
**Output**: `1994`  
**Explanation**:  
- `M = 1000`  
- `CM = 900`  
- `XC = 90`  
- `IV = 4`  
Total = `1000 + 900 + 90 + 4 = 1994`

---

## ✅ Solution 1

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        for char in reversed(s):  # Process from right to left
            value = roman_map[char]
            if value < prev_value:
                total -= value  # Subtract if smaller than the previous (e.g. IV, IX)
            else:
                total += value
                prev_value = value

        return total
```

## ✅ Solution 2
```py
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        previous_value = 0
        for char in reversed(s):
            value = roman_map[char]
            if value >= previous_value:
                total += value
                previous_value = value
            else:
                total -= value

        return total
```
### ✅ Why This Works:
Roman numerals are read from left to right, but we reverse the string to simplify subtraction logic.

When a smaller value appears before a larger one, we subtract it.

Both solutions use linear time (O(n)) and constant space.

### 🧠 Summary

| Feature              | Value                          |
| -------------------- | ------------------------------ |
| Time Complexity      | O(n), where n is length of `s` |
| Space Complexity     | O(1)                           |
| Handles Subtractions | ✅ Yes                          |
| Efficient & Clean    | ✅ Yes                          |
