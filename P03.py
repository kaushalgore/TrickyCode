#print a for divisible by 3 b for 7 and c for both 3 and 7 
num=int(input("Enter number :"))
if(num%3==0 and num%7==0):
    print("c")
elif(num%3==0):
    print("a") 
elif(num%7==0):
    print("b")
else:
    print("number not divisible by 3 or 7")