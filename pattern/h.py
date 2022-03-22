""" 
    *
   ***
  *****
 *******
*********
"""
# pattern 8
n = 7
for i in range(1, n):
    for _ in range(0, 6-i):
        print(" ", end="")
    for _ in range(i, 2*i-1):
        print("*", end="")
    for _ in range(1, i-1):
        print("*", end="")
    print()
