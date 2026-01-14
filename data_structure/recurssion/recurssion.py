def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

factorial(4)

print(factorial(4))

def sum_n(n):
    if n==0:
        return 0
    return n + sum_n(n-1)

print(sum_n(10))



