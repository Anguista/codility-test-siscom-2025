"""
**LONGEST PALINDROMIC SUBSTRING**

 Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters."""


"#Solution"


def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        
        start = 0
        max_len = 1
       
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
              left -= 1
              right += 1
             return lft +1, right -1
         
         for i in range(len(s)):
             l1, r1 = expand(i, i)
             if r1 - l1 +1 > max_len:
                start = l1
                max-len = r1 -l1 +1
              l2, r2 = expand(i, i+1)
              if r2 -l2 +1 > max_len:
                 start = l2
                 max+len = r2 - l2 + 1

          return s[start:start + max_len]
              
