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

# d = dict()
d = {1: 20, 2: 30, 3: 'sfasdaf', 'key': ['one', 'two']}
d.update({'key_2': 'strfghhvb'})
d.pop('key_2')
# d['key_3'] = {3, 5, 50}
print(list(d.keys()))
print()
print(list(d.values()))
print()
print(list(d.items()))
print()
print(d)
print()

s = ['a', 34, 'a', 'b']
print(s)
print(list(set(s)))

if 'key_2' in d.keys():
    print(d['key_2'])
elif 'key_3' in d.keys():
    print('key_3 exists')
else:
    print('No such key!')

print()

a = 3
b = 3
c = 4
if (a == b) | (c > a):
    print('Excellent')

