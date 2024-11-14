import pandas as pd
import matplotlib.pyplot as plt

# 1.3
# Lese die Datei Zeitreihe-Winter-2024011810.xlsx ein und gib die deskriptive Statistik aus.
df = pd.read_excel('Aufgabe_03/Zeitreihe-Winter-2024011810.xlsx')


base = ['Bezirk','Gemnr','Gemeinde']
years = df.columns[3:].astype(str)
base.extend('x' + years)
df.columns = base

print(df.describe())

# 2.1
# Zeitlicher Verlauf der einzelnen Jahre als Punktediagramm

years = df.columns[3:]
innsbruck = df[df['Bezirk'] == 'I'].values[0,3:]
plt.scatter(x=years, y=innsbruck, label='Innsbruck')
plt.xticks(rotation=90)
plt.show()

# Interpretation:
# steigende Touristenzahlen in Innsbruck
# Einbrüche durch Covid-19

# 2.2
# alle Gemeinden des Bezirks IM als Punktediagramm

im = df[df['Bezirk'] == 'IM']
imst = im.iloc[:,3:].sum(axis=0)
plt.plot(years, imst, label='Imst', linestyle='-')
plt.xticks(rotation=90)
plt.show()

# Interpretation:
# steigende Touristenzahlen in Imst
# Einbrüche durch Covid-19
# steigende Touristenzahlen nach Covid-19

# 3.1
# Berechne die Min, Max, Mean und Range für jede Gemeinde

df['min'] = df.iloc[:,3:].min(axis=1)
df['max'] = df.iloc[:,3:].max(axis=1)
df['mean'] = df.iloc[:,3:].mean(axis=1)
df['range'] = df['max'] - df['min']

# 3.1.1
# Standardisierung der Werte

std = (df['range'] - df['range'].mean()) / df['range'].std()

# 3.2

# Summe Touristen pro Jahr
sum = df.sum(axis=0)[3:-4]

# Summe Touristen insgesamt
total = sum.sum()

# Summe der Touristen pro Bezirk
sum_bezirk = df.groupby('Bezirk').sum().iloc[:,3:-4]
sum_bezirk = sum_bezirk.sum(axis=1)
sum_bezirk.plot.bar()
plt.show()

# Interpretation:
# Bezirk I hat die wenigsten Touristen
# Bezirk Landeck hat die meisten Touristen pro Jahr

# 4.1

df.boxplot(column='range', by='Bezirk')
plt.show()

# Interpretation:
# Bezirk I hat die geringste Spanne
# Bezirk Landeck hat die größte Spanne

# 4.2


innsbruck = df[df['Bezirk'] == 'I'].set_axis(df.columns, axis=1)

plt.bar(innsbruck.columns[3:-4], innsbruck.iloc[0,3:-4])
plt.xticks(rotation=90)
plt.show()

# Interpretation:
# steigende Touristenzahlen in Innsbruck
# Einbrüche durch Covid-19

# 5

df_bev = pd.read_excel('Aufgabe_03/bev_meld.xlsx')

base = ['Bezirk', 'Gemnr','Gemeinde']
years = df_bev.columns[3:].astype(str)
base.extend('bev' + years)
df_bev.columns = base

both = pd.merge(df, df_bev, on='Gemnr')

both = both.drop(columns=['Bezirk_y', 'Gemeinde_y'])
both = both.rename(columns={'Bezirk_x': 'Bezirk', 'Gemeinde_x': 'Gemeinde'})

# a)
both['tourist_per_bev_2018'] = both['x2018'] / both['bev2018']

# b)
tourist_per_bev_2018 = both.iloc[:,[0,1,-1]]
tourist_per_bev_2018_grouped = tourist_per_bev_2018.groupby('Bezirk').mean()['tourist_per_bev_2018']

tourist_per_bev_2018_grouped.plot.bar()
plt.show()

# Interpretation:
# Bezirk Landeck hat die meisten Touristen pro Einwohner
# Bezirk I hat die wenigsten Touristen pro Einwohner


# c)
tourist_per_bev_2018 = both.iloc[:,[0,2,-1]]

df_high = tourist_per_bev_2018.sort_values(by='tourist_per_bev_2018',ascending=False).head(10)
df_low = tourist_per_bev_2018.sort_values(by='tourist_per_bev_2018',ascending=True).head(10)

# d)

haiming = tourist_per_bev_2018[tourist_per_bev_2018['Gemeinde'].str.contains('Haiming', case=False, na=False)]
