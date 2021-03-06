
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Specify the file to READ to
csvpath = os.path.join('Resources', 'budget_data.csv')

# totalmonths = []
profits = 0 

# Open the file using "write" mode. Specify the variable to hold the contents
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # csv_header = next(csvfile) #skip first row <--- DO I NEED THIS???
    for row in csvreader:
        #print(row) #this will print the csvfile

#------------ Data to pull from CSVFILE---------------   
     
        # Add total months 
        totalmonths= len(list(csvreader))

        # Add Net Total Profits 
        #csv_header = next(csvfile) -----STUCK HERE----
        #netprofits += int(row[1]) -----STUCK HERE-----

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
    #writer.writerow([f"Total: {str(netprofits)}"]) #-----STUCK HERE-----
    #print([f"Total: {str(netprofits)}"]) #-----STUCK HERE-----

    # # Write average change in profit/losses
    # writer.writerow([f"Average Change: {str(netprofits)}"])
    # print(f"Average Change: {str(netprofits)}")

    # Write greatest increase in profits (date and amount) over entire period
    #writer.writerow([f"Greatest Increase in Profits: {str(incdate)} {str(greatestincrease)"])

    # Write greatest decrease in losses (date and amount) over entire period
    #writer.writerow([f"Greatest Decrease in Profits: {str(decdate)} {str(greatestdecrease)"])


#------------------------MY CODE ABOVE HERE------------------------
