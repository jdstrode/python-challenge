import os

# Module for reading CSV files
import csv

# Specify the file to READ to
csvpath = os.path.join('Resources', 'election_data.csv')

candidates_dict = {} #credit to Mohammad TA 
candidates_perc_dict = {} #credit to Mohammad TA 
totalvotes = 0 

# Open the file using "write" mode. Specify the variable to hold the contents
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader) 
    for row in csvreader:
        #print(row) #this will print the csvfile
        totalvotes +=1 #add number of rows

        candidate = row[2] #identify column 3 as variable

        if candidate in candidates_dict: #credit to Mohammad TA 
            candidates_dict[candidate] += 1 #if name already in dict, +1 to that candidates "vote count"
        else:
            candidates_dict[candidate] = 1 #if name not in dict, set equal to 1 to record first "vote"

        candidates_perc_dict[candidate] = f"{round(candidates_dict[candidate] /totalvotes * 100):.2f}%"


print(f"total_votes :: {totalvotes}")
print(f"candidates_dict :: {candidates_dict[candidate]}")
print(f"candidates_perc_dict :: {candidates_perc_dict}")



#------------WRITING TO OUTPUT FILE---------------

# Specify the file to WRITE to
output_path = os.path.join("analysis", "results2.txt")

# Initialize csv.writer
with open(output_path, 'w', newline='', encoding='utf8') as txtfile:
    writer = csv.writer(txtfile)

    # Write the first row (column headers)
    writer.writerow(["Election Results"])
    print("Election Results")

    # Write the second row
    writer.writerow(["----------------------"])
    print("----------------------")

    # Write total # of months
    writer.writerow([f"Total Votes: {str(totalvotes)}"])
    print(f"Total Votes: {str(totalvotes)}")

    # Write the fourth row
    writer.writerow(["----------------------"])
    print("----------------------")

    # Write total # of votes for each candidate in candidate dictionary
    #writer.writerow([f"Total: {str(netprofits)}"]) 
    #print(f"Khan: ({candidates_perc_dict["Khan"]})")

#     # # Write average change in profit/losses
#     # writer.writerow([f"Average Change: {str(netprofits)}"])
#     # print(f"Average Change: {str(netprofits)}")

#     # Write greatest increase in profits (date and amount) over entire period
#     #writer.writerow([f"Greatest Increase in Profits: {str(incdate)} {str(greatestincrease)"])

#     # Write greatest decrease in losses (date and amount) over entire period
#     #writer.writerow([f"Greatest Decrease in Profits: {str(decdate)} {str(greatestdecrease)"])


# #------------------------MY CODE ABOVE HERE------------------------
# #-----------------------SNIPPETS BELOW-------------------------


