# tuple =it stores multiple items in a single variable
# unmutale/unchangeble
# ordered
# non homogenous
# allows duplicate values
# myTuple= (1,2,3,4,4)
# print(myTuple)
# print(len(myTuple))
# tuple1= ("car","bike","boat","jet")

# list1 = list(tuple1)
# list1.append("cycle")
# tuple2= tuple(list1)
# print(tuple2)
# tuple1= (10,20,30,40,50)
# list1 = list(tuple1)
# list1.reverse()
# tuple2 = tuple(list1)
# print(tuple2)

# tuple1 = ("soni",)
# print(tuple1)
# del tuple1
# print(tuple1)

tuple1= (1,2,3,[6,7],4,5)
print(tuple1[3][0])
list1 = list(tuple1)
list1[3][0]=8

print(tuple(list1))