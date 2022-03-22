"""
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
"""
# pattern 10
n = 5
k = n - 1
for i in range(0, n):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for _ in range(0, i+1):
        print("* ", end="")
    print("\r")
