usernames = input().split(', ')

for user in usernames:
    condition = user.isalnum() or '-' in user or '_' in user

    if 3 <= len(user) <= 16 and condition:
        print(user)