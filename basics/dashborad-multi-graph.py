import matplotlib.pyplot as plt

# Data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [20000, 25000, 22000, 27000, 30000, 28000]
expenses = [15000, 18000, 16000, 20000, 21000, 19000]

categories = ["Product A", "Product B", "Product C"]
market_share = [40, 35, 25]

ages = [22, 25, 28, 30, 35, 40, 45]
salary = [30000, 40000, 50000, 60000, 70000, 80000, 90000]

x = range(len(months))

# Create 2x3 dashboard
fig, axs = plt.subplots(2, 3, figsize=(15, 8))

# 1. Fill between (Sales vs Expenses)
axs[0, 0].plot(x, sales, label="Sales", color='blue')
axs[0, 0].plot(x, expenses, label="Expenses", color='red')
axs[0, 0].fill_between(x, sales, expenses, color='lightblue', alpha=0.4)
axs[0, 0].set_title("Sales vs Expenses")
axs[0, 0].set_xticks(x)
axs[0, 0].set_xticklabels(months)
axs[0, 0].legend()

# 2. Pie chart (Market Share)
axs[0, 1].pie(market_share, labels=categories, autopct='%1.1f%%', startangle=90)
axs[0, 1].set_title("Market Share")

# 3. Scatter plot (Age vs Salary)
axs[0, 2].scatter(ages, salary, color='green')
axs[0, 2].set_title("Age vs Salary")

# 4. Histogram (Sales distribution)
axs[1, 0].hist(sales, bins=5, color='purple', edgecolor='black')
axs[1, 0].set_title("Sales Distribution")

# 5. Bar chart (Monthly Sales)
axs[1, 1].bar(months, sales, color='orange')
axs[1, 1].set_title("Monthly Sales (Bar Chart)")

# Hide empty subplot
axs[1, 2].axis("off")

# Layout fix
plt.tight_layout()
plt.show()