# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

def bubble(point, step):
    # point = point
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(point, radius=radius, color=sd.COLOR_ORANGE, width=2)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код
# point = sd.get_point(200, 200)
# bubble(point, 5)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код
# point_x = float(input("Введите координату х: "))
# point_y = float(input("Введите координату у: "))
# radius_step = float(input("Введите шаг: "))
# point = sd.get_point(point_x, point_y)
# bubble(point, radius_step)

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код
for x in range(100, 1100, 100):
    point = sd.get_point(x, 200)
    bubble(point, 5)

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код
# for y in range(100, 400, 100):
#     # point = sd.get_point(x, y)
#     for x in range(100, 1100, 100):
#         point = sd.get_point(x, y)
#         # color = sd.random_color()
#         bubble(point, 5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код
for _ in range(100):
    point = sd.random_point()
    color = sd.random_color()
    bubble(point, 5)

sd.pause()


