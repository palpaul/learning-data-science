import matplotlib.pyplot as plt

# Pie chart example for IPL team wins
teams = ['MI', 'CSK', 'RCB', 'KKR', 'SRH', 'DC', 'PBKS', 'RR']
wins = [5, 4, 3, 3, 2, 2, 1, 1]  # Sample win counts
colors = ['blue', 'yellow', 'red', 'purple', 'orange', 'green', 'pink', 'brown']
plt.pie(wins, labels=teams, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('IPL Team Wins Distribution')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()