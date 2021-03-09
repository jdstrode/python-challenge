import os

# Module for reading CSV files
import csv

# Specify the file to READ to
csvpath = os.path.join('Resources', 'election_data.csv')

# Specify the file to WRITE to
output_path = os.path.join("analysis", "results2.txt")

candidates_dict = {} #credit to Mohammad TA 
candidates_perc_dict = {} #credit to Mohammad TA 
totalvotes = 0 
maxvote = 0
winner = ""

# Open the file using "write" mode. Specify the variable to hold the contents
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader) 
    for row in csvreader:

        #print(row) #this will print the csvfile

        # calculate # of rows, which is equal to value of votes
        totalvotes +=1 

        #identify column 3 to pull candidate name
        candidate = row[2] 

        # if statement to tally votes for each candidate
        if candidate in candidates_dict: #credit to Mohammad TA for this if statement structure

            candidates_dict[candidate] += 1 # if name already in dict, +1 to that candidates "vote count"
        else:
            candidates_dict[candidate] = 1 # if name not in dict, set equal to 1 to record first "vote"
        
        # set formatting and calculation for candidate percent dictionary
        candidates_perc_dict[candidate] = f"{(candidates_dict[candidate] /totalvotes * 100):.3f}%"

    # create electionresult list to house the print & outputs (I wanted to try to do this differently then how I did it with the other project)
    electionresults = []

    # place each line into the list
    electionresults.append("Election Results")
    electionresults.append("----------------------")
    electionresults.append(f"Total Votes: {str(totalvotes)}")
    electionresults.append("----------------------")

    # credit to leilazintsem for structure to loop through dictionary, determine winner, and idea to print each candidates results after each loop
    for candidate in candidates_dict: 

        # establish variables for each result needed to print: name (candidate), percent of votes(percent), and total votes(votes)
        votes = candidates_dict[candidate] 
        percent = candidates_perc_dict[candidate]
        electionresults.append(f'{candidate}: {percent} ({votes})')
        # test print(f'{candidate}: {percentage} ({votes})')
        if votes > maxvote:
            maxvote = votes
            winner = candidate 
     
    # place more lines into the list
    electionresults.append("----------------------")
    electionresults.append(f'Winner: {winner}')
    electionresults.append("----------------------")

    # loop through list and print election result to terminal
    for i in range(0, len(electionresults)):
        print(electionresults[i])

# open txtfile to write too
with open(output_path, 'w', newline='', encoding='utf8') as txtfile:
    writer = csv.writer(txtfile)
    
    # loop through list and print election result to txt file
    for i in range(0, len(electionresults)):
        writer.writerow(electionresults[i])
