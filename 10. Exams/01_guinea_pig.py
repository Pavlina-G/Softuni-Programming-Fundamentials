food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
weight = float(input()) * 1000
days = 30

while days != 0:
    days -= 1

    food -= 300
    if days % 2 == 0:
        hay -= 0.05 * food
    if days % 3 == 0:
        cover -= 1/3 * weight

if food > 0 and hay > 0 and cover > 0:
    print(f"Everything is fine! Puppy is happy! Food: {food / 1000:.2f}, Hay: {hay / 1000:.2f}, Cover: {cover / 1000:.2f}.")
else:
    print("Merry must go to the pet store!")