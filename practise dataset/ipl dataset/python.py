import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("ipl dataset/IPL2025Batters.csv")
# print(df.head())
# print(df.info())
# print(df.shape)

# print(df.isnull().sum())

# 1). top 5 batsmen in the tournament.
top5 = df.sort_values("Runs",ascending=False).head(5)
print(top5)


# 2). which player hits the most sixes.(top 5)
top_six = df.sort_values(by="6s",ascending=False).head(5)
print(top_six[["Player Name","Team","Runs","Matches","6s"]])


# 3). top 5 players bf>200 (strike rate).
qualified_players = df[df["BF"] >= 200]
top_strike = qualified_players.sort_values(by="SR",ascending=False).head(5)
print(top_strike[["Player Name","Team","Runs","Matches","SR"]])


# 4). how many players that hits century(top5).
century = df[df["100s"] > 0]
print(century[["Player Name", "Team", "100s", "HS"]].sort_values("HS", ascending=False).head(5))


# 5). which team player hits the most fours.(top 5)
top_four = df.sort_values(by="4s", ascending=False).head(5)
print(top_four[["Player Name","Team","Runs","Matches","4s"]])


# 6). team wise average.
team_avg_runs = df.groupby("Team")["Runs"].mean().reset_index().round(2)
print(team_avg_runs)


# 7). how many players who play more than 10 innings and more has than 40 AVG.(top 5)
df["Avg"] = pd.to_numeric(df["Avg"], errors="coerce")

top_inn = df[(df["Inn"] >= 10) & (df["Avg"] >= 40)]
top_inn = top_inn.sort_values(by="Avg", ascending=False).head(5)
print(top_inn[["Player Name", "Team", "Inn", "Avg", "Runs", "Matches"]])


# 8). players vs run (top 10).
top10_runs = df.sort_values("Runs", ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(data=top10_runs, x="Runs", y="Player Name", hue="Team", dodge=False)
plt.title("🏏 Top 10 Players by Runs - IPL 2025")
plt.xlabel("Total Runs")
plt.ylabel("Player Name")
plt.tight_layout()
plt.show()


# 9). team wise total sixes
team_sixes = df.groupby("Team")["6s"].sum().reset_index()
team_sixes = team_sixes.sort_values("6s",ascending=False)
print(team_sixes)


# 10). most fifties (top10).
fifties = df[df["50s"] > 0].sort_values("50s", ascending=False).head(10)
print(fifties[["Player Name", "Team", "50s"]])

sns.barplot(data=fifties, x="50s", y="Player Name", hue="Team", dodge=False)
plt.title("Top 10 Players with Most Fifties - IPL 2025")
plt.xlabel("Number of 50s")
plt.ylabel("Player")
plt.tight_layout()
plt.show()


# 11). top 5 impact player? (High SR + High Average)
df["impact_score"] = df['Avg'] * df['SR']
impact_player = df.sort_values(by="impact_score", ascending=False).head(5)
print(impact_player[['Player Name', 'Avg', 'SR', 'impact_score']])


# 12). top 5 finishers
df_filtered = df[(df['Runs'] >= 100) & (df['Inn'] >= 5)]

df_filtered['Boundary_Runs'] = df_filtered['4s'] * 4 + df_filtered['6s'] * 6
df_filtered['Boundary_Percentage'] = df_filtered['Boundary_Runs'] / df_filtered['Runs']
df_filtered['Finisher_Score'] = (df_filtered['SR'] * df_filtered['No'] * df_filtered['Boundary_Percentage']) / df_filtered['Inn']

top_5_finishers = df_filtered.sort_values(by='Finisher_Score', ascending=False).head(5)

print(top_5_finishers[['Player Name', 'Team', 'Inn', 'No', 'SR', 'Runs', 'Avg', 'Boundary_Percentage', 'Finisher_Score']])


# 13). virat vs rohit.
players = ["Virat Kohli", "Rohit Sharma"]
compare_df = df[df["Player Name"].isin(players)]
columns = ["Player Name", "Team", "Matches", "Inn", "No", "Runs", "Avg", "BF", "SR", "100s", "50s", "4s", "6s", "HS"]

print(compare_df[columns].set_index("Player Name").T)


# 14). consistency score.
df["consistency"] = (df['50s'] + df['100s'])/df["Inn"]
df["consistency"] = df["consistency"].round(3)
top_consistent = df[df["Inn"] >= 5].sort_values("consistency", ascending=False).head(10)
print(top_consistent[["Player Name", "Team", "Inn", "50s", "100s", "consistency"]])


# 15). Aggression Index (Power Hitters)
df["Aggression"] = (df["SR"] * df["6s"]) / df["Inn"]
df["Aggression"] = df["Aggression"].round(3)
top_aggression_players = df[df["Inn"] >= 5].sort_values("Aggression", ascending=False).head(10)
print(top_aggression_players[["Player Name", "Team", "Inn", "6s", "SR", "Aggression"]])