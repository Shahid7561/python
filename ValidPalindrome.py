def isPalindrome(s):
    left, right = 0, len(s) - 1
        
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
            
        if s[left].lower() != s[right].lower():
            return False
            
        left += 1
        right -= 1
        
    return True

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
# This function uses two pointers, one starting from the beginning of the 
# string and the other from the end. It advances both pointers while skipping
# non-alphanumeric characters. Then, it compares the characters at the two 
# pointers, converting them to lowercase for comparison. If the characters 
# are not the same, it returns False. If the pointers meet in the middle 
# without encountering any mismatched characters, the function returns True.