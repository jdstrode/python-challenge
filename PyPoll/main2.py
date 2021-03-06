import os

# Module for reading CSV files
import csv

# Specify the file to READ to
csvpath = os.path.join('Resources', 'election_data.csv')


# Open the file using "write" mode. Specify the variable to hold the contents
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # csv_header = next(csvfile) #skip first row <--- DO I NEED THIS???
    for row in csvreader:
        #print(row) #this will print the csvfile

#------------ Data to pull from CSVFILE---------------   
     
        # Add total votes 
        totalvotes= len(list(csvreader)) #does this work?

        # Add list of candidates
        # Make a candidatelist.  
        # Make candidate variable 
            # Loop through candidate column(2) and append name to list if candidate name is not already in list
        
        # Add Percentage of votes for each candidate 
            # Loop through candidate column(2) and count how many for each candidate
            # Divide by totalvotes variable and multiply by 100

        # Calculate winner variable as candidate with > count

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
#-----------------------SNIPPETS BELOW-------------------------


