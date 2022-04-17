text = input().split(" ")
palindrome = input()
palindrome_list = []

for word in text:
    if word == "".join(reversed(word)): # or == word[::-1]
        palindrome_list.append(word)

print(palindrome_list)
print(f"Found palindrome {palindrome_list.count(palindrome)} times")

