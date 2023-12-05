# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:27:18 2023

@author: urdil
"""

def length_of_last_word(s):
 # Split the string into words
 words = s.split()
 # Check if there are any words
 if not words:
  return 0
 # Return the length of the last word
 return len(words[-1])
# Example usage:
input_string = 'Hello World'
output_length = length_of_last_word(input_string)
print(output_length)