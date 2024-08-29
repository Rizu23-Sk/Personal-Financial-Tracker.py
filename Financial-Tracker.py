import pandas as pd
import matplotlib.pyplot as plt

# Initialize an empty DataFrame to store financial records
financial_data = pd.DataFrame(columns=['Type', 'Category', 'Amount'])

# Function to add a new financial entry
def add_entry(entry_type):
    global financial_data
    try:
        # Prompt user for category and amount
        category = input(f"Please enter the {entry_type.lower()} category (e.g., Salary, Rent, Savings): ").strip()
        amount = float(input(f"Enter the amount for {entry_type.lower()}: ").strip())
        
        # Create a new DataFrame for the new entry
        new_entry = pd.DataFrame([{'Type': entry_type, 'Category': category, 'Amount': amount}])
        
        # Append the new entry to the existing DataFrame
        financial_data = pd.concat([financial_data, new_entry], ignore_index=True)
        print(f"\n{entry_type} added successfully!")
    except ValueError:
        print("\nOops! That's not a valid number. Please enter a numeric value for the amount.")

# Function to visualize the financial data
def plot_financial_data():
    if financial_data.empty:
        print("\nNo data available to plot.")
    else:
        # Create a figure and axis for the plot
        plt.figure(figsize=(12, 7))
        
        # Group data by 'Type' and 'Category' and sum amounts
        grouped_data = financial_data.groupby(['Type', 'Category']).sum().unstack().fillna(0)
        
        # Plot each financial type (Income, Expense, Savings) in different colors
        for entry_type in grouped_data.columns.levels[0]:
            grouped_data[entry_type].plot(kind='bar', stacked=True, label=entry_type, ax=plt.gca())
        
        plt.title('Financial Overview: Income, Expenses, and Savings')
        plt.xlabel('Category')
        plt.ylabel('Amount')
        plt.xticks(rotation=45, ha='right')
        plt.legend(title='Type')
        plt.tight_layout()
        plt.show()

# Main function to run the program
def main():
    while True:
        print("\nWelcome to the Financial Tracker!")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Add Savings")
        print("4. View Financial Overview")
        print("5. Exit")
        
        # Get user choice from the menu
        choice = input("Select an option (1-5): ").strip()

        if choice == '1':
            add_entry('Income')
        elif choice == '2':
            add_entry('Expense')
        elif choice == '3':
            add_entry('Savings')
        elif choice == '4':
            plot_financial_data()
        elif choice == '5':
            print("\nThank you for using the Financial Tracker. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select a number between 1 and 5.")

# Execute the main function if this script is run
if __name__ == "__main__":
    main()
    
       
     

