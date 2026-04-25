import matplotlib.pyplot as plt

# Sample data (salaries)
salaries = [48000, 82000, 54000, 71000, 39000, 95000, 50000, 68000, 62000, 73000]

# Create histogram
plt.hist(salaries, bins=5, color='lightcoral', edgecolor='black')

# Labels and title
plt.title("Salary Distribution")
plt.xlabel("Salary Range")
plt.ylabel("Number of People")

# Show graph
plt.show()


#scatter plot example
import matplotlib.pyplot as plt

# Sample data
ages = [26, 38, 29, 33, 24, 41, 28, 36, 31, 34]
salaries = [48000, 82000, 54000, 71000, 39000, 95000, 50000, 68000, 62000, 73000]

# Create scatter plot
plt.scatter(ages, salaries, color='lightcoral', edgecolors='green', s=100)

# Labels and title
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")

# Show plot
plt.show()

#fill between example
import matplotlib.pyplot as plt

# Months and sales data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [20000, 25000, 22000, 27000, 30000, 28000]

# Convert months to numeric positions
x = range(len(months))

# Fill area under sales line
plt.fill_between(x, sales, color='lightblue', alpha=0.5)

# Plot the sales line
plt.plot(x, sales, color='blue', marker='o')

# Labels and title
plt.title("Monthly Sales Report")
plt.xlabel("Months")
plt.ylabel("Sales")

# Show month names on x-axis
plt.xticks(x, months)

plt.show()