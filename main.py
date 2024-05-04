from time import perf_counter

primes = []

t = perf_counter()

n = 10 ** 8
p = [True] * n

for i in range(2, n):
    if p[i]:
        for j in range(i * 2, n, i):
            p[j] = False
        primes.append(i)

print(primes[-1])
print(perf_counter() - t)

with open('primes.txt', 'w', encoding='utf-8') as file:
    for i in primes:
        file.write(f'{i}\n')

exit()

def prime(x):
    for i in primes:
        if x % i == 0:
            return False
        if i ** 2 > x:
            return True
    if primes[-1] ** 2 < x:
        i = primes[-1]
        while i * i <= x:
            if x % i == 0:
                return False
            i += 1
    return True


l = list(range(1, 10))

time = perf_counter()

l2 = []
while True:
    for j in range(1, 10):
        for i in range(len(l)):
            t = int(f'{j}{l[i]}')
            if prime(t):
                l2.append(t)
        if perf_counter() - time > 3:
            print(l2[-1])
            time = perf_counter()
    l = l2.copy()
    print(f'-- {l2[-1]}')
    l2 = []