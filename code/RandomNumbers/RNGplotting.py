# -*- coding: utf-8 -*-
"""
@author: Rhyse Bendell
"""
import matplotlib.pyplot as plt
import random
import sobol_seq

plt.figure(figsize=(18,18))

plt.subplot(251, aspect =1)
x100 = [random.random() for x in range(100)]
y100 = [random.random() for x in range(100)]
plt.title("N=100")
plt.ylabel("Pseudo Random Number Generator")
plt.scatter(x100, y100, marker = (1,1))

plt.subplot(252, aspect =1)
x250 = [random.random() for x in range(250)]
y250 = [random.random() for x in range(250)]
plt.title("N=250")
plt.scatter(x250, y250, marker = (1,1))

plt.subplot(253, aspect =1)
x1000 = [random.random() for x in range(1000)]
y1000 = [random.random() for x in range(1000)]
plt.title("N=1000")
plt.scatter(x1000, y1000, marker = (1,1))

plt.subplot(254, aspect =1)
x2000 = [random.random() for x in range(2000)]
y2000 = [random.random() for x in range(2000)]
plt.title("N=2000")
plt.scatter(x2000, y2000, marker = (1,1))

plt.subplot(255, aspect =1)
x5000 = [random.random() for x in range(5000)]
y5000 = [random.random() for x in range(5000)]
plt.title("n=5000")
plt.scatter(x5000, y5000, marker = (1,1))

# sobol
plt.subplot(256, aspect =1)
sobol_100_x = sobol_seq.i4_sobol_generate(2, 100)
x100 = sobol_100_x[:,0]
y100 = sobol_100_x[:,1]
plt.ylabel("Quasi Random Number Generator")
plt.scatter(x100, y100, marker = (1,1))

plt.subplot(257, aspect =1)
sobol_250_x = sobol_seq.i4_sobol_generate(2, 250)
x500 = sobol_250_x[:,0]
y500 = sobol_250_x[:,1]
plt.scatter(x500, y500, marker = (1,1))

plt.subplot(258, aspect =1)
quasi_1000_x = sobol_seq.i4_sobol_generate(2, 1000)
x1000 = quasi_1000_x[:,0]
y1000 = quasi_1000_x[:,1]
plt.scatter(x1000, y1000, marker = (1,1))

plt.subplot(259, aspect =1)
sobol_2000_x = sobol_seq.i4_sobol_generate(2, 2000)
x2000 = sobol_2000_x[:,0]
y2000 = sobol_2000_x[:,1]
plt.scatter(x2000, y2000, marker = (1,1))

plt.subplot(2,5,10, aspect =1)
sobol_5000_x = sobol_seq.i4_sobol_generate(2, 5000)
x5000 = sobol_5000_x[:,0]
y5000 = sobol_5000_x[:,1]
plt.scatter(x5000, y5000, marker = (1,1))
plt.show()

