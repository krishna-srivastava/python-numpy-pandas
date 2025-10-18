import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("titanic dataset/output.csv")
print(df.head())

print(f"how many people survive: {df["survived"].sum()}")

# # 1. Gender wise survival:
sns.barplot(x="sex", y="survived", data=df)
plt.show()

# # 2. Class wise survival
sns.barplot(x="class", y="survived", data=df)
plt.show()

# # 3. Age distribution
sns.histplot(df["age"], bins=20, kde=True)
plt.show()

# # 4. embark town vs survival
sns.barplot(x="embark_town", y="survived", data=df)
plt.show()

sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.show()

df['age_group'] = pd.cut(df['age'], bins=[0,12,18,60,100], labels=['Child','Teen','Adult','Senior'])
sns.barplot(x='age_group', y='survived', data=df)
plt.title("Survival Rate by Age Group")
plt.show()

sns.barplot(x='alone', y='survived', data=df)
plt.title("Survival Rate: Alone vs With Family")
plt.show()

sns.histplot(x="fare", hue="survived", data=df, bins=30, kde=True)
plt.title("Average Fare by Survival")
plt.show()

alone_df = df[df['alone'] == True]
total_alone = alone_df.shape[0]
survived = alone_df["survived"].sum()

print("Total alone passengers:", total_alone)
print("Alone passengers survived:", survived)