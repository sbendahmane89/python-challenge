# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0        # initialize the total months included in the dataset to 0
total_net = 0           # initialize the net total of "Profit/Losses" over the entire period to 0
# Add more variables to track other necessary financial data
monthly_changes = []    # initialize the list of net months changes
months = []             # initialize the list of months  

# Read the csv file
with open(file_to_load) as financial_data:
# Create a csv reader object
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    firstRow = next(reader)
    
   # Track the total
    total_months += 1 

    # Track the net change
    total_net += int(firstRow[1])
    
    # Track the total and net change
    previousNet = int(firstRow[1])
    # Process each row of data
    for row in reader:
         
        # Track the total
        total_months += 1 

        # Track the net change
        total_net += int(row[1])
        # Calculate the net change 
        netChange = int(row[1])-previousNet
        # Add on the list of monthly changes
        monthly_changes.append(netChange)
        
        # Add the first month that a change occurred
            # month is in index 0
        months.append(row[0]) 
        
        # Update the previous net 
        previousNet = int(row[1])
        
# Calculate the average net change across the month
averageChangePerMonth = sum(monthly_changes) / len(monthly_changes)  

greatestIncrease = [months[0], monthly_changes[0]]  # holds the month and the value of the greatest increase
greatestDecrease = [months[0], monthly_changes[0]] # holds the month and the value of the greatest decrease

# Use loop to calculate the index of the greatest and least monthly changes 
for m in range(len(monthly_changes)):
     # Calculate the greatest increase in profits (month and amount)
    if (monthly_changes[m]> greatestIncrease[1]):
        #if the value is greater than the greatest increase, that value becomes the new greatesr increase
        greatestIncrease[1] = monthly_changes[m]
        # Update the month 
        greatestIncrease[0]= months[m]
        
     # Calculate the greatest decrease in losses (month and amount)
    if (monthly_changes[m] < greatestDecrease[1]):
        # if the value is less than the greatest decrease, that value becomes the new greatesr decrease
        greatestDecrease[1] = monthly_changes[m]
        # Update the month 
        greatestDecrease[0]= months[m]

# Generate the output summary
output = (
    f"\nFinancial Analysis \n"
    f"-------------------------\n"
f"Total Months: {total_months}\n"
f"Total: ${total_net:}\n"
f"Average Change: ${averageChangePerMonth:.2f}\n"
f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]})\n"
f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]})"
)
# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
   txt_file.write(output)
