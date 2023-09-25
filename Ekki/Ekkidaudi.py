"""
Math and Variables Lab
By: Daniel Booth
CSCI 110 Lab
Date: 9/14/2023
Read and solve: EKKIDAUDI - https://open.kattis.com/problems/ekkidaudi 
Algorithm steps:
  1. Read data as a line
  2. Split the line into two strings named line1_a and line1_b using .split('|') method
  3. Read second line and split into two new varibles, line2_a and line2_b 
  4. Concatenate the strings into a string named answer
  5. Print the answer
"""
def main():
  a, b = input().split('|')
  c, d = input().split('|')
  ans = a+d, c+b
  print(ans)

main() # call main function