import matplotlib.pyplot as plt
import numpy as np

# Sample Data
x = [
    1,1,2,3,3,5,7,8,9,10, 10,11,11,13,13,15,16,17,18,18,
    18,19,20,21,21,23,24,24,25,25, 25,25,26,26,26,27,27,27,27,27,
    29,30,30,31,33,34,34,34,35,36, 36,37,37,38,38,39,40,41,41,42,
    43,44,45,45,46,47,48,48,49,50, 51,52,53,54,55,55,56,57,58,60,
    61,63,64,65,66,68,70,71,72,74, 75,77,81,83,84,87,89,90,90,91
]

# Data for Bar Chart
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 30, 40]

# Data for Pie Chart
labels = ['Apple', 'Banana', 'Cherry', 'Date']
sizes = [20, 30, 35, 15]
colors = ['red', 'yellow', 'purple', 'brown']

# Data for Box Plot
data = np.random.normal(50, 15, 100)  # Generating 100 random values


# Creating subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Histogram
axes[0, 0].hist(x, bins=10, color='blue', edgecolor='black')
axes[0, 0].set_title("Histogram")
axes[0, 0].set_xlabel("Age")
axes[0, 0].set_ylabel("Frequency")

# Box Plot
axes[0, 1].boxplot(data)
axes[0, 1].set_title("Box Plot")
axes[0, 1].set_ylabel("Values")

# Bar Chart
axes[1, 0].bar(categories, values, color=['blue', 'green', 'red', 'orange'])
axes[1, 0].set_title("Bar Chart")
axes[1, 0].set_xlabel("Categories")
axes[1, 0].set_ylabel("Values")

# Pie Chart
axes[1, 1].pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
axes[1, 1].set_title("Pie Chart")

# Adjust layout
plt.tight_layout()
plt.show()
