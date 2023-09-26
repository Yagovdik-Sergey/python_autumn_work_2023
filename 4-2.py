order_of_matrix = int(input())
# Создаем матрицу порядка order_of_matrix
matrix = [None] * order_of_matrix
for i in range(order_of_matrix):
    matrix[i] = [None] * order_of_matrix
# Задаем начальные условия движения по матрице. Начинаем движение вправо на 1
x = 0
y = 0
dx = 1
dy = 0
# Двигаемся по матрице
for i in range(order_of_matrix * order_of_matrix):
    matrix[y][x] = i + 1
    # Вводим переменную для проверки выхода координаты за пределы матрицы
    test = x + dx if dx else y + dy
    # Проверка выхода координаты за пределы матрицы
    if test < 0 or test == order_of_matrix or matrix[y + dy][x + dx] != None:
        # Меняем направление
        dx, dy = -dy, dx
    x += dx
    y += dy
# Выводим получившийся результат
for y in range(order_of_matrix):
    print(matrix[y])

