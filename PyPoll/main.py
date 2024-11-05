# Import necessary modules (csv and os modules)
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
condidateVotes = {}
condidates = [] # list that holds condidates names in the election data

# Winning Candidate and Winning Count Tracker
winningCount = 0 # variable that holds the winning count
winningCondidate = "" # variable that holds the winning condidate

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        
        # Increment the total vote count for each row
        total_votes += 1   # same as total_Votes = total_Votes + 1
        
        # Check to see if the condidate is in the list of condidates 
        if row[2] not in condidates:
            # If the candidate is not already in the candidate list, add them
            condidates.append(row[2])
            # Add the value to the dictionary
            # Start the count at 1 for the votes
            condidateVotes[row[2]] =1
        else:
            # The condidate is in the list of condidates
            # Add a vote to the candidate's count
            condidateVotes[row[2]] += 1
     
    vote_Output = ""
            
    # Loop through the candidates to determine vote percentages and identify the winner
    for condidate in condidateVotes:
        
        # Get the vote count and calculate the percentage
        votes = condidateVotes.get(condidate)
        vote_Percentage =  (float(votes) / float(total_votes)) * 100
        
        # Print and save each candidate's vote count and percentage
        vote_Output += f"{condidate}: {vote_Percentage:.3f}% ({votes}) \n"

        # Compare the votes to the winning count 
        if votes > winningCount:
            
           # Update the winning candidate to the winning count
            winningCount = votes
            
           # Update the winning candidate 
            winningCondidate = condidate
            
           # Generate and print the winning candidate summary  
            winingCondidateOutput = f"Winner: {winningCondidate}\n-------------------------"
            
# create an output varible to hold the output
output = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes: } \n"
    f"-------------------------\n"
    f"{vote_Output}"
    f"-------------------------\n"
    f"{winingCondidateOutput}"
 )  

 # Displays the output to the console     
print(output)

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    
    # Write the output to the text file
    txt_file.write(output)
    