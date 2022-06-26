# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Assign a list to hold candidates' names.
candidate_options = []

# Create an empty dictionary to hold each candidate name and their respective vote count.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the csv file.
    for row in file_reader:

        # 2. Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match an existing candidate...
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Start tracking the vote count for the new candidate.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

    # Calculate the percentage of votes per candidate by looping through the vote counts.
    # 1. Get the candidate name.
    for candidate_name in candidate_votes:

        # 2. Find their amount of votes.
        votes = candidate_votes[candidate_name]

        # 3. Determine the percent of votes received for that candidate.
        vote_percentage = float(votes) / float(total_votes) * 100

        # 4. Print the candidate name, percentage of votes, and vote count to the terminal.
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine winning vote count and candidate
        # 1. Determine if votes are greater than the winning vote count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            # 2. If true, then set winning_count = votes and winning_percentage = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage

            # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    # Print the winning candidate summary
    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------\n")
    print(winning_candidate_summary)

# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Use the with statement to open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.

    txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")