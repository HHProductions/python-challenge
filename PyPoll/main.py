# Import the os module
import os

# Module for reading CSV files
import csv

# establish path to file
csvpath = os.path.join('Resources', 'election_data.csv')

# open csv file

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    DataSummary = csv.reader(csvfile, delimiter=',')
    
with open(csvpath) as csvfile2:
    DataSummary2 = csv.reader(csvfile2, delimiter=',')
    next(DataSummary2)

# Create list of county and candidate
    County, Candidate = [], []
    for row in DataSummary2:
        if row[1] not in County:
            County.append(row[1])
        if row[2] not in Candidate:
            Candidate.append(row[2])
    numofcand = len(Candidate)
    candcount = []

total_cand_votes = [0]  
# loop through each candidate and results and establish how many votes are cast per candidate
for i in range(numofcand):
    if i > 0:
        total_cand_votes.append(0)

    with open(csvpath) as csvfile2:
        DataSummary3 = csv.reader(csvfile2, delimiter=',')
        next(DataSummary3)

        for row in DataSummary3:
     
            if Candidate[i] == row[2]:
               
                total_cand_votes[i] += +1

Total = sum(total_cand_votes)

# Print and save results

with open('analysis/poll_analysis.txt', 'w') as textfile:
   
    l1 = "Election Results\n"
    l2 = "\n"
    l3 = "-------------------------\n"
    l4 = f"Total Votes: {Total}\n"
    textfile.writelines([l1, l2, l3, l2, l4, l2, l3, l2])
print("Election Results")
print("")
print("-------------------------")
print("")
print(f"Total Votes: {Total}")
print("")
print("-------------------------")
print("")
# establish highest votes
Max_Votes = total_cand_votes[0]
index = 0
for k in range(numofcand):
    candscore = f"{Candidate[k]}: {total_cand_votes[k]/Total:.3%} ({total_cand_votes[k]})\n"
    with open('analysis/poll_analysis.txt', 'a') as textfile:
        textfile.writelines([candscore, l2])
    print(f"{Candidate[k]}: {total_cand_votes[k]/Total:.3%} ({total_cand_votes[k]})")
    print("")
    if total_cand_votes[k] > Max_Votes:
        Max_Votes = total_cand_votes[k]
        index = k

print("-------------------------")
print("")
winner = f"Winner: {Candidate[index]}\n"
print(f"Winner: {Candidate[index]}")
print("")
print("-------------------------")
with open('analysis/poll_analysis.txt', 'a') as textfile:
    textfile.writelines([l3, l2, winner, l2, l3, l2])

print("")
