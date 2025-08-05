# Check if Integer is a Palindrome

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

> A palindrome is a number that reads the same forwards and backwards.

---

## 📘 Problem Statement

Given an integer `x`, return true if `x` is a palindrome, and false otherwise.

### Constraints:

- `-2^31 <= x <= 2^31 - 1`

### Follow-up:

> Could you solve it **without converting the integer to a string**?

---

## 📌 Examples

### Example 1:

**Input**: `x = 121`  
**Output**: `true`  
**Explanation**: 121 reads the same forwards and backwards.

---

### Example 2:

**Input**: `x = -121`  
**Output**: `false`  
**Explanation**: From left to right it reads -121. From right to left: `121-`. Not the same.

---

### Example 3:

**Input**: `x = 10`  
**Output**: `false`  
**Explanation**: From right to left, it becomes `01`. Not the same.

---

## ✅ Solution 1 – String Reversal (Simple but Not Optimal)

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
```
✅ Why This Works:
Converts the number to a string and checks if it equals its reverse.

Simple and elegant for small inputs.

❌ Why This Is Incorrect:
Violates the follow-up constraint: Uses string conversion.

Less optimal for performance-critical environments.

## ✅ Solution 2 – Full Math-Based Reversal
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        num = x
        rev_num = 0
        while x > 0:
            digit = x % 10
            rev_num = rev_num * 10 + digit
            x = x // 10

        return num == rev_num
```
✅ Why This Is Correct:
Avoids string conversion.

Reverses the entire number and compares it with the original.

Works for all positive integers.

❌ Limitation:
Slightly less efficient because it reverses the entire number, even though we only need to reverse half to verify palindromes.

## ✅ Solution 3 – Optimized Half Reversal (Most Efficient)
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers or trailing zeros are not palindromes (except 0 itself)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev_half = 0

        while x > rev_half:
            digit = x % 10
            rev_half = rev_half * 10 + digit
            x //= 10

        return x == rev_half or x == rev_half // 10

```
✅ Correct Solution (Two-Pointer – Meets All Constraints)
Reverses only half of the number, not the entire integer.

Handles odd and even digit counts.

✅ No string conversion

✅ Constant space

✅ Most performant among the three

| Solution   | Uses String? | Reverses Full Number? | Constant Space | Follow-Up Constraint Passed? |
| ---------- | ------------ | --------------------- | -------------- | ---------------------------- |
| Solution 1 | ✅ Yes        | ✅ Yes                 | ✅ Yes          | ❌ No                         |
| Solution 2 | ❌ No         | ✅ Yes                 | ✅ Yes          | ✅ Yes                        |
| Solution 3 | ❌ No         | ❌ No (half only)      | ✅ Yes          | ✅ Yes                        |


✅ Conclusion
- ✅ Use Solution 3 when asked to avoid string conversion and meet performance expectations.

- ✅ Use Solution 1 when quick prototyping or simplicity is acceptable.

- ✅ Solution 2 is a good middle ground — easier to understand than Solution 3, but less efficient.