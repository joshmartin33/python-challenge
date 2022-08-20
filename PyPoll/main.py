import os
import csv

      
       #---------setup connection with csv----------
# Set working directory to where this Python file is
os.chdir(os.path.dirname(__file__))

# Path to collect csv from the Resources folder
work_csv = os.path.join("Resources", "election_data.csv")

# Path to collect/create txt from/to the analysis folder
work_txt = os.path.join("analysis", "results.txt")

        #-------Setup variables---------------

# Variable to keep track of the total votes
total_votes = 0

# Empty list to hold candidates names
list_candidates = []

# Empty list to keep track of candidate votes
candidate_vote = []

        #--------------extracting data from csv file------------
# Read in the CSV file
with open(work_csv, 'r') as csvfile:

    # Split the data on commas
    reader = csv.reader(csvfile, delimiter=',')

    # Skip header row
    header = next(reader)

    # Loop through the data
    for row in reader:
        
        # Keeps track of the total amount of votes
        total_votes += 1

        # Read in candidate name
        candidate = (str(row[2]))

        # Check if the candidate's name aready exists in the list of candidates
        # If not add name to candidate list and add value of 0 to the candidate vote list
        if candidate not in list_candidates:
            list_candidates.append(candidate)
            candidate_vote.append(0)
        
        #finding the matching index in candidate list for reference against candidate vote list
        index = list_candidates.index(candidate)

        # Add vote to the candidate vote list by finding the matching index and adding one to its value
        candidate_vote[index] += 1

# Find the highest vote count and its index
winner_index = candidate_vote.index(max(candidate_vote))

# Use winner index to pull the winners name
winnner = list_candidates[winner_index]

#--------------Displaying summary analytics------------
# Read in the txt file
with open(work_txt, "w") as txtfile:

    # Write analysis summary to the txt file
    txtfile.write("Election Results")
    txtfile.write('\n')
    txtfile.write("-------------------------")
    txtfile.write('\n')
    txtfile.write(f"Total Votes: {str(total_votes)}")
    txtfile.write('\n')
    txtfile.write("-------------------------")
    txtfile.write('\n')
    for vote_index in range(len(list_candidates)):
        candidate_name = str(list_candidates[vote_index])
        vote_count = int(candidate_vote[vote_index])
        vote_percentage = (vote_count / total_votes) * 100
        rounded_percentage = round(vote_percentage, 3)

        txtfile.write(candidate_name + ": " + str(rounded_percentage) + "% (" + str(vote_count) + ")")
        txtfile.write('\n')
    txtfile.write("-------------------------")
    txtfile.write('\n')
    txtfile.write("Winner: " + str(winnner))
    txtfile.write('\n')
    txtfile.write("-------------------------")


# Print out summary data
print("Election Results")
print("-------------------------")
print(f"Total Votes: {str(total_votes)}")
print("-------------------------")
for vote_index in range(len(list_candidates)):
    candidate_name = str(list_candidates[vote_index])
    vote_count = int(candidate_vote[vote_index])
    vote_percentage = (vote_count / total_votes) * 100
    rounded_percentage = round(vote_percentage, 3)

    print(candidate_name + ": " + str(rounded_percentage) + "% (" + str(vote_count) + ")")
print("-------------------------")
print("Winner: " + str(winnner))
print("-------------------------")