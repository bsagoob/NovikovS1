
data1 = [[1, 2], [2, 4], [3, 6]]
results1 = [0, 2]
aresults1 = mnk(data1)
assert actual_results1 == results1, f"1 Failed: expected {results1}, got {results1}"


data2 = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
results2 = [0, 1]
aresults2 = mnk(data2)
assert actual_results2 == results2, f"2 Failed: expected {results2}, got {results2}"


try:
    mnk([])
except ValueError as e:
    assert str(e) == "Данные не могут быть пустыми.", f"3 Failed: {str(e)}"


try:
    calculate_mnk_coefficients([[1, 2, 3], [4, 5]])
except ValueError as e:
    assert str(e) == "Каждая точка должна содержать ровно 2 значения.", f"4 Failed: {str(e)}"


import time

data5 = [[i, 2 * i] for i in range(1000)]  
start_time = time.time()
mnk(data5)
end_time = time.time()
assert (end_time - start_time) < 1, "5 Failed: функция выполняется слишком долго"

print("Все тесты пройдены успешно!")
