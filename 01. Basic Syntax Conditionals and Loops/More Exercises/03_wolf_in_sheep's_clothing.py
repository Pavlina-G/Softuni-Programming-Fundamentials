animal = input().split(", ")
list_of_animals = animal

list_of_animals.reverse()
counter = 0
n = len(list_of_animals) # returns number of the animals 3(sheep, sheep, wolf)

for i in range(n):
    if list_of_animals[i] == "wolf" and i == 0:
        print("Please go away and stop eating my sheep")
        break
    elif list_of_animals[i] == "wolf" and i != 0:
        counter += i
        print(f"Oi! Sheep number {counter}! You are about to be eaten by a wolf!")
        break


# string=input().split(", ")
# list=[]
# list=string
# n=len(list)
#
# for i in (range(n)):
#
#
#        if list[n-1]=="wolf" :
#
#               print("Please go away and stop eating my sheep")
#               break
#        elif list[i]=="wolf" :
#               print(f"Oi! Sheep number {n-i-1}! You are about to be eaten by a wolf!")
#               break
