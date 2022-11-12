colors = ["Red","Blue","Red","Black","22"]
cars = ["TATA","NANO","ALTO","Jeep"]
players = ["Dhoni","Messi","Dravid"]
newList= []
for i in cars:
    if 'A' in i:
        newList.append(i)
print(newList)
newList = [x for x in cars if x == "TATA"]
print(newList)





#[print(x) for x in cars]

#for x in cars:
    #print(x)
#x = 0
#while x < len(cars):
 #   print(cars[x])
  #  x=x+1
#colors[ :2] = "Green","Yellow"
#print(colors)
#colors.insert(2,"indigo")
#print(colors)
#colors.append("BMW")
#print(colors)
#colors.extend(cars)
#print(colors)
#colors.extend(players)
#print(colors)
#colors.remove("Red")
#print(colors)
#colors.pop(1)
#print(colors)
#del colors[0]
#print(colors)
#colors.clear()
#print(colors)