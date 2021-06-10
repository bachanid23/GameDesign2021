#Deeya Bachani
#We are learning about lists and tuples
#Learn their functions and looping with list
from typing import Counter


myFruit=["apples", "berries", "mangoes", "bananas"]
print(myFruit)
for fruit in myFruit:
    print(fruit)

for fruit in myFruit:
    print(fruit, end= " , ")
print()
Counter=len(myFruit) #length of your list is one more than your last index

for x in range(0,Counter-1):
    print(myFruit[x], end= " , ")

print(myFruit[Counter-1]) #print the last element

if "apples" in myFruit:
    print("Yes, you got apples")
    myFruit.remove("apples")
    print(myFruit)
myFruit.insert(0,"kiwi")
myFruit.insert(2,"papaya")
myFruit.append("beets")
print(myFruit)

