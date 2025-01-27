def is_palindrome(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True

def can_form_palindrome_by_rotation(s):
    n = len(s)
    
    for i in range(n):  
        is_rotated_palindrome = True
        
        for j in range(n):  
            if s[(i + j) % n] != s[(i + n - j - 1) % n]:
                is_rotated_palindrome = False
                break
        
        if is_rotated_palindrome:
            return "Yes, the rotated string is a palindrome."
    
    return "No, the rotated string is not a palindrome."

s = input()
print(can_form_palindrome_by_rotation(s))