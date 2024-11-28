import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
import numpy as np

df = pd.read_excel('Aufgabe_04/bev_meld.xlsx')

# 2.1

df_reg = df.sum(axis=0)[3:]
df_reg = pd.DataFrame(df_reg).reset_index()
df_reg.columns = ['years', 'bev']
df_reg = df_reg.astype({'years': 'int', 'bev': 'int'})
plt.scatter(df_reg['years'], df_reg['bev'])
plt.xlabel('Jahre')
plt.ylabel('Bevölkerung')
plt.show()

# Interpretation:
# kontinuierliches Wachstum
# wirkt relativ linear

# 2.2

model = sm.ols('bev ~ years', df_reg).fit()
print(model.summary())


prediction = model.predict(pd.DataFrame({'years': np.arange(2030, 2100)}))

plt.plot(np.arange(2030, 2100), prediction)
plt.show()

# Interpretation:
# Prognose zeigt weiterhin kontinuierliches Wachstum
# Über 1 Mio ab ca. Jahr 2090

plt.plot(np.arange(1993, 2100), df_reg['bev'].to_list() + model.predict(pd.DataFrame({'years': np.arange(2022, 2100)})).to_list())
plt.show()

# Interpretation:
# Prognose passt gut zu den Daten
# weiteres Wachstum


# 3

df_haiming = df[df['Gemeinde'] == 'Haiming']
df_haiming_reg = df_haiming.sum(axis=0)[3:].reset_index()
df_haiming_reg.columns = ['years', 'bev']
df_haiming_reg = df_haiming_reg.astype({'years': 'int', 'bev': 'int'})

model_haiming = sm.ols('bev ~ years', df_haiming_reg).fit()

prediction_haiming = model_haiming.predict(pd.DataFrame({'years': np.arange(2021, 2100)}))

plt.plot(np.arange(2021, 2100), prediction_haiming)
plt.plot(df_haiming_reg['years'], df_haiming_reg['bev'])
plt.show()

# Interpretation:
# Zackiger Verlauf der Daten
# Prognose trifft gut auf die Daten zu

# 4 

df_RE = df[df['Bezirk'] == 'RE']
df_RE_reg = df_RE.sum(axis=0)[3:].reset_index()
df_RE_reg.columns = ['years', 'bev']
df_RE_reg = df_RE_reg.astype({'years': 'int', 'bev': 'int'})

model_RE = sm.ols('bev ~ years', df_RE_reg).fit()

df_IL = df[df['Bezirk'] == 'IL']
df_IL_reg = df_IL.sum(axis=0)[3:].reset_index()
df_IL_reg.columns = ['years', 'bev']
df_IL_reg = df_IL_reg.astype({'years': 'int', 'bev': 'int'})

model_IL = sm.ols('bev ~ years', df_IL_reg).fit()


fig, axes = plt.subplots(nrows=1, ncols=2)


re_2100 = model_RE.predict(pd.DataFrame({'years': np.arange(1980, 2100)}))

il_2100 = model_IL.predict(pd.DataFrame({'years': np.arange(1980, 2100)}))

re_2100.plot(ax=axes[0], title="RE", legend=False);
df_RE_reg['bev'].plot(ax=axes[0], title="RE", legend=False)

il_2100.plot(ax=axes[1], title="IL", legend=False);
df_IL_reg['bev'].plot(ax=axes[1], title="IL", legend=False)

fig.tight_layout()
plt.show()

# Interpretation:
# RE hat stärkeres Wachstum als IL
# linerarer Verlauf bei IL, zackiger Verlauf bei RE
