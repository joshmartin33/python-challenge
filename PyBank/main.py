from contextlib import nullcontext
import os
import csv
from statistics import mean

# Set working directory to where this Python file is
os.chdir(os.path.dirname(__file__))

# Path to collect data from the Resources folder
work_csv = os.path.join("Resources", "budget_data.csv")

# Variable to keep track of the previous months P/L
previous_period = nullcontext

def csv_summary(budget_data):

    current_month = str(budget_data[0])
    current_pl = int(budget_data[1])

    if previous_period is not nullcontext:
            
    # Sets current month as previous period for use in next row calcs
    previous_period = current_pl
    

# Variable to keep count of the number of rows
total_month_count = 0

# Variable to keep track of total months P/L
net_total = 0



# Empty list to store change totals
monthly_change = []

# Create empty dictionary to hold greatest increase/decrease
greatest_increase = {"month": "","amount": ""}
greatest_decrease = {"month": "","amount": ""}

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

        # Counter to add 1 for every row loop
        total_month_count += 1

        if previous_period is not nullcontext:
            monthly_change.append(int(row[1]) - previous_period)
        
        previous_period = int(row[1])



print(total_month_count)
print(net_total)
print(mean(monthly_change))
print(max(monthly_change))
print(min(monthly_change))