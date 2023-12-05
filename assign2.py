# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:30:50 2023

@author: urdil
"""

def majority_elements(nums):
 if not nums:
  return []
 # Initialize candidates and counters
 Candidate1, count1 = None, 0 
 Candidate2, count2 = None, 0
 # Voting processf
 for num in nums:
  if num == candidate1:
   Count1 += 1
  elif num == candidate2:
   Count2 += 1
  elif count1 == 0: 
   Candidate1, count1 = num, 1 
  elif count2 == 0: Candidate2, 
  count2 = num, 1
 else:
  Count1 -= 1
 Count2 -= 1
 # Count occurrences of candidates
 Count1, count2 = 0, 0 
for num in nums:
 if num == candidate1:
  Count1 += 1
 elif num == candidate2:
  Count2 += 1
 # Check if candidates appear more than n/3 times
 N = len(nums)
 Result = []
 if count1 > n // 3: 
   Result.append(candidate1)
 if count2 > n // 3:
  Result.append(candidate2)
   return Result[]
# Example usage:
Nums_input = [3, 2, 3]
Output_result = majority_elements(nums_input)
Print(output_result)
