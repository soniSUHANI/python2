def calculator(num1,num2,op):
    if op =='+':
        return num1+num2
    elif op == '-':
        return num1-num2
    elif op == '*':
        return num1*num2
    elif op == '/':
        return num1/num2

num1 = float(input("enter num1: "))
num2 = float(input("enter num2: "))
op = str(input("enter a operator: "))
ans= calculator(num1,num2,op)
print(ans)