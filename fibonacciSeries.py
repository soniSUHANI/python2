n = int(input("Enter the no of terms: "))
if n<= 0:
    print("invalid")
if n==1:
    print(0)
if n>=2:
    num1 = 0
    num2= 1
    print(num1)
    print(num2)
    for i in range(2,n):
        a = num1+num2
        print(a)
        num1 =num2
        num2= a
        
    
