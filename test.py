a = 'Hello'
# print(a[0])
l = [[3, 3, 3], [1, 1, 1], [2, 2, 2]]
l[0][2] = 7
# Объявление массива
k = list()   # k = []
k.append(1)
k.insert(0, 'a')
k.append('!')
k_copy = k[:]

for el in k:
    print(el)

print()
#
# for i in range(3):
#     if i == 1:
#         continue
#     print(k[i])

print()

i = 0
while i < 3:
    print(k[i])
    i += 1

print()

i = 0
while True:
    print(k[i])
    i += 1
    if i == 2:
        break
