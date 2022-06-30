import os
#import sys
import csv
#os.chdir(os.path.dirname(sys.argv[0]))

file_to_load = os.path.join('Resources', 'election_results.csv')
file_to_save = os.path.join('analysis', 'election_analysis.txt')

total_votes= 0

candidate_options = []

candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     file_reader = csv.reader(election_data)
     headers = next(file_reader)
        # Print each row in the CSV file.
     for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    votes_percentage = float(votes) / float(total_votes) *100
    print(f"{candidate_name}: {votes_percentage:.1f}% ({votes:,})\n")
    if (votes > winning_count) and (votes_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = votes_percentage
        winning_candidate = candidate_name
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
# 3. Print the total votes.
#print(candidate_votes)

