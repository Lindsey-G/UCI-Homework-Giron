# Import modules
import os
import csv

# Define function Py_Poll and have voters_id, candidate as perameters:
def py_poll(voter_id, candidate):
    
    # Get total amount of votes with len funciton using voters_id
    total_votes = (len(voter_id))

    # Creat a candidate_list that appends by cadidate name
    candidate_list = candidate.append(candidate)

    # name equals name
    for name in candidate_list:
        if name == name:
        
            # Get sum of results for indivudal candidate
            results = sum(name)

            # Get percentage of votes
            percentage = (sum(results)/len(total_votes)) * 100

            # Using the results list get the max candidate as winner
            winner = max(results)

    # Print results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("--------------------------")
    print(f" {name} : {percentage} ({results})")
    print(f"Winner: {wiiner}")

poll_csv = os.path.join("..", "Resources", "election_data.csv")

candidate_list = []

# Open csv path as csv file
with open(poll_csv, 'r') as csv_file:
    # Create csv_reader from csv_file and 
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_reader)

    for row in csv_reader:
        voter_id(int(row[0]))
        candidate(row[2])

py_poll(voter_id, candidate)