"""
leencode.py contains my solutions in side the LeenCode Class. On top of each function we have the problem number and name followed by its link.
"""
import re
class LeenCode:
    
    #9. Palindrome Number: https://leetcode.com/problems/palindrome-number/
    def isPalindromeInt(self, x: int) -> bool:
        """
        Checks if an integer is a palindrome.
        Args:
            x (int): The number to check.

        Returns:
            bool: True if x is a palindrome, False otherwise.
        """
        x = str(x)
        if x[::-1] == x:
            return True
        return False
    
    #125. Valid Palindrome: https://leetcode.com/problems/valid-palindrome/description/ 
    def isPalindrome(self, s: str) -> bool:
        """
        Checks if the string is a palindrome after removing all non-alphanumeric characters .
        Args:
            s (str): The string we want to check.
        Returns:
            bool: True if s is a palindrome, False otherwise.
        """
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        if s.upper() == s.upper()[::-1]:
            return True
        return False
    
    #214. Shortest Palindrome: https://leetcode.com/problems/shortest-palindrome/description/
    def shortestPalindrome(self, s: str) -> str:
        """
        Convert string to a palindrome by adding characters in front of it.
        Args:
            s (str): The string we want to convert to  a palindrome.
                     Consists of lowercase English letters only.
        Returns:
            S (str): The shortest palindrome you can find by performing this transformation.
        """
        l = len(s)
        S,s1 = s,''
        while S != S[::-1]:
            s1 += s[l-1]
            S = s1+s
            l-=1
        return S