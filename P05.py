#count digits of a number 
num=int(input("Enter a number: "))
count=0
if(num==0):
    count=1
while num>0:
    num=num//10
    count=count+1
print(count)

#not without using loops10

number1 = int(input("Enter a number: "))
# Convert to string after taking absolute value
digit_count = len(str(abs(number1)))
print(digit_count)


import math
number3 = int(input("Enter a number: "))
num2=math.log(number3, 10)
print(int(num2) + 1)  # Adding 1 to account for the last digit
