import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

df=pd.read_excel('measurements2.xlsx')

print(df.shape)

df.info()

df.describe()

df.isnull().sum()

df.drop(['specials','refill liters','refill gas'],axis=1,inplace=True)

df.head(2)

mn = df.temp_inside.mean()
mn

med = df.temp_inside.median()
med

df['temp_inside']=df.temp_inside.fillna(mn)

df.isnull().sum()


df.head(5)

df[['distance','consume','speed','temp_inside',
   'temp_outside']].mean()

df[['distance','consume','speed','temp_inside',
   'temp_outside']].median()

df[['gas_type','AC','rain','sun']].mode()

df.describe()
df.head()

sns.histplot(df.distance)
sns.kdeplot(df.distance,shade=True)
sns.histplot(df.speed)
sns.kdeplot(df.speed,shade=True)

sns.histplot(df.temp_inside)
sns.kdeplot(df.temp_inside,shade=True)
sns.histplot(df.temp_outside)
sns.kdeplot(df.temp_outside,shade=True)


df.head(1)

plt.hist(df.gas_type)

plt.figure(figsize=(7,5))
df.gas_type.value_counts().plot(kind='barh')

plt.hist(df.temp_outside)

df.temp_inside.value_counts().plot(kind='barh')

plt.hist(df.temp_inside)

df.head(2)

sns.barplot(x='gas_type',y='consume',data=df)

plt.figure(figsize=(12,5))
sns.boxplot(x='temp_outside',y='consume',data=df,palette='rainbow')

df.head(2)

sns.barplot(x='gas_type',y='consume',data=df)

sns.barplot(x='AC',y='consume',data=df)

sns.barplot(x='rain',y='consume',data=df)

sns.barplot(x='sun',y='consume',data=df)

sns.heatmap(df.corr(),annot=True)

sns.pairplot(df)

df.head(2)

from sklearn.preprocessing import LabelEncoder

le=LabelEncoder()

df['gas_types']=le.fit_transform(df.gas_type)

df.drop('gas_type',axis=1,inplace=True)

df.head(2)

x=df.drop(['consume'],axis=1)
y=df.consume

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,
                                              random_state=42)

from sklearn.linear_model import LinearRegression

linear_reg=LinearRegression()

linear_reg.fit(x_train,y_train)

y_pred=linear_reg.predict(x_test)

from sklearn.metrics import mean_absolute_error,mean_squared_error

mean_absolute_error(y_test,y_pred)

mean_squared_error(y_test,y_pred)

np.sqrt(mean_squared_error(y_test,y_pred))

import pickle

pickle.dump(linear_reg,open('model.pkl','wb'))

import joblib
joblib.dump(linear_reg,'model.save')

