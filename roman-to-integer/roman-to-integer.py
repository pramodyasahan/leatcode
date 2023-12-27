class Solution(object):
    @staticmethod
    def romanToInt(s):
        dec = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        i = len(s) - 1
        while i >= 0:
            if i < len(s) - 1 and dec[s[i]] < dec[s[i + 1]]:
                total = total - dec[s[i]]
            else:
                total = total + dec[s[i]]
            i -= 1
        return total


s = Solution()
result = s.romanToInt("MCMXCIV")
print(result)
