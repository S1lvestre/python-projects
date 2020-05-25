F = [0, 1]

n = 1

sum = 0

while F[n] < 4000000:
    F.append((F[n]+F[n-1]))
    n += 1

for i in F:
    if i % 2 == 0:
        sum = sum + i

print(sum)
