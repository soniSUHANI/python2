numbers = [1,2,3,4,5,2,6]
#in the above list ,find value 2 ,if it is present,
#replace it with 200,only update the first occrance

for x in numbers:
    if x==2:
        a=numbers.index(x)
        numbers.pop(numbers.index(2))
        numbers.insert(a,200)
        break
print(numbers)
