a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:5"))
if a>b:
    if a>c:
        print("Largest number is:",a)
    else:
        print("Largest number is:",c)
else:
    if b>c:
        print("Largest number is:",b)
    else:
        print("Largest number is:",c)