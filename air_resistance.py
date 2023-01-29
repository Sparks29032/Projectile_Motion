import math

C = 0.5  # drag
r = 0.05  # radius of ball
A = math.pi * r ** 2  # cross sectional area
p = 1.3  # density of air
m = 0.2  # mass of ball
g = 9.801  # gravity
b = C * A * p / (2 * m)  # drag coefficient

x_max = 60  # distance ball travels
fence_height = 2  # height of fence it has to clear
dt = 0.001  # precision in time

x_0 = 0  # initial x position
y_0 = 0.7  # initial y position
angle = 35 / 360 * 2 * math.pi  # initial angle shot at
v_0 = math.floor(math.sqrt(g * x_max ** 2 / (2 * math.cos(angle) * (x_max * math.sin(angle) - (fence_height - y_0) * math.cos(angle)))))  # initial speed to test with

y_final = 0
v_precision = 0.1  # precision to first decimal in v_0
while y_final < fence_height:
    v_0 += v_precision
    x = x_0  # initialize x
    y = y_0  # initialize y
    v_x = v_0 * math.cos(angle)  # initialize x velocity
    v_y = v_0 * math.sin(angle)  # initialize y velocity
    while x < x_max and y > 0:
        x += v_x * dt  # change in x
        y += v_y * dt  # change in y
        v_x += -b * v_x * math.sqrt(v_x ** 2 + v_y ** 2) * dt  # differential equation for x velocity
        v_y += -b * v_y * math.sqrt(v_x ** 2 + v_y ** 2) * dt - g * dt  # differential equation for y velocity
    y_final = y
print("Minimum Velocity: {:.1f}".format(v_0))

y_prev = -1
y_final = 0
angle_precision = 0.01  # precision in angle
while y_prev < y_final:
    y_prev = y_final
    angle += angle_precision
    x = x_0
    y = y_0
    v_x = v_0 * math.cos(angle)
    v_y = v_0 * math.sin(angle)

    while x < x_max and y > 0:
        x += v_x * dt
        y += v_y * dt

        v_x += -b * v_x * math.sqrt(v_x ** 2 + v_y ** 2) * dt
        v_y += -b * v_y * math.sqrt(v_x ** 2 + v_y ** 2) * dt - g * dt
    y_final = y
angle -= angle_precision
print("Angle Maximizing Height: {:0.1f}".format(angle * 360 / (2 * math.pi)))
print("Maximum Height: {:0.1f}".format(y_prev - fence_height))
