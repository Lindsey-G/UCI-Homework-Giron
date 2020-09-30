import os
import csv

def py_poll(voter_id, candidate):
    total_votes = (len(voter_id))

    print(total_votes)

poll_csv = os.path.join("..", "Resources", "election_data.csv")

voter_id = []
with open(poll_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_reader)

    for row in csv_reader:
        voter_id(int(row[0]))

py_poll(voter_id, candidate)