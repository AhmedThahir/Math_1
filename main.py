import math
import matplotlib.pyplot as plt

t = int(input("Value of t "))

# the coefficient of i will be the x term, and the coefficient of j will be y term
r0198x = math.pi * t - math.sin(math.pi * t)
r0198y = 1 - math.cos(math.pi * t)
m = math.sqrt(r0198x * r0198x + r0198y * r0198y)  # magnitude

# plotting the graph
if m != 0:  # only display plot when magnitude is not 0
    x = r0198x / m
    y = r0198y / m
    plt.arrow(0, 0, x, y, length_includes_head=True, width=0.01, head_length=0.1, head_width=0.05)

# graph styles
plt.title("Direction of position vector for t = {}".format(t))
plt.xlabel("X coordinate")
plt.ylabel("Y coordinate")
plt.style.use('presentation.mplstyle')
plt.axes().spines['bottom'].set_position(('data', 0))
plt.axes().spines['left'].set_position(('data', 0))
plt.show()





