
import matplotlib.pyplot as plt
x = []
y = []
f = open("D:\week1_edit.txt", 'r')
n = 0
for line in f:
    x.append(n)
    n += 1
    y.append(row)

plt.plot(x, y)
plt.show
