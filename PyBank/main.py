import os
import csv

# Define the file path
csvpath = os.path.join("Resources/budget_data.csv")

# Initialize variables to store results
total_months = 0
net_profit_loss = 0
previous_profit_loss = 0
profit_loss_changes = []
dates = []

# Read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row
    next(csvreader)

    # Iterate through rows in the CSV
    for row in csvreader:
        # Extract date and profit/loss values
        date = row[0]
        profit_loss = int(row[1])

        # Calculate total months and net profit/loss
        total_months += 1
        net_profit_loss += profit_loss

        # Calculate profit/loss change and store it
        if total_months > 1:
            profit_loss_change = profit_loss - previous_profit_loss
            profit_loss_changes.append(profit_loss_change)
            dates.append(date)

        # Update previous profit/loss
        previous_profit_loss = profit_loss

# Calculate the average profit/loss change
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Find the greatest increase and decrease in profits
greatest_increase = max(profit_loss_changes)
greatest_increase_index = profit_loss_changes.index(greatest_increase)
greatest_increase_date = dates[greatest_increase_index]
greatest_decrease = min(profit_loss_changes)
greatest_decrease_index = profit_loss_changes.index(greatest_decrease)
greatest_decrease_date = dates[greatest_decrease_index]

# Print the results
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Save the results to a text file
with open("analysis/financial_analysis.txt", "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_profit_loss}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
