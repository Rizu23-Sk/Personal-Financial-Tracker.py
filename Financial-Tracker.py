import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame to store the financial data
data = pd.DataFrame(columns=['Type', 'Category', 'Amount'])

# Function to add an entry (either income or expense)
def add_entry(entry_type):
    global data
    try:
        category = input(f"Enter {entry_type.lower()} category (e.g., Salary, Rent, etc.): ").strip()
        amount = float(input(f"Enter the amount: ").strip())
        new_entry = pd.DataFrame([{'Type': entry_type, 'Category': category, 'Amount': amount}])
        data = pd.concat([data, new_entry], ignore_index=True)
        print(f"\n{entry_type} entry added successfully!")
    except ValueError:
        print("\nInvalid input! Please enter a valid number for the amount.")

# Function to plot income and expenses
def plot_financial_data():
    if data.empty:
        print("\nNo data to plot.")
    else:
        plt.figure(figsize=(10, 6))
        grouped_data = data.groupby(['Type', 'Category']).sum().unstack().fillna(0)
        grouped_data.plot(kind='bar', stacked=True, color=['skyblue', 'lightcoral'], ax=plt.gca())
        plt.title('Income and Expenses by Category')
        plt.xlabel('Type')
        plt.ylabel('Amount')
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.show()

# Main loop
def main():
    while True:
        print("\nMenu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Plot Income and Expenses")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            add_entry('Income')
        elif choice == '2':
            add_entry('Expense')
        elif choice == '3':
            plot_financial_data()
        elif choice == '4':
            print("\nExiting the program. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()

