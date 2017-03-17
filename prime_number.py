prime_number = [2]

for i in range(2, 1000):
    for j in range(2, i):
        if i % j == 0:
            break
        if i - 1 == j:
            prime_number.append(i)

for i in prime_number:
    print(i, end = ' ')
