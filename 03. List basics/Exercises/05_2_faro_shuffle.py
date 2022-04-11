cards = input().split(' ')
count_of_shuffles = int(input())

for i in range(count_of_shuffles):
    first_half = cards[:len(cards)//2]
    second_half = cards[len(cards)//2:]
    final_cards = []

    for a,b in zip(first_half, second_half):
        final_cards.append(a)
        final_cards.append(b)

        cards = final_cards

print(cards)

