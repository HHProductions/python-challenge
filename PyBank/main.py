# Import the os module
import os

# Module for reading CSV files
import csv

# Establish path to file
csvpath = os.path.join('Resources', 'budget_data.csv')

#this is used to identify PnL value for first month. Dictionry looked up later.
with open(csvpath) as csvfile:
    csvreader1 = csv.reader(csvfile, delimiter=',')
    mydict = {rows[0]:rows[1] for rows in csvreader1}
  
# Used for main data analysis
with open(csvpath) as csvfile:
    csvreader2 = csv.reader(csvfile, delimiter=',')   
    csv_header = next(csvreader2)
    
    # Loop through to sum P&L and do other calculations
    Total = 0
    Linenumber = 0
    # Tracking monthly variations
    PnL_change = 0
    
    PnL_Prev = mydict["Jan-10"] # first month PnL
    Max_PnL_profit = 0
    Max_PnL_loss = 0 
    Total_monthly_change = 0
    for row in csvreader2:
        Total += int(row[1])
        Linenumber = Linenumber + 1
        PnL_change = int(row[1]) - int(PnL_Prev)
        PnL_Prev = int(row[1])
        Total_monthly_change = Total_monthly_change +PnL_change
        if PnL_change < Max_PnL_loss:
            Max_PnL_loss = PnL_change
            Loss_PnL_month = row[0]
        elif PnL_change > Max_PnL_profit:
            Max_PnL_profit = PnL_change
            Profit_PnL_month = row[0]


    #print and save results
    print("Financial Analysis\n")  
    print("----------------------------\n")
    print(f"Total Months: {Linenumber}\n")
    print(f"Total: {Total}\n")
    Average_Change = Total_monthly_change/(Linenumber - 1)
    print(f"Average Change: {round(Average_Change,2)}\n")
    print(f"Greatest Increase in Profits: {Profit_PnL_month} (${Max_PnL_profit})\n")
    print(f"Greatest Decrease in Profits: {Loss_PnL_month} (${Max_PnL_loss})\n")
 
    with open('analysis/bank_analysis.txt', 'w') as textfile:
        l1 = "Financial Analysis\n"
        l2 = "\n"
        l3 = "----------------------------\n"
        l5 = f"Total Months: {Linenumber}\n"
        l6 = f"Total: {Total}\n"
        l7 = f"Average Change: {round(Average_Change,2)}\n"
        l8 = f"Greatest Increase in Profits: {Profit_PnL_month} (${Max_PnL_profit})\n"
        l9 = f"Greatest Decrease in Profits: {Loss_PnL_month} (${Max_PnL_loss})\n"
        textfile.writelines([l1, l2, l3, l2, l5, l2, l6, l2, l7, l2, l8, l2, l9])