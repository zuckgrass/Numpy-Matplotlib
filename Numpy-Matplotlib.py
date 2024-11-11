import numpy as np

# Task 1
# Initialize two 1D arrays with random numbers
array1 = np.random.rand(10)
array2 = np.random.rand(10)

# Concatenate arrays
concatenated_array = np.concatenate((array1, array2))

# Find max, min, sum, and product
max_element = np.max(concatenated_array)
min_element = np.min(concatenated_array)
sum_elements = np.sum(concatenated_array)
product_elements = np.prod(concatenated_array)

# Print the results for task 1
print("Task 1 Results:")
print(f"Concatenated array: {concatenated_array}")
print(f"Max element: {max_element}")
print(f"Min element: {min_element}")
print(f"Sum of elements: {sum_elements}")
print(f"Product of elements: {product_elements}\n")

# Task 2
# Initialize a 1D array with 15 elements
array_15 = np.random.rand(15)

# Subtract the mean from each element and sort the array
mean_value = np.mean(array_15)
modified_array = np.sort(array_15 - mean_value)

# Print the result for task 2
print("Task 2 Results:")
print(f"Original array: {array_15}")
print(f"Mean value: {mean_value}")
print(f"Modified and sorted array: {modified_array}\n")

# Task 3
# Initialize a 1D array with 20 elements
array_20 = np.random.rand(20)

# Reshape it into a 2D array and add 10 to each element
reshaped_array = array_20.reshape(4, 5) + 10

# Print the result for task 3
print("Task 3 Results:")
print(f"Original array: {array_20}")
print(f"Reshaped and modified array:\n{reshaped_array}\n")

# Task 4: Create a 2D array with integers in the range from -15 to 15
array_2d = np.random.randint(-15, 16, (4, 6))
print("Original 2D Array:")
print(array_2d)

# Replace all negative numbers with -1 and positive numbers with 1
new_array = np.where(array_2d < 0, -1, np.where(array_2d > 0, 1, array_2d))

print("\nModified Array (negative numbers -> -1, positive numbers -> 1):")
print(new_array)

# Write the modified array to a file
with open('array_modifications.txt', 'w') as file:
    file.write("Original 2D Array:\n")
    file.write(str(array_2d) + "\n\n")
    file.write("Modified Array (negative numbers -> -1, positive numbers -> 1):\n")
    file.write(str(new_array) + "\n\n")

# Task 5: Apply functions sort(), min(), sum(), mean() to the 2D array
# Sort each row of the array
sorted_array = np.sort(array_2d, axis=1)

# Find the minimum value of the array
min_value = np.min(array_2d)

# Sum of all elements in the array
sum_value = np.sum(array_2d)

# Mean of all elements in the array
mean_value = np.mean(array_2d)

# Output results to the console
print("\nSorted Array (row-wise):")
print(sorted_array)

print("\nMinimum Value in the Array:")
print(min_value)

print("\nSum of All Elements in the Array:")
print(sum_value)

print("\nMean Value of the Array:")
print(mean_value)

# Write results to a file
with open('array_results.txt', 'w') as file:
    file.write("Sorted Array (row-wise):\n")
    file.write(str(sorted_array) + "\n\n")
    file.write("Minimum Value in the Array:\n")
    file.write(str(min_value) + "\n\n")
    file.write("Sum of All Elements in the Array:\n")
    file.write(str(sum_value) + "\n\n")
    file.write("Mean Value of the Array:\n")
    file.write(str(mean_value) + "\n")

#Task 6
import matplotlib.pyplot as plt

def increase_values(values, increment):
    return [x + increment for x in values]

# Define x values
x = list(range(0, 10))
y = increase_values(x, 2)

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='y = x + 2', color='blue', linewidth=2, marker='o')
plt.title('Linear Graph Example', fontsize=16, color='blue')
plt.xlabel('X values', fontsize=14, color='red')
plt.ylabel('Y values', fontsize=14, color='red')
plt.grid(True)
plt.legend()
plt.savefig('linear_graph.png')
plt.show()

#Task 7

# First function: Y(x) = 5 * cos(10 * x) * sin(x) / sqrt(x), for x in [0, 5]
def function_1(x):
    return 5 * np.cos(10 * x) * np.sin(x) / np.sqrt(x)

# Second function: Y(x) = cos(10 * x) * sin(3 * x) / sqrt(x), for x in [0, 10]
def function_2(x):
    return np.cos(10 * x) * np.sin(3 * x) / np.sqrt(x)

# Values for x for each function
x1 = np.linspace(0.1, 5, 400)  # Start at 0.1 to avoid division by zero
x2 = np.linspace(0.1, 10, 400)

# Calculate y values
y1 = function_1(x1)
y2 = function_2(x2)

# Create subplots
plt.figure(figsize=(12, 6))

# First subplot for the first function
plt.subplot(1, 2, 1)  # 1 row, 2 columns, first plot
plt.plot(x1, y1, color='blue', linestyle='-', marker='o', label=r'$Y(x)=5 \cdot \frac{\cos(10x) \cdot \sin(x)}{\sqrt{x}}$')
plt.title('Graph of the First Function', fontsize=14, color='blue')
plt.xlabel('x', fontsize=12)
plt.ylabel('Y(x)', fontsize=12)
plt.grid(True)  # Add grid
plt.legend()

# Second subplot for the second function
plt.subplot(1, 2, 2)  # 1 row, 2 columns, second plot
plt.plot(x2, y2, color='green', linestyle='--', marker='s', label=r'$Y(x)=\frac{\cos(10x) \cdot \sin(3x)}{\sqrt{x}}$')
plt.title('Graph of the Second Function', fontsize=14, color='green')
plt.xlabel('x', fontsize=12)
plt.ylabel('Y(x)', fontsize=12)
plt.grid(True)  # Add grid
plt.legend()

# Adjust the layout to prevent overlapping elements
plt.tight_layout()

# Save the plots to a file
plt.savefig('subplots_functions.png')

# Show the plots
plt.show()

#Task 8
x = np.linspace(-6, 6, 400)
y1 = np.abs(x)
y2 = x**3
y3 = (1/2) * x

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='y = |x|', color='blue', linestyle='-')
plt.plot(x, y2, label='y = x^3', color='green', linestyle='--')
plt.plot(x, y3, label='y = (1/2)x', color='red', linestyle=':')

plt.title('Graphs of Mathematical Functions', fontsize=16, color='blue')
plt.xlabel('X values', fontsize=14, color='red')
plt.ylabel('Y values', fontsize=14, color='red')
plt.legend(loc='lower right')
plt.grid(True)

plt.savefig('multiple_functions.pdf')
plt.show()

#Task 9
from collections import Counter
import matplotlib.pyplot as plt

# Define vowels
vowels = "AEIOUaeiou"

# Read the text from the file
filename = 'input_text.txt'
with open(filename, 'r') as file:
    text = file.read()

# Count the frequency of vowels in the text
vowel_count = Counter(letter for letter in text if letter in vowels)

# Separate the vowels and their counts
vowels_list = list(vowel_count.keys())
frequency = list(vowel_count.values())

# Plot the bar chart
plt.bar(vowels_list, frequency, color='skyblue')

# Add titles and labels
plt.title('Frequency of Vowels in the Text')
plt.xlabel('Vowels')
plt.ylabel('Frequency')

# Save the plot as a PNG file
plt.savefig('vowel_histogram.png')

# Show the plot
plt.show()

#Task 10
import matplotlib.pyplot as plt

labels = ['A', 'B', 'C']
sizes = [2310, 3145, 1520]
colors = ['gold', 'lightcoral', 'lightskyblue']

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Gross Profit of Enterprises, thousands UAH', fontsize=16)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.savefig('pie_chart.png')
plt.show()

#Task 11
# Using the same data as in the previous example
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, startangle=140, wedgeprops=dict(width=0.3))
plt.title('Gross Profit of Enterprises (Donut Chart)', fontsize=16)
plt.axis('equal')
plt.savefig('donut_chart.png')
plt.show()

#Task 12
# Data for the sales (in thousand UAH)
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
sales_A = [470, 684, 350, 806]
sales_B = [787, 586, 980, 792]
sales_C = [320, 440, 360, 400]

# Setting the positions and width for the bars
bar_width = 0.2
r1 = np.arange(len(quarters))  # positions for the first group of bars
r2 = [x + bar_width for x in r1]  # positions for the second group of bars
r3 = [x + bar_width for x in r2]  # positions for the third group of bars

#Grouped Bar Chart (Vertical)
plt.figure(figsize=(10, 6))
plt.bar(r1, sales_A, color='blue', width=bar_width, edgecolor='grey', label='Company A')
plt.bar(r2, sales_B, color='green', width=bar_width, edgecolor='grey', label='Company B')
plt.bar(r3, sales_C, color='red', width=bar_width, edgecolor='grey', label='Company C')

# Add labels and title
plt.xlabel('Quarters', fontweight='bold')
plt.ylabel('Sales (thousands UAH)', fontweight='bold')
plt.xticks([r + bar_width for r in range(len(quarters))], quarters)
plt.title('Sales Volume per Company by Quarter')

# Adding legend
plt.legend()

# Save the grouped bar chart
plt.savefig('grouped_bar_chart.png')
plt.show()

#Task 13
# Horizontal grouped histogram
plt.figure(figsize=(10, 6))
plt.barh(r1, sales_A, color='blue', height=bar_width, edgecolor='grey', label='Company A')
plt.barh(r2, sales_B, color='green', height=bar_width, edgecolor='grey', label='Company B')
plt.barh(r3, sales_C, color='red', height=bar_width, edgecolor='grey', label='Company C')

# Add labels and title
plt.ylabel('Quarters', fontweight='bold')
plt.xlabel('Sales (thousands UAH)', fontweight='bold')
plt.yticks([r + bar_width for r in range(len(quarters))], quarters)
plt.title('Sales Volume per Company by Quarter (Horizontal)')

# Adding legend
plt.legend()

# Save the horizontal grouped bar chart
plt.savefig('horizontal_grouped_bar_chart.png')
plt.show()

# 13. Stacked Bar Chart
plt.figure(figsize=(10, 6))
plt.bar(quarters, sales_A, color='blue', edgecolor='grey', label='Company A')
plt.bar(quarters, sales_B, bottom=sales_A, color='green', edgecolor='grey', label='Company B')
plt.bar(quarters, sales_C, bottom=np.array(sales_A) + np.array(sales_B), color='red', edgecolor='grey', label='Company C')

# Add labels and title
plt.xlabel('Quarters', fontweight='bold')
plt.ylabel('Sales (thousands UAH)', fontweight='bold')
plt.title('Stacked Sales Volume per Company by Quarter')

# Adding legend
plt.legend()

# Save the stacked bar chart
plt.savefig('stacked_bar_chart.png')
plt.show()
