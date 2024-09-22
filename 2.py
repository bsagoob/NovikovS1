num = int(input("Введите число для разложения на простые множители: "))
def p(n, d=2):
    if n == 1:
        return []
    
    if n % d == 0:
        return [d] + p(n // d, d)
    else:

        return p(n, d + 1)

print(p(num))
