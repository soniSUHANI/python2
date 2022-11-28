# tuple1=(1,2,3)
# (one,two,three)= tuple1
# print(one)
# print(two)
# print(three)

# tuple1=("car","bike","boat","cycle")
# (item1,*item2,item3)= tuple1
# print(item1)
# print(item2)
# print(item3)
#write a program to unpack following tuple into 4 variables
tuple1=(10,20,30,40)
(num1,num2,num3,num4)=tuple1
print(num1)
print(num2)
print(num3)
print(num4)
# for i in tuple1:
    # print(i)
i = 0
a = len(tuple1)
while(i<a):
    print(tuple1[i])
    i = i+1
