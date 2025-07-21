# A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.

## Example 1:

**Input**: s = "leeetcode"

**Output**: "leetcode"

**Explanation**:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".

## Example 2:

**Input**: s = "aaabaaaa"

**Output**: "aabaa"

**Explanation**:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".

**Solution**:
```py
class Solution:
    def makeFancyString(self, s: str) -> str:
        s = s.lower()
        result = s[:2]
        for char in s[2:]:
            if not (char==result[-1]==result[-2]):
                result += char
        return result
```
