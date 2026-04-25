import matplotlib.pyplot as plt # 1. Import the Matplotlib library
# 2. Create some data to plot
x = [1, 4, 3, 4, 5]
y = [1, 5, 9, 15, 25]
# 3. Create a plot
plt.plot(x, y,color='orange', linestyle='--', linewidth=2 ,marker='o') # 4. Plot the data
# 5. Add labels and title
plt.xlabel('X-axis') # 6. Label for the x-axis
plt.ylabel('Y-axis') # 7. Label for the y-axis
plt.title('Line Plot') # 8. Title for the plot
# 9. Show the plot
plt.show() # 10. Display the plot

