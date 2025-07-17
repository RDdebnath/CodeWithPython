a = int(input("enter the first number : "))
b = int(input("enter the second number : "))
c = int(input("enter the third number : "))
d = int(input("enter the forth number : "))

if(a >= b and a >= c and a >= d):
    print("First number is largest : ", a)
elif(b >= c and b >= d):
    print("Second number is largest : ", a)
elif(c >= d):
    print("Third number is largest :",c)

else:
    print("Forth number is largest : ", d)
