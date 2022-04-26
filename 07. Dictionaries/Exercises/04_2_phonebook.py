phone_book = {}

while True:

    contact_info = input()
    if contact_info.isdigit():
        break

    contact_details = contact_info.split("-")
    name = contact_details[0]

    phone_book[name] = contact_details[1]

number_of_lines = int(contact_info)

for i in range(number_of_lines):
    name = input()
    if name not in phone_book:
        print(f"Contact {name} does not exist.")
    else:
        print(f"{name} -> {phone_book[name]}")
