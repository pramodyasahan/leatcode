class Solution(object):
    def isPalindrome(self, x):
        char_list = [int(i) for i in str(x)]
        rev_list = char_list[::-1]
        if char_list == rev_list:
            return True
        else:
            return False
