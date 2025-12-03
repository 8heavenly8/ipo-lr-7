def isCorrectRect(list):
    if list[0][0] >= list[1][0] or list[0][1] >= list[1][1]:
        return False
    else:
        return True
list = []
for i in range(2):
    print(f"\nВведите координаты для точки {i + 1}:")
    x_str = input(f"Введите X: ")
    y_str = input(f"Введите Y: ")
    try:
        x = float(x_str)
        y = float(y_str)
        list.append((x, y))
    except ValueError:
        print(f"Ошибка ввода! Координаты должны быть числами.")
        break

if len(list) != 0:
    print(isCorrectRect(list))
    