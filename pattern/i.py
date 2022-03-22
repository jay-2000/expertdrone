"""
*********
 *******
  *****
   ***
    *
"""
# pattern 9
n = 7
for i in range(n-1,0,-1):
    for _ in range(0, 6-i):
        print(" ", end="")
    for _ in range(i, 2*i-1):
        print("*", end="")
    for _ in range(1, i-1):
        print("*", end="")
    print()
