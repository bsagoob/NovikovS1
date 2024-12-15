def prime_factors(n):
    """Функция"""
    if n < 2:
        return "Невозможно" if n != 1 else "1"
    
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return " x ".join(map(str, factors))

assert prime_factors(12) == "2 x 2 x 3", "Тест 1 не пройден"
assert prime_factors(20) == "2 x 2 x 5", "Тест 2 не пройден"
assert prime_factors(7) == "7", "Тест 3 не пройден"
assert prime_factors(1) == "1", "Тест 4 не пройден"
assert prime_factors(0) == "Невозможно"
assert prime_factors(-15) == "Невозможно"
assert prime_factors(30) == "2 x 3 x 5", "Тест 7 не пройден"
assert prime_factors(100) == "2 x 2 x 5 x 5", "Тест 8 не пройден"
assert prime_factors(13) == "13", "Тест 9 не пройден"

print("Все тесты пройдены")

