# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

# FIGURE OUT THE FILEPATH ON YOUR COMPUTER
csvpath = "Python_challenge/budget_data.csv"


# read in the CSV data into memory - a list of lists
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # recognizes header and skips header when reading dataset
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

#Stores rows as List(lists)
    all_rows = []
    for row in csvreader:
        #turning Profits/Losses into INT
        int_row = row
        int_row[1] = int(int_row[1])
        all_rows.append(int_row)

    print(all_rows)

 #ANALYSIS 
    #Total months in dataset
    monthtotals = print(len(all_rows))

    #sum of profits and losses
    profits = [x[1] for x in all_rows]
    profitsums = sum(profits)

    #changes(profits, greatest, and lows)
    changes = []
    for i in range(len(all_rows) - 1):
        months_profit = all_rows [i] [1]
        nextmon_profit = all_rows[i + 1][1]

        profit_difference = nextmon_profit - months_profit
        changes.append(profit_difference)
   
    #print number of changes  
    print(len(changes))  

    #Average of changes
    avgchange = sum(changes)/len(changes)
    print (avgchange)
    

    #GreatestChange
    greatest_change = max(changes)
    print(greatest_change)

    #When was the greatest change
    index = changes.index(greatest_change) + 1
    greatest_index = print(all_rows[index][0])

    #Smallest Change
    small_change = min(changes)
    print(small_change)

    #When was the smallest change
    index2 = changes.index(small_change) + 1
    smallest_index = print(all_rows[index2][0])
    

    #Summary Table of Analysis to TXT file
    sum_table_write = "pybank.txt"
    with open(sum_table_write, "w") as f:
        f.write(f"Financial Analysis:\n")
        f.write(f"___________________________\n")
        f.write(f"Total Months: {monthtotals}\n")
        f.write(f"Total: $ {profitsums}\n")
        f.write(f"Average Change: $ {avgchange}\n")
        f.write(f"Greatest Increase in Profits: {greatest_index} , (${greatest_change})\n")
        f.write(f"Greatest Decrease in Profits: {smallest_index} , (${small_change})")






