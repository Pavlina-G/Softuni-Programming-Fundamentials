def next_version(num):
    next_soft_version = int(num[0] + num[1] + num[2]) + 1
    print(".".join(str(next_soft_version)))


version = input().split(".")
next_version(version)