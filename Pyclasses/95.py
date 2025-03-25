def prime(n):
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i

print(list(prime(int(input("Give the number to get the prime till here: ")))))