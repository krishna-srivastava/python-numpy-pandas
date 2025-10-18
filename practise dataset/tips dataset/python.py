import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
# print(tips.head())
# print(tips.tail())
# print(tips.info())

# print(tips.isnull().sum())

# 1). Gender wise tipping?
pivot = pd.pivot_table(tips, values="tip", index="sex", aggfunc="sum")
print(pivot)

# 2). difference b/w smoker n no-smoker?
pivot = pd.pivot_table(tips, values="tip", index="smoker", aggfunc="sum")
print(pivot)

# 3). visualization with bar plot.
sns.barplot(x="day", y="total_bill", data=tips, estimator=sum)
plt.show()

# 4). weekday vs weekend.
tips["weekend"] = tips["day"].isin(["Sat","Sun"])

sns.barplot(x="weekend", y="total_bill", data=tips, estimator=sum, ci=None)
plt.title("Weekday vs Weekend - Revenue")
plt.show()

sns.barplot(x="weekend", y="tip", data=tips, estimator=sum, ci=None)
plt.title("Weekday vs Weekend - Tips")
plt.show()

# 5). Lunch vs Dinner.
sns.barplot(x="time", y="total_bill", data=tips, estimator=sum)
plt.show()

# 6). average tip by group size
sns.barplot(x="size", y="tip", data=tips, estimator='mean')
plt.title("Average Tip by Group Size")
plt.show()
