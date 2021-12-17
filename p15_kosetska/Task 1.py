def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)
def binomial_coefficient(n):
    for i in range(n):
        x = ''
        for k in range(i+1):
            x += str(int((factorial(i)) / (factorial(k) * factorial(i - k)))) + ' '
        yield x
n = int(input("Please, input polynomial:"))
for i in binomial_coefficient(n):
    print(i)
