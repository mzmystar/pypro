# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
# array = np.linspace(-20,20,5)
# print(array)

N = 8
y =np.zeros(N)
x1 = np.linspace(0, 10, N, endpoint=True)
x2 = np.linspace(0, 10, N, endpoint=False)
# plt.plot(x1,y,'o')
plt.plot(x2,y+0.5,'o')
plt.ylim([0.5,1])
plt.show()