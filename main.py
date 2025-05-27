from leencode import LeenCode

if __name__ == "__main__":
    leen_obj =  LeenCode()

    #9. Palindrome Number: https://leetcode.com/problems/palindrome-number/ 
    x = 121
    print(f"Is {x} palindrome? {leen_obj.isPalindromeInt(x)}")
    x = -121
    print(f"Is {x} palindrome? {leen_obj.isPalindromeInt(x)}")
    x = 10
    print(f"Is {x} palindrome? {leen_obj.isPalindromeInt(x)}")

    #125. Valid Palindrome: https://leetcode.com/problems/valid-palindrome/description/ 
    s = "A man, a plan, a canal: Panama"
    print(f"Is {s} palindrome? {leen_obj.isPalindrome(s)}")
    s = "race a car"
    print(f"Is {s} palindrome? {leen_obj.isPalindrome(s)}")
    s = " "
    print(f"Is {s} palindrome? {leen_obj.isPalindrome(s)}")

    #214. Shortest Palindrome: https://leetcode.com/problems/shortest-palindrome/description/
    s = "aacecaaa" #Output: "aaacecaaa"
    print(f"The shortesr palindrome for {s} is: {leen_obj.shortestPalindrome(s)}")
    s = "abcd" #Output: "dcbabcd"
    print(f"The shortesr palindrome for {s} is: {leen_obj.shortestPalindrome(s)}")

    #12. Integer to Roman: https://leetcode.com/problems/integer-to-roman/description/
    num = 3749 #Output: "MMMDCCXLIX"
    print(f"{num} to Roman numeral is: {leen_obj.intToRoman(num)}")
    num = 58   #Output: "LVIII"
    print(f"{num} to Roman numeral is: {leen_obj.intToRoman(num)}")
    num = 1994   #Output: "MCMXCIV"
    print(f"{num} to Roman numeral is: {leen_obj.intToRoman(num)}")

    #13. Roman to Integer: https://leetcode.com/problems/roman-to-integer/description/
    s = "III" #Output: 3
    print(f"{s} to Integer is: {leen_obj.romanToInt(s)}")
    s = "LVIII" #Output: 58
    print(f"{s} to Integer is: {leen_obj.romanToInt(s)}")
    s = "MCMXCIV" #Output: 1994
    print(f"{s} to Integer is: {leen_obj.romanToInt(s)}")

    #7. Reverse Integer: https://leetcode.com/problems/reverse-integer/description/ 
    x = 123 #Output: 321
    print(f"The reversed signed 32-bit integer of {x} is: {leen_obj.reverse(x)}")
    x = -123 #Output: -321
    print(f"The reversed signed 32-bit integer of {x} is: {leen_obj.reverse(x)}")
    x = 120 #Output: 21
    print(f"The reversed signed 32-bit integer of {x} is: {leen_obj.reverse(x)}")







