def loading_bar(num):
    if num == 100:
        print(f"100% Complete!")
        print(f"[%%%%%%%%%%]")
    else:
        print(f"{num}% [{(num//10 * '%')}{(10 - num//10) * '.'}]")
        print(f"Still loading...")


number = int(input())
loading_bar(number)