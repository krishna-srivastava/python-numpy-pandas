import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("flights")
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.shape)

# print(df.isnull().sum())

# Total passengers per year
years = df.groupby("year")["passengers"].sum()
print(years)

# Average passengers per month
monthly_avg = df.groupby("month")["passengers"].mean().round(2)
print(monthly_avg)

# Line plot (yearly trend)
sns.lineplot(x="year", y="passengers", data=df, estimator="sum")
plt.title("Total Passengers per Year")
plt.show()


