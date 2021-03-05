
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Specify the file to READ to
csvpath = os.path.join('Resources', 'budget_data.csv')

# totalmonths = []
# netprofits = []
netprofits = 0

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
        #profitchange= (list(csvreader))

        # Add Greatest Increase in Profits
        #greatestincrease= (list(csvreader))

        # Add Greatest Increase in Profits
        #greatestdecrease= (list(csvreader))

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

    # Write average change in profit/losses
    #writer.writerow([f"Average CHange: {str(profitchange)}"])

    # Write greatest increase in profits (date and amount) over entire period
    #writer.writerow([f"Greatest Increase in Profits: {str(incdate)} {str(greatestincrease)"])

    # Write greatest decrease in losses (date and amount) over entire period
    #writer.writerow([f"Greatest Decrease in Profits: {str(decdate)} {str(greatestdecrease)"])


#------------------------MY CODE ABOVE HERE------------------------
#-----------------------SNIPPETS BELOW-------------------------




# Your task is to create a Python script that analyzes the records to calculate each of the following:

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The average of the changes in "Profit/Losses" over the entire period

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period