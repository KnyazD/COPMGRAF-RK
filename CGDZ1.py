import matplotlib.pyplot as plt
import time
import psutil
import os

# Функция для получения использования памяти
def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)  # В МБ

def draw_ellipse(x_center, y_center, a, b, max_points):
    points_list = []

    x = 0
    y = b
    a_squared = a * a
    b_squared = b * b
    a_squared_2 = 2 * a_squared
    b_squared_2 = 2 * b_squared

    # Первая половина эллипса
    p = round(b_squared - (a_squared * b) + (0.25 * a_squared))
    while (a_squared * y > b_squared * x):
        points_list.append((x_center + x, y_center + y))
        points_list.append((x_center - x, y_center + y))
        points_list.append((x_center + x, y_center - y))
        points_list.append((x_center - x, y_center - y))
        
        x += 1
        if len(points_list) >= max_points:  # Проверка на количество точек
            break
        if p < 0:
            p += b_squared_2 * x + b_squared
        else:
            y -= 1
            p += b_squared_2 * x - a_squared_2 * y + b_squared

    # Вторая половина эллипса
    p = round(b_squared * (x + 0.5) * (x + 0.5) + a_squared * (y - 1) * (y - 1) - a_squared * b_squared)
    while (y >= 0):
        points_list.append((x_center + x, y_center + y))
        points_list.append((x_center - x, y_center + y))
        points_list.append((x_center + x, y_center - y))
        points_list.append((x_center - x, y_center - y))
        
        y -= 1
        if len(points_list) >= max_points:  # Проверка на количество точек
            break
        if p > 0:
            p += a_squared - a_squared_2 * y
        else:
            x += 1
            p += b_squared_2 * x - a_squared_2 * y + a_squared

    return points_list  # Возвращаем все точки

def main():
    # Ввод данных
    a = int(input("Введите длину полуоси по оси X (a): "))
    b = int(input("Введите длину полуоси по оси Y (b): "))
    num_points = int(input("Введите количество точек для отображения (например, 1000 или больше): "))

    # Замер времени и памяти перед началом рендеринга
    start_time = time.time()
    initial_memory = get_memory_usage()

    # Генерация точек эллипса
    points = draw_ellipse(0, 0, a, b, num_points)

    # Замер времени и памяти после выполнения
    end_time = time.time()
    end_memory = get_memory_usage()

    # Вывод времени и использования памяти
    elapsed_time = end_time - start_time
    memory_used = end_memory - initial_memory

    print(f"Время выполнения: {elapsed_time:.4f} секунд")
    print(f"Использование памяти: {memory_used:.4f} МБ")

    # Отображение результата
    plt.figure(figsize=(6, 6))
    for point in points:
        plt.plot(point[0], point[1], 'bo', markersize=1)  # Рисуем точки эллипса
    # Устанавливаем границы осей с учетом размеров эллипса
    plt.xlim(-a - 10, a + 10)
    plt.ylim(-b - 10, b + 10)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(f'Ellipse (a={a}, b={b}) using Bresenham\'s Algorithm')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
