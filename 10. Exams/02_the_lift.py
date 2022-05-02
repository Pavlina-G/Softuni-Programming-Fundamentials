people = int(input())
lift = list(map(int, input().split(" ")))

result = []

for wagon in lift:
    free_space = min(4 - wagon, people)
    wagon += free_space
    people -= free_space
    result.append(str(wagon))

if people > 0:
    print(f"There isn't enough space! {abs(people)} people in a queue!")
    print(" ".join(result))
elif sum(map(int,result)) < len(lift) * 4:
    print("The lift has empty spots!")
    print(" ".join(result))
elif people == 0 and sum(map(int,result)) == len(lift) * 4:
    print(" ".join(result))