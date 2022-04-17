text = input().split(" ")
filtered_text = list(x for x in text if len(x) % 2 == 0)
print("\n".join(filtered_text))
