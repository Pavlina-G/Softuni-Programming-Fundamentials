cards = input().split(" ")
count_shuffle = int(input())

# middle_index = (len(cards))//2

for i in range(count_shuffle):
    first_half = cards[:len(cards)//2]
    second_half = cards[len(cards)//2:]
    final_cards = []
    for element1, element2 in zip(first_half, second_half):

        final_cards.append(element1)
        final_cards.append(element2)

        cards = final_cards

print(cards)




