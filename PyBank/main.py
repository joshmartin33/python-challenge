from contextlib import nullcontext
from multiprocessing import current_process
import os
import csv
from statistics import mean

        #---------setup connection with csv----------
# Set working directory to where this Python file is
os.chdir(os.path.dirname(__file__))

# Path to collect csv from the Resources folder
work_csv = os.path.join("Resources", "budget_data.csv")

        #-------Setup variables---------------

# Variable to keep track of entire months P/L
net_total = 0

# Variable to keep count of the number of rows
total_month_count = 0

# Variable to keep track of the previous months P/L
previous_period = nullcontext

# Empty variable to capture current monthly changes in P/L
current_monthly_change = 0

# Empty list to store monthly change totals
monthly_change = []

# Variable to hold greatest increase in profits (Month and $ figure)
greatest_increase_value = 0
greatest_increase_month = ''

# Variable to hold greatest decrease in profits (Month and $ figure)
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
        
        # Adds monthly P/L to month total counter
        net_total += int(row[1])

        # counts each row to give us total qty of rows/months
        total_month_count += 1

        #
        if previous_period is not nullcontext:
            monthly_change.append(int(row[1]) - previous_period)
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

# Print out summary data
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {str(total_month_count)}")
print(f"Total: ${str(net_total)}")
print(f"Average Change: ${str(round(average_monthly_change, 2))}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${str(greatest_increase_value)})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${str(greatest_decrease_value)})")