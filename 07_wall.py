# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
for x in range(1200, 0, -100):
    for y in range(0, 1200, 50):
        x -= 50
        point_left = sd.get_point(x,y)
        point_right = sd.get_point(x+100,y+50)
        sd.rectangle(left_bottom=point_left, right_top=point_right, color=sd.COLOR_RED, width=2)

sd.pause()
