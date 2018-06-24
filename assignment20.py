#1.
import pandas as pd
data = {'Name':['Reena', 'Veena', 'Sony', 'Rinki'],'Age':[19,22,26,30]}
df = pd.DataFrame(data)
df.loc[4]=['Binni',20]
print(df)

#2.
import pandas as pd
df=pd.read_csv('weather.csv')
print(type(df))
df=pd.read_csv('weather.csv',header=None)
print(df)
print(df.head(10))
a=df.sum(axis=1)/ len(df.columns)
print(a)
print(df.tail(5))
X=df.iloc[:,[2]]
print(X)
b=df['MinTemp'].mean(axis=1)
print(b)



