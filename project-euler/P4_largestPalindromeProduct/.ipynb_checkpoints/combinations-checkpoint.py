lst = ['a', 'b', 'c']

a = 0
while a < len(lst):
    b = a
    while b < len(lst):
        print(lst[a] + lst[b])
        b += 1
    a += 1
