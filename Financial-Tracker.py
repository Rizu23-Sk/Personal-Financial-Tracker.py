import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame to store the income data
data = pd.DataFrame(columns=['Type', 'Category', 'Amount'])

# Example: Adding a person's salary
def add_income(category, amount):
    global data
    new_entry = pd.DataFrame([{'Type': 'Income', 'Category': category, 'Amount': amount}])
    data = pd.concat([data, new_entry], ignore_index=True)

# Add a sample income entry
add_income('Salary', 100000)

# Print the data to console
print("Data:")
print(data)

# Plot the income data
def plot_income(data):
    plt.figure(figsize=(8, 6))
    data.groupby('Category').sum()['Amount'].plot(kind='bar', color='skyblue')
    plt.title('Income by Category')
    plt.xlabel('Category')
    plt.ylabel('Amount')
    plt.tight_layout()

    # Show the plot
    plt.show()

# Generate the plot
plot_income(data)
