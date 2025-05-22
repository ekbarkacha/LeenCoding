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

