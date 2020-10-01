# Import modules
import os
import csv

# set path
poll_csv = os.path.join("..", "Resources", "election_data.csv")

# list 
total_votes = 0
candidate_list = []
percentage = 0
results = []
total_votes_won = 0

# Open csv path as csv file
with open(poll_csv, 'r') as csv_file:
    # Create csv_reader from csv_file and 
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Skip header
    csv_header = next(csv_reader)

    # for row in csv_reader:
    #     votes.append(int(row[0]))
    #     candidate.append(row[2])

# Get total amount of votes 
total_votes = total_votes + 1
print(total_votes)

    # # Create loop for each row in the csv_reader
    # for rows in csv_reader:

    #     total_votes = len(candidate_name)
    #     print(total_votes)

    #     # Get total votes used += instead of total_votes = total_votes + 1
    #     # total_votes = sum(candidate_list)
    #     # print(total_votes)
        # total_votes = total_votes + 1
        # # Identify that the candidat names are in row 2 to use in if statement
        

        # # if statement to seperate candidates names from candidate list
        # if candidate_name not in candidate_list:
            
        #     # append cadidate list using the candidate name from if statement
        #     candidate_list.append(candidate_name)
        #     # candidate_list.index(candidate_list)
        #     print(candidate_list)
        
        # #     votes.append(0)

        

        # print(total_votes)
        # # print(candidate_list)    

    # for rows in candidate_list:
    #     if candidate == candidate:
    #         results = candidate
    #     break
    # candidate_list.append(candidate)

    # candidate_list.count(candidate)
    # print(candidate_list)
    # # Create a candidate_list that appends by cadidate name
    # 

    # name equals name
    # for rows in candidate:

    #     if candidate == voter_id:
    #         candidate_list = candidate
    #         candidate_list.append(candidate)
    #         print(candidate_list)
        
        # Get sum of results for indivudal candidate
            # results = (sum(name))
            # print(results)

    #         # Get percentage of votes
    #         percentage = (sum(results) / len(total_votes)) * 100

    #         # Using the results list get the max candidate as winner
    #         winner = max(results)

    # Print results
print("Election Results")
print("-------------------------")
    # print(f"Total Votes: {total_votes}")
    # print("--------------------------")
    # print(f" {name} : {percentage} ({results})")
    # print(f"Winner: {winner}")








