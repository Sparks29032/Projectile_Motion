import math

x_max = 1000  # distance ball travels
fence_height = 0  # height of fence it has to clear
dt = 0.001  # precision in time
g = 9.801  # gravity
b = 0.025  # drag coefficient

x_0 = 0  # initial x position
y_0 = 0  # initial y position
v_0 = 140  # initial speed
angle = math.asin(g * x_max / v_0 ** 2) / 2  # initial angle shot at

y_prev = 0
y_final = 0
flag = True
angle_precision = 0.003  # precision in angle
while flag:
    flag = False
    y_prev = y_final
    angle += angle_precision
    x = x_0
    y = y_0
    v_x = v_0 * math.cos(angle)
    v_y = v_0 * math.sin(angle)

    while x < x_max and y >= 0:
        x += v_x * dt
        y += v_y * dt

        v_x += -b * v_x * dt
        v_y += -b * v_y * dt - g * dt

    if y < 0:
        flag = True
    y_final = y
angle -= angle_precision
print("Angle Maximizing Height: {:0.1f}".format(angle * 360 / (2 * math.pi)))
