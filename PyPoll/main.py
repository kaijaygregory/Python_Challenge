import os
import csv

# Define file path
csvpath = os.path.join("Resources/election_data.csv")

# Create a directory to store the vote count for each candidate
vote_count = {}

# Read the csv file to calculate the totla number of votes
total_votes = 0

# Read the csv file and calculate the total number of votes
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #skip the header row
    next(csvreader)
    
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        
        if candidate in vote_count:
            vote_count[candidate] += 1
            
        else:
            
            vote_count[candidate] = 1
            

# Find the list of candidates and calculate the percentage of votes
candidates = list(vote_count.keys())

# Define the file path to export the analysis results
output_file = "analysis/election_analysis.txt"

# Write the analysis results to the terminal and a text file
with open(output_file, "w") as text_file:
    print(f"Election Results", file=text_file)
    print(f"-------------------------", file=text_file)
    print(f"Total Votes: {total_votes}", file=text_file)
    print(f"-------------------------", file=text_file)
    
    for candidate in candidates:
        votes = vote_count[candidate]
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.2f}% ({votes})", file=text_file)
              
    print("-------------------------", file=text_file)
    
    # Determine the winner based on the number of votes
    winner = max(vote_count, key=vote_count.get)
    print(f"Winner: {winner}", file=text_file)
    print(f"-------------------------", file=text_file)
    
# Print the analysis to the terminal
with open(output_file, "r") as output:
    for line in output:
        print(line.strip())
        
