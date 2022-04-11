#First variant
tail = input()
body = input()
head = input()
meerkat = [head,body,tail]
print(meerkat)

#Second variant
tail = input()
body = input()
head = input()
meerkat = [tail, body, head]
meerkat[0], meerkat[2] = meerkat[2], meerkat[0]
print(meerkat)
