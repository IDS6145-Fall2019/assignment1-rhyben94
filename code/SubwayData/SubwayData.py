import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("MTASubwayRidershipAtaGlance.csv", index_col = "Year")

day_stds = data.std(axis=0)
day_means = data.mean(axis=0)
year_stds = data.std(axis=1)
year_means = data.mean(axis=1)

day_means.plot(kind = 'line')
plt.title('Means by Day')
plt.xlabel('Day')
plt.ylabel('Mean')
plt.savefig('MeansByDay.png')
plt.show()

year_means.plot(kind = 'line')
plt.title('Means by Year')
plt.xlabel('Year')
plt.ylabel('Mean')
plt.savefig('MeansByYear.png')
plt.show()

year_stds.plot(kind = 'line')
plt.title('Standard Deviations by Year')
plt.xlabel('Year')
plt.ylabel('Standard Dev')
plt.savefig('StandardDevsByYear.png')
plt.show()

day_stds.plot(kind = 'line')
plt.title('Standard Deviations by Day')
plt.xlabel('Day')
plt.ylabel('Standard Dev')
plt.savefig('StandardDevsByDay.png')
plt.show()

data.plot(kind = 'line')
plt.title('Average Ridership: Weekday vs Weekend')
plt.xlabel('Year')
plt.ylabel('Ridership Average')
plt.savefig('RidershipByDayandYear.png')
plt.show()








