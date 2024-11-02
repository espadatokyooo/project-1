def cantor_pair(x, y):
    return (x + y) * (x + y + 1) // 2 + y

def inverse_cantor(n):
    w = int(((8 * n + 1)**0.5 - 1) // 2)
    t = n - (w * (w + 1)) // 2
    y = t
    x = w - t
    return (x, y)

x = int(input('Введите первое неотрицательное число: '))
y = int(input('Введите второе неотрицательное число: '))

if x < 0 or y < 0:
    print("Ошибка: оба числа должны быть неотрицательными.")
else:
    n = cantor_pair(x, y)
    print(f"Прямая нумерация: ({x}, {y}) -> {n}")
    
    x_inv, y_inv = inverse_cantor(n)
    print(f"Обратная нумерация: {n} -> ({x_inv}, {y_inv})")
