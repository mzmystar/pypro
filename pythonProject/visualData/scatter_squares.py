# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
x_values= range(0,100)
y_values= [x**2 for x in range(0,100)]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolors='none', s=24)
plt.xlabel("values",fontsize=14)
plt.ylabel("Squares of values",fontsize=14)
plt.title("Squares of values(0,100)",fontsize=20)
plt.savefig('scatter_squares.png',bbox_inches='tight')

