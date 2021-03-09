
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

#csvpath = pointer to file
#csvfile = "name of file"
#csvreader = "data within file"

# Specify the file to READ to
csvpath = os.path.join('Resources', 'budget_data.csv')

totalmonths = 0
monthofchange= []
netchange= []
grtinc = ["",0] #credit to classmate, Daniel Atuesta, to avoid indexerror
grtdec = ["", 9999999999999] #credit to classmate, Daniel Atuesta, to avoid indexerror
netprofits = 0

# Open the file using "write" mode. Specify the variable to hold the contents
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) #skip first row 

    first_row = next(csvreader)
    totalmonths = totalmonths + 1
    netprofits = netprofits + int(first_row[1])
    prevnet = int(first_row[1])
    
    # loop through rows in csvreader
    for row in csvreader:

        # add 1 month for every row
        totalmonths += 1

        # add up profits (everything in second column)
        netprofits = netprofits + int(row[1])

        # save the values of all the differences from value in second column to the next value in that column into a list [netchange]
        # classmate Daniel Atuesta assisted with some of this framework
        netchangevalue = int(row[1]) - prevnet
        prevnet = int(row[1])
        netchange += [netchangevalue]
        # save the months from each difference into a similar list [monthofchange]
        monthofchange = monthofchange + [row[0]]

        # create if statement to compare netchangevalue (which is aggregated everytime we loop through table above) and save the final greatest value into greatestincrease variable
        if netchangevalue > grtinc[1]:
            grtinc[0] = row[0]
            grtinc[1] = netchangevalue
        # complete the same process as in last step, but save into greatestdecrease variable
        if netchangevalue < grtdec[1]:
            grtdec[0] = row[0]
            grtdec[1] = netchangevalue

    # use the aggregated list of netchange, sum the totals within it, and divide by its length to get the average
    avgchange = sum(netchange)/ len(netchange)

# Specify the file to WRITE to
output_path = os.path.join("analysis", "results1.txt")

# Initialize csv.writer
with open(output_path, 'w', newline='', encoding='utf8') as txtfile:
    writer = csv.writer(txtfile)

    # Write the first row (column headers)
    writer.writerow(["Financial Analysis"])
    # print to terminal
    print("Financial Analysis")

    # Write the second row
    writer.writerow(["----------------------"])
    # print to terminal
    print("----------------------")

    # Write total # of months
    writer.writerow([f"Total Months: {str(totalmonths)}"])
    # print to terminal
    print(f"Total Months: {str(totalmonths)}")

    # Write total # of profits/losses
    writer.writerow([f"Total: {str(netprofits)}"]) 
    # print to terminal
    print(f"Total: {str(netprofits)}")

    # Write average change in profit/losses
    writer.writerow([f"Average Change: ${str(avgchange)}"])
    # print to terminal
    print(f"Average Change: ${str(avgchange)}")

    # Write greatest increase in profits (date and amount) over entire period
    writer.writerow([f"Greatest Increase in Profits: {grtinc[0]} (${str(grtinc[1])})"])
    print(f"Greatest Increase in Profits: {grtinc[0]} (${str(grtinc[1])})")

    # Write greatest decrease in losses (date and amount) over entire period
    writer.writerow([f"Greatest Increase in Profits: {grtdec[0]} (${str(grtdec[1])})"])
    # print to terminal
    print(f"Greatest Increase in Profits: {grtdec[0]} (${str(grtdec[1])})")
