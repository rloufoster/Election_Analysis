# Add our dependencies.

import csv
import os


# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# County options and county votes.
county_names = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Track the largest county and county voter turnout.
largest_county_turnout = ""
largest_county_vote = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    # Read the header
    header = next(reader)

    # Loop each row in the CSV file.
    for row in reader:
        # Add to the total vote count
        total_votes = total_votes + 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # If statement checks that county doesn't match any existing county in county list.
        if county_name not in county_names:
            # Add the existing county to the list of counties.
            county_names.append(county_name)

            # Begin tracking the county's vote count.
            county_votes[county_name] = 0
        # Add a vote to that county's vote count.
        county_votes[county_name] += 1
        
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"County Votes:\n")
    print(election_results, end="")
    # Save the final vote count to text file
    txt_file.write(election_results)


    #  Write a for loop to get the county from the county dictionary.
    for county in county_votes:
       # Retrieve the county vote count and percentage
        county_vote = county_votes[county]
        county_percent = int(county_vote)/int(total_votes) * 100
        county_results = (
            f"{county}: {county_percent:.1f}% ({county_vote:,})\n"
        )
        print(county_results, end="")
        txt_file.write(county_results)
        
        # Determine winning vote count
        if (county_vote > largest_county_vote):
            largest_county_vote = county_vote
            largest_county_turnout = county

    #Print the county with largest turnout 
    largest_county_turnout = (
        f"--------------------------\n"
        f"Largest County Turnout {largest_county_turnout}\n"
        f"--------------------------\n"
    )
    print(largest_county_turnout)
    txt_file.write(largest_county_turnout)

    # Save the county votes to a text file.
    for candidate in candidate_votes:
        # Retrieve vote count and percentage
        votes = candidate_votes[candidate]
        vote_percentage = int(votes)/int(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n"
            )
         
        # Print each candidate's voter count and percentage to the terminal
        print(candidate_results)
        txt_file.write(candidate_results)

        #Determine winning vote count, winning percentage, and winning candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
    )
    print(winning_candidate_summary)

    #Save winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)

    
    
        

    