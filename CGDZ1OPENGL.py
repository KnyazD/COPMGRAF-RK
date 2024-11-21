import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import time
import psutil
import os

# Функция для построения эллипса
def draw_ellipse(a, b, num_points):
    glBegin(GL_LINE_LOOP)
    for i in range(num_points):
        angle = 2 * math.pi * i / num_points
        x = a * math.cos(angle)
        y = b * math.sin(angle)
        glVertex2f(x, y)
    glEnd()

# Функция для получения использования памяти
def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)  # В МБ

# Основная функция
def main():
    # Инициализация pygame
    pygame.init()

    # Получаем параметры эллипса от пользователя
    a = float(input("Введите длину полуоси a: "))
    b = float(input("Введите длину полуоси b: "))
    num_points = int(input("Введите количество точек для эллипса: "))

    # Увеличенные размеры окна
    width, height = 1600, 1200
    pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.OPENGL)

    # Масштабируем проекцию в зависимости от длины полуосей
    max_radius = max(a, b)
    glOrtho(-max_radius, max_radius, -max_radius, max_radius, -1, 1)

    # Замер времени и памяти перед началом рендеринга
    start_time = time.time()
    initial_memory = get_memory_usage()

    # Главный цикл
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Рисуем эллипс
        draw_ellipse(a, b, num_points)

        # Обновляем экран
        pygame.display.flip()

        # Печатаем информацию о времени и памяти через определенный интервал
        current_time = time.time() - start_time
        current_memory = get_memory_usage() - initial_memory

        # Выводим информацию каждую секунду
        if current_time >= 1.0:
            print(f"Время работы: {current_time:.2f} сек | Память: {current_memory:.2f} МБ")
            start_time = time.time()  # Сброс времени
            initial_memory = get_memory_usage()  # Сброс памяти

        pygame.time.wait(10)  # Ждем немного, чтобы не перегрузить процессор

if __name__ == "__main__":
    main()
