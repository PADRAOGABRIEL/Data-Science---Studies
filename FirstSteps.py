import pandas as pd
import matplotlib.pyplot as plt

file = r'F:\Downloads\Pandas x Excel.xlsx'
base = pd.read_excel(file)

print(base.dtypes,'\n')
print(base.head(6))
print(base.tail())
print(base.info())
print(base[base["Venda $"] > 800000])
base.plot.scatter(x= 'Segundos', y='Venda $')
print(base['Venda $'].mean())