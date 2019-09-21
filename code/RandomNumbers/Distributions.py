import numpy as np
import matplotlib.pyplot as plt
import sobol_seq

plt.figure(figsize=(26,26))

plt.subplot(451)
sobol100 = sobol_seq.i4_sobol_generate(1, 100)
plt.ylabel("Sobol Sequence (Quasi-Random)")
plt.hist(sobol100, 100)
plt.title("N=100")

plt.subplot(452)
sobol500 = sobol_seq.i4_sobol_generate(1, 250)
plt.hist(sobol500, 250)
plt.title("N=250")

plt.subplot(453)
sobol1000 = sobol_seq.i4_sobol_generate(1, 1000)
plt.hist(sobol1000, 100)
plt.title("N=1000")

plt.subplot(454)
sobol2000 = sobol_seq.i4_sobol_generate(1, 2000)
plt.hist(sobol2000, 100)
plt.title("N=2000")

plt.subplot(455)
sobol5000 = sobol_seq.i4_sobol_generate(1, 5000)
plt.hist(sobol5000, 100)
plt.title("N=5000")

plt.subplot(456)
u100 = np.random.uniform(0,1,100)
plt.hist(u100, 100)
plt.ylabel("Uniform Distribution")

plt.subplot(457)
u500 = np.random.uniform(0,1,250)
plt.hist(u500, 100)

plt.subplot(458)
u1000 = np.random.uniform(0,1,1000)
plt.hist(u1000, 100)

plt.subplot(459)
u2000 = np.random.uniform(0,1,2000)
plt.hist(u2000, 100)

plt.subplot(4,5,10)
u5000 = np.random.uniform(0,1,5000)
plt.hist(u5000, 100)

plt.subplot(4,5,11)
c100 = np.random.chisquare(1,100)
plt.hist(c100)
plt.ylabel("Chi-Square Distribution")

plt.subplot(4,5,12)
c500 = np.random.chisquare(1,250)
plt.hist(c500, 100)

plt.subplot(4,5,13)
c1000 = np.random.chisquare(1,1000)
plt.hist(c1000, 100)

plt.subplot(4,5,14)
c2000 = np.random.chisquare(1,2000)
plt.hist(c2000, 100)

plt.subplot(4,5,15)
c5000 = np.random.chisquare(1,5000)
plt.hist(c5000, 100)

plt.subplot(4,5,16)
p100 = np.random.poisson(1,100)
plt.hist(p100, 20)
plt.ylabel("Poisson Distribution")

plt.subplot(4,5,17)
p500 = np.random.poisson(1,250)
plt.hist(p500, 20)

plt.subplot(4,5,18)
p1000 = np.random.poisson(1,1000)
plt.hist(p1000, 20)

plt.subplot(4,5,19)
p2000 = np.random.poisson(1,2000)
plt.hist(p2000, 20)

plt.subplot(4,5,20)
p5000 = np.random.poisson(1,5000)
plt.hist(p5000, 20)

plt.show()