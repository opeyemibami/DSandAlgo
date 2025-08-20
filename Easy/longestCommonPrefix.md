# Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

---

## Problem Statement

Given an array of strings, return the **longest common prefix** among them.  
If no common prefix exists, return an empty string.

---

### Example 1:

**Input**:  
`strs = ["flower","flow","flight"]`  

**Output**:  
`"fl"`

---

### Example 2:

**Input**:  
`strs = ["dog","racecar","car"]`  

**Output**:  
`""`  

**Explanation**: There is no common prefix among the input strings.

---

### Constraints:
- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lowercase English letters if it is non-empty.

---

## Solution 1

```python
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Find the shortest word (prefix cannot be longer than this)
        shortest_word = min(strs, key=len)
        prefix = ""

        # Compare each character of the shortest word with all other words
        for i in range(len(shortest_word)):
            current_char = shortest_word[i]

            # Check if current_char matches across all words
            for word in strs:
                if word[i] != current_char:
                    return prefix  # mismatch found, return current prefix

            # If all matched, add the character to prefix
            prefix += current_char

        return prefix

```

## Solution 2
```Py
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for chars in zip(*strs):   # zip chars column by column
            if len(set(chars)) == 1:   # all characters match
                prefix += chars[0]
            else:
                break
        return prefix

```

✅ Why Solution 2 is Interesting:
- Very concise and pythonic.

- Uses zip(*strs) to align characters by index.

- Uses set to check if all characters in that position are the same.

- Automatically stops at the shortest word length because of zip.

⚠️ Tradeoff: Less explicit than Solution 1. May be harder to understand sometimes.