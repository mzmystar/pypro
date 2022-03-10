# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
from die import Die
die1 = Die()
results = [die1.roll() for i in range(100)]
frequencies = { value:results.count(value) for value in range(1,die1.num_sides+1)}
plt.plot(frequencies.keys(),frequencies.values())
plt.savefig('scatter_die.png',bbox_inches='tight')