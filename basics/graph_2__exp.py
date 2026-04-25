import matplotlib.pyplot as plt

import pandas as pd

x = ["student1", "student2", "student3", "student4", "student5"]
y = [60, 70, 80, 90, 100]
bars = plt.bar(x, y, color=['red', 'green', 'blue', 'orange', 'purple'], label='Marks')

for bar in bars:
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height()+1, str(bar.get_height()), ha='center', va='bottom')


plt.xlabel('Students')
plt.ylabel('Marks')
plt.title('Student Marks')
plt.legend()
plt.show()