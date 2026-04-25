import matplotlib.pyplot as plt
import pandas as pd
# 
df  = pd.read_csv("Graph_data.csv")
plt.plot(df["x"], df["y"], color='orange', linestyle='--', linewidth=2 ,marker='o')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')
plt.show()

# bar graph exaple for runs and overs 
df  = pd.read_csv("cricket_data.csv")
plt.bar(df["Over"], df["Runs"], color='lightblue', label='Runs')
plt.bar(df["Over"], df["Wickets"], bottom=df["Runs"], color='lightcoral', alpha=0.7, label='Wickets')
# Add circles for each wicket
for index, row in df.iterrows():
    if row["Wickets"] > 0:
        for i in range(int(row["Wickets"])):
            plt.scatter(row["Over"], row["Runs"] + i + 1, marker='o', color='black', s=100)
plt.xticks(range(1, 21))
plt.xlabel('Overs')
plt.ylabel('Runs / Wickets')
plt.title('Runs and Wickets vs Overs')
plt.legend()

plt.show()

