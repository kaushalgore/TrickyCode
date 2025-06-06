# Swap without using a temporary variable
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
a=a+b
b=a-b
a=a-b
print("After swapping: a =", a, ", b =", b)

#python tupple unpacking swap
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
x,y=y,x
print("After swapping: x =", x, ", y =", y)
