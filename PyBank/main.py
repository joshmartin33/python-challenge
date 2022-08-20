from contextlib import nullcontext
import os
import csv
from statistics import mean

        #---------setup connection with csv----------
# Set working directory to where this Python file is
os.chdir(os.path.dirname(__file__))

# Path to collect csv from the Resources folder
work_csv = os.path.join("Resources", "budget_data.csv")

# Path to collect/create txt from/to the analysis folder
work_txt = os.path.join("analysis", "results.txt")

        #-------Setup variables---------------

# Variable to keep track of entire months P/L
net_total = 0

# Variable to keep count of the number of rows
total_month_count = 0

# Variable to keep track of the previous months P/L
# to start as a null value in order to skip the first months calculation
previous_period = nullcontext

# Empty variable to capture current monthly changes in P/L
current_monthly_change = 0

# Empty list to store monthly change totals
monthly_change = []

# Variables to hold greatest increase in profits (Month and $ figure)
greatest_increase_value = 0
greatest_increase_month = ''

# Variables to hold greatest decrease in profits (Month and $ figure)
greatest_decrease_value = 0
greatest_decrease_month = ''

        #--------------extracting data from csv file------------
# Read in the CSV file
with open(work_csv, 'r') as csvfile:

    # Split the data on commas
    reader = csv.reader(csvfile, delimiter=',')

    # Skip header row
    header = next(reader)

    # Loop through the data
    for row in reader:
        
        # Adds each months P/L to the running net total
        net_total += int(row[1])

        # counts each row to give us total qty of rows/months
        total_month_count += 1

        # Checks if the previous month has a value
        # If true calculates the difference between current month value and the previous months value
        if previous_period is not nullcontext:
            # Adds to the monthly change list
            monthly_change.append(int(row[1]) - previous_period)
            # Adds to the current months change value
            current_monthly_change = (int(row[1]) - previous_period)
        
        # Sets current month value as previous month ***to be used in the next cycle of the loop***
        previous_period = int(row[1])

        # Check to see if the current change in P/L is the largest number
        # If true updates greatest values with current month changes
        if current_monthly_change > greatest_increase_value:
            greatest_increase_value = current_monthly_change
            greatest_increase_month = str(row[0])

        # Check to see if the current change in P/L is the smallest number
        # If true updates greatest values with current month changes
        if current_monthly_change < greatest_decrease_value:
            greatest_decrease_value = current_monthly_change
            greatest_decrease_month = str(row[0])

#calculate the average monthly change in P/L
average_monthly_change = mean(monthly_change)

 #--------------Displaying summary analytics------------
# Read in the txt file
with open(work_txt, "w") as txtfile:

    # Write analysis summary to the txt file
    txtfile.write("Financial Analysis")
    txtfile.write('\n')
    txtfile.write("----------------------------")
    txtfile.write('\n')
    txtfile.write(f"Total Months: {str(total_month_count)}")
    txtfile.write('\n')
    txtfile.write(f"Total: ${str(net_total)}")
    txtfile.write('\n')
    txtfile.write(f"Average Change: ${str(round(average_monthly_change, 2))}")
    txtfile.write('\n')
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${str(greatest_increase_value)})")
    txtfile.write('\n')
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${str(greatest_decrease_value)})")


# Print out summary data
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {str(total_month_count)}")
print(f"Total: ${str(net_total)}")
print(f"Average Change: ${str(round(average_monthly_change, 2))}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${str(greatest_increase_value)})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${str(greatest_decrease_value)})")