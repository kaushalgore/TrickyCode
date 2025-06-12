#find is number power of 2 or not
num=int(input("Enter a Number: "))
for i in range (0,int(num/2)+1):
    if(2**i==num):
        print("Yes, it is a power of 2")
        break
else:
    print("No, it is not a power of 2")

#Check if a number is a power of 2 without using loops

import math
def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0  

#In binary, these numbers have only one '1' bit and the rest are **'0'**s.
#n & (n - 1) removes the lowest set bit from n.
# If n is a power of two:
# In binary: only one bit is set (like 1000)
# n - 1 flips that bit and sets all lower bits to 1.