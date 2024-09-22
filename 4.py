size = int(input("Введите количество строк: "))
symb = input("Введите символ для треугольника: ")

def print_triangle(size, symb, current=1):
    if current > size:
        return 
    print(symb * current)
    print_triangle(size, symb, current + 1) 

def print_mirrored_triangle(size, symb):
    print_triangle(size, symb)
    for current in range(size - 1, 0, -1):
        print(symb * current)

print_mirrored_triangle(size, symb)
