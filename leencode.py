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
    #12. Integer to Roman: https://leetcode.com/problems/integer-to-roman/description/
    def _intToRomanCont_(self, num: int, ans: str,val1: str,val2: str,val3: str) -> str :
        """
        Contienues with the process of convering integer to a Roman numeral.
        Args:
            num (int): The integer value a a given place value
            ans (str): The string we are creating to hold the roman numerals
            val1 (str): The smallest roman numeral in a given range 
            val2 (str): The middle roman numeral in a given range 
            val3 (str): The largest roman numeral in a given range 
        Returns:
            ans (str): The current converted Roman numeral.
        """
        if 0<num<4:
            return ans+val1*num
        elif num==4:
            return ans+val1+val2
        elif num==5:
            return ans+val2
        elif 9>num>5:
            return ans+val2+val1*(num-5)
        elif num==9:
            return ans+val1+val3
        return ans
    def intToRoman(self,num: int) -> str:
        """
        Convert a given integer to a Roman numeral.

        EXAMPLLE:

        Input: num = 3749
        Output: "MMMDCCXLIX"
        Explanation:
            3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
             700 = DCC as 500 (D) + 100 (C) + 100 (C)
              40 = XL as 10 (X) less of 50 (L)
               9 = IX as 1 (I) less of 10 (X)

        Args:
            num (int): The integer we want we want to convert to  roman numeral. 1 <= num <= 3999
        Returns:
            ans (str): The converted Roman numeral.
        """
        s = str(num)[::-1]
        l = len(s)-1
        ans = ""
        while l>-1:
            b = "0"*l
            v = int(s[l])
            if len(b)==3:
                ans+="M"*v
            elif len(b)==2:
                ans = self._intToRomanCont_(v, ans,"C","D","M")
            elif len(b)==1:
                ans = self._intToRomanCont_(v, ans,"X","L","C")
            else:
                ans = self._intToRomanCont_(v, ans,"I","V","X")
            l-=1
        return ans
    
    #13. Roman to Integer: https://leetcode.com/problems/roman-to-integer/description/
    def romanToInt(self, s: str) -> int:
        """
        Convert a given Roman numeral to integer.

        EXAMPLLE:

        Input: s = "MCMXCIV"
        Output: 1994
        Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

        Args:
            s (str): The Roman numeral we want we want to convert to  integer. 1 <= s.length <= 15
                        s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
        Returns:
            ans (int): The converted Integer from Roman numeral.
        """
        dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        b = 0
        ans = 0
        for i in s[::-1]:
            a = dic.get(i)
            if b<=a:
                ans+=a
            else:
                ans-=a
            b = a
        return ans

    #7. Reverse Integer: https://leetcode.com/problems/reverse-integer/description/ 
    def reverse(self, x: int) -> int:
        """
        Reversing digits of a signed 32-bit integer x.

        Example 2:
            Input: x = 123
            Output: 321
        
        Args:
            x (int): A signed 32-bit integer.
        return:
            x (int): x with its digits reversed or 0 when x reversed is outside the 
            signed 32-bit integer range [-231, 231 - 1]   
        """

        if x>0:
            x = str(x)[::-1]
        else:
            x = "-"+str(x)[1:][::-1]

        if ((-2**31) < int(x) < (2**31 - 1)) :
            return int(x)
        else:
            return 0
        