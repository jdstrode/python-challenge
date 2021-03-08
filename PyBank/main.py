
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
greatestincrease = ["",0] #credit to classmate, Daniel Atuesta, to avoid indexerror
greatestdecrease = ["", 9999999999999] #credit to classmate, Daniel Atuesta, to avoid indexerror
netprofits = 0

# Open the file using "write" mode. Specify the variable to hold the contents
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) #skip first row 

    first_row = next(csvreader)
    totalmonths = totalmonths + 1
    netprofits = netprofits + int(first_row[1])
    previousnet = int(first_row[1])
    
    #------------ Data to pull from CSVFILE---------------     
    for row in csvreader:

        totalmonths = totalmonths + 1
        netprofits = netprofits + int(row[1])

       #7.2 Extract the net change of the sample
        netchangevalue = int(row[1]) - previousnet
        previousnet = int(row[1])
        netchange = netchange + [netchangevalue]
        monthofchange = monthofchange + [row[0]]

       # Add Greatest Increase in Profits
        if netchangevalue > greatestincrease[1]:
            greatestincrease[0] = row[0]
            greatestincrease[1] = netchangevalue
        # Add Greatest Decrease in Profits
        if netchangevalue < greatestdecrease[1]:
            greatestdecrease[0] = row[0]
            greatestdecrease [1] = netchangevalue

    # Add Average Change in Profit/Losses
    averagechange = sum(netchange)/ len(netchange)

    #------------WRITING TO OUTPUT FILE---------------

# Specify the file to WRITE to
output_path = os.path.join("analysis", "results1.txt")

# Initialize csv.writer
with open(output_path, 'w', newline='', encoding='utf8') as txtfile:
    writer = csv.writer(txtfile)

    # Write the first row (column headers)
    writer.writerow(["Financial Analysis"])
    print("Financial Analysis")

    # Write the second row
    writer.writerow(["----------------------"])
    print("----------------------")

    # Write total # of months
    writer.writerow([f"Total Months: {str(totalmonths)}"])
    print(f"Total Months: {str(totalmonths)}")

    # Write total # of profits/losses
    writer.writerow([f"Total: {str(netprofits)}"]) 
    print(f"Total: {str(netprofits)}")

    # Write average change in profit/losses
    writer.writerow([f"Average Change: ${str(averagechange)}"])
    print(f"Average Change: ${str(averagechange)}")

    # Write greatest increase in profits (date and amount) over entire period
    writer.writerow([f"Greatest Increase in Profits: {greatestincrease[0]}, (${str(greatestincrease[1])})"])
    print(f"Greatest Increase in Profits: {greatestincrease[0]}, (${str(greatestincrease[1])})")

    # Write greatest decrease in losses (date and amount) over entire period
    writer.writerow([f"Greatest Increase in Profits: {greatestdecrease[0]}, (${str(greatestdecrease[1])})"])
    print(f"Greatest Increase in Profits: {greatestdecrease[0]}, (${str(greatestdecrease[1])})")
