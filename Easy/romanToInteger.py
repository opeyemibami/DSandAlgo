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
    

    # class Solution:
    # def romanToInt(self, s: str) -> int:
    #     roman_map = {
    #         'I': 1,
    #         'V': 5,
    #         'X': 10,
    #         'L': 50,
    #         'C': 100,
    #         'D': 500,
    #         'M': 1000
    #     }

    #     total = 0
    #     previous_value = 0
    #     for char in reversed(s):
    #         value = roman_map[char]
    #         if value >= previous_value:
    #             total += value
    #             previous_value = value
    #         else:
    #             total -= value

    #     return total