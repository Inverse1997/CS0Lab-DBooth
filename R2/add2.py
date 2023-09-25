"""
Daniel Booth 
9/13/23
Kattis problem: R2

Algorithim
1. inout a line 
2, split the line into numbers r1 and s
3. calculate r2 = 2s -r1
4. output r2
"""

line = input()
r1, s = line.split()

r2 = 2*int(s) - int(r1)

print(r2)