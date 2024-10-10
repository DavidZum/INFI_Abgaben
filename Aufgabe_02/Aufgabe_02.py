import numpy as np
from matplotlib import pyplot as plt

d = np.genfromtxt('Aufgabe_02/london_weather.csv', delimiter=",", skip_header=1)

dt =  d[:,0]
day = (dt % 100).astype('i')
month = (dt % 10000 / 100).astype('i')
year = (dt % 100000000 / 10000).astype('i')

temperature = d[:, 5]

temp1980 = temperature[year == 1980]
temp1990 = temperature[year == 1990]
temp2000 = temperature[year == 2000]
temp2010 = temperature[year == 2010]

# 1.1

plt.boxplot([temp1980, temp1990, temp2000, temp2010])
plt.xticks([1, 2, 3, 4], ['1980', '1990', '2000', '2010'])
plt.ylabel('Temperature')
plt.show()

# 1.2

plt.scatter(day[year == 1980], temp1980)
plt.show()

# 1.3

low1980 = np.quantile(temp1980, 0.05)
high1980 = np.quantile(temp1980, 0.95)
low2010 = np.quantile(temp2010, 0.05)
high2010 = np.quantile(temp2010, 0.95)

print(f'1980: {low1980} - {high1980}')
print(f'2020: {low2010} - {high2010}')

# 1.4

for i in range(2010, 2021):
    temp = temperature[year == i]
    middle = np.median(temp)
    plt.bar(i, middle, color='blue')

plt.show()

# 1.5
# Durchschnittliche Temperatur pro Monat im Jahr 2010

for i in range(1, 13):
    temp = temperature[(year == 2010) & (month == i)]
    middle = np.median(temp)
    plt.bar(i, middle, color='blue')

plt.show()