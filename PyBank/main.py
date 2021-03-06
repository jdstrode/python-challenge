
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
profits = 0

# Open the file using "write" mode. Specify the variable to hold the contents
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) #skip first row 

    #------------ Data to pull from CSVFILE---------------     
    for row in csvreader:
        profits += int(row[1])
        # Add total months 
        totalmonths = totalmonths + 1

        # Add Average Change in Profit/Losses
        # headerline = csvfile.next()
        # for col in row[1]:
        #     profits += int(col)
        #     netprofits = profits / totalmonths 
        #profitchange= (list(csvreader))

        # Add Greatest Increase in Profits
            # loop through row(1). 
            # change2 = 0, change1 = 0
            # Value2 = row(1) + 1.  value1 = row(1).  Value2 - Value1 = Change2
            # If change2 > change1 then change2 = change1
            # change1 then is greatest inc.  

        # Add Greatest Increase in Profits
        # Reverse of above should work for for greatest dec?

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
    writer.writerow([f"Total: {str(profits)}"]) #-----STUCK HERE-----
    print(f"Total: {str(profits)}") #-----STUCK HERE-----

    # # Write average change in profit/losses
    # writer.writerow([f"Average Change: {str(netprofits)}"])
    # print(f"Average Change: {str(netprofits)}")

    # Write greatest increase in profits (date and amount) over entire period
    #writer.writerow([f"Greatest Increase in Profits: {str(incdate)} {str(greatestincrease)"])

    # Write greatest decrease in losses (date and amount) over entire period
    #writer.writerow([f"Greatest Decrease in Profits: {str(decdate)} {str(greatestdecrease)"])


#------------------------MY CODE ABOVE HERE------------------------
