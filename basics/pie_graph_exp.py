#pie chart graph
import matplotlib.pyplot as plt
import pandas as pd

subjects = ['Math', 'Science', 'English', 'History', 'Art']
marks = [85, 90, 78, 92, 88]
plt.pie(marks, labels=subjects, autopct='%1.1f%%', startangle=140,shadow=True, explode=(0.1, 0.1, 0, 0.1, 0))
plt.title('Marks Distribution') 
plt.axis('equal')
plt.show()



