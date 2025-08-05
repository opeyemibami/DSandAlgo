class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
    


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        num = x
        rev_num = 0
        while x>0:
            digit = x%10
            rev_num = (rev_num * 10) + digit
            x = (x//10)
        return num==rev_num


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending in 0 (but not 0 itself) cannot be palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev_half = 0

        # Reverse only half of the number
        while x > rev_half:
            digit = x % 10
            rev_half = rev_half * 10 + digit
            x //= 10

        # For even digit numbers: x == rev_half
        # For odd digit numbers: x == rev_half // 10 (middle digit is ignored)
        return x == rev_half or x == rev_half // 10
