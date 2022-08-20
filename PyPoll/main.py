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

# Empty list to hold candidates
list_candidates = []

# Empty list to keep track of candidate votes
candidate_vote = []


def track_votes(candidate_votes):

    candidate = candidate_votes(str(row[2]))


    if candidate not in list_candidates:
        list_candidates.append(candidate)
    


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
        candidate = (str(row[2]))

        if candidate not in list_candidates:
            list_candidates.append(candidate)
            candidate_vote.append(0)
        
        index = list_candidates.index(candidate)

        candidate_vote[index] += 1
        #track_votes(row)

winner_index = candidate_vote.index(max(candidate_vote))
winnner = list_candidates[winner_index]


print("Election Results")
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