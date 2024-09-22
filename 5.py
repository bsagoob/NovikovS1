import numpy as np

n = int(input("Введите количество строк (N): "))
m = int(input("Введите количество столбцов (M): "))

def create_spiral_matrix(n, m):
    matrix = np.zeros((n, m), dtype=int)
    
    top, bottom, left, right = 0, n-1, 0, m-1
    num = 1  
    
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            matrix[top, i] = num
            num += 1
        top += 1
        
        for i in range(top, bottom + 1):
            matrix[i, right] = num
            num += 1
        right -= 1
        
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom, i] = num
                num += 1
            bottom -= 1
        
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i, left] = num
                num += 1
            left += 1
    
    return matrix

def multiply_rows_by_index(matrix):
    for i in range(matrix.shape[0]):
        matrix[i] *= (i + 1)
    return matrix



spiral_matrix = create_spiral_matrix(n, m)
print("Спиральная матрица:")
print(create_spiral_matrix(n, m))

result_matrix = multiply_rows_by_index(spiral_matrix)
print("Результат после умножения каждой строки на её номер:")
print(multiply_rows_by_index(spiral_matrix))
