def sum(a,b):
    return a+b
def diff(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

print ("Select a operation:\n\
    1:Addition\
    2:Subtraction\
    3:Multiplication\
    4:Division")

select=int(input("Select operation from 1,2,3,4: "))

num1=int(input("number1= "))
num2=int(input("number2="))

if select==1:
    print(num1,"+",num2,"=",sum(num1,num2))
elif select==2:
    print(num1,"-",num2,"=",diff(num1,num2))
elif select==3:
    print(num1,"*",num2,"=",mul(num1,num2))
elif select==4:
    print(num1,"/",num2,"=",div(num1,num2))
else:
    print("invalid input.")