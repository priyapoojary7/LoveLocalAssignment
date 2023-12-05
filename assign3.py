# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:40:12 2023

@author: urdil
"""

def shortest_palindrome(s):
 if not s:
  return 
 # Helper function to check if a string is a palindrome
 def is_palindrome(string):
  return string == string[::-1]
 n = len(s)
 # Find the longest palindrome prefix
 i = n
 while i > 0 and not is_palindrome(s[:i]):
  i -= 1
 # Construct the shortest palindrome
 return s[i:][::-1] + s
# Example usage:
input_string1 = 'aacecaaa'
output_result1 = shortest_palindrome(input_string1)
print(output_result1)
input_string2 = 'abcd'
output_result2 = shortest_palindrome(input_string2)
print(output_result2)