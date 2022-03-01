# -*- coding: UTF-8 -*-
from die import Die
import pygal
die1 = Die()
# results = []
# for i in range(100):
#     result = die1.roll()
#     results.append(result)
results = [die1.roll() for i in range(100)]
frequencies = [results.count(value) for value in range(1,die1.num_sides+1)]
pb = pygal.Bar()
pb.add("掷骰子", frequencies)
pb.render_to_file('die_visual.svg', dpi='24')

