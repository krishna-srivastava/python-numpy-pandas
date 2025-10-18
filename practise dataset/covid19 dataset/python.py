import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("covid19 dataset/country_wise_latest.csv")
# print(df.head())
# print(df.isnull().sum())

# 1. Top 10 Countries with Most Confirmed Cases
top_confirmed = df.sort_values(by="Confirmed", ascending=False).head(10)
print(top_confirmed[["Country/Region","Confirmed"]])


# 2. Which country has the highest death?
death = df.sort_values(by="Deaths", ascending=False).head(10)
print(death[["Country/Region","Confirmed","Deaths","Deaths / 100 Cases"]])

plt.figure(figsize=(12,6))
sns.barplot(x="Deaths", y="Country/Region", data=death, palette="Reds_r")
plt.title("Top 10 Countries with Highest COVID-19 Deaths", fontsize=14)
plt.xlabel("Total Deaths")
plt.ylabel("Country")
plt.tight_layout()
plt.show()


# 3. Which country has the most active cases?
active_cases = df.sort_values(by="Active", ascending=False).head(10)
print(active_cases[["Country/Region","Confirmed","Deaths","Active"]])


# 4. Which WHO region has the most confirmed cases in total?
grouped = df.groupby("WHO Region")["Confirmed"].sum().sort_values(ascending=False)
print(grouped)


# 5. Plot bar chart: Top 10 countries with new cases today.
new_cases = df.sort_values(by="New cases", ascending=False).head(10)

plt.figure(figsize=(12,6))
sns.barplot(x="New cases", y="Country/Region", data=new_cases, palette="Set2")
plt.title("Top 10 countries with new cases today")
plt.tight_layout()
plt.show()


# 6. Which country has the highest recovery?
recovery = df.sort_values(by="Recovered", ascending=False).head(10)
print(recovery[["Country/Region","Confirmed","Deaths","Recovered"]])


# 7. Compare two countries (e.g., India vs USA)
india_usa = df[df["Country/Region"].isin(["India", "US"])]
comparison = india_usa[["Country/Region", "Confirmed", "Deaths", "Deaths / 100 Cases", "1 week % increase"]]
comparison = comparison.set_index("Country/Region").T
print(comparison)


# 8. Recovery Rate vs Death Rate Plot (All Countries)
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x="Recovered / 100 Cases", y="Deaths / 100 Cases", hue="WHO Region", s=100)
plt.title("Recovery Rate vs Death Rate by Country")
plt.xlabel("Recovery %")
plt.ylabel("Death %")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()



# 9. Pie Chart: Status Distribution for India
india = df[df["Country/Region"] == "India"]
values = india[["Active", "Recovered", "Deaths"]].values.flatten()
labels = ["Active", "Recovered", "Deaths"]

plt.figure(figsize=(6,6))
plt.pie(values, labels=labels, autopct='%1.1f%%', colors=["orange", "green", "red"])
plt.title("COVID-19 Status Distribution in India")
plt.show()
