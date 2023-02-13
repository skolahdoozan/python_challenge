import os
import csv
import numpy as np
print(os.getcwd())
csvpath = os.path.join("PyBank", "Resources", "budget_data.csv")
with open (csvpath, encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skipping the header
    next(csvreader)
    list1 = list(csvreader)
    count = 0
    totalprofitsLosses = 0
    # Counting the net for profits and losses
    for row in list1:
        count = count + 1
        totalprofitsLosses = totalprofitsLosses + int(row[1])
    
    monthly_profits_losses_value = 0
    profits_losses_value = []
    monthly_profits_losses = []
    profits_losses_value = [int(row[1]) for row in list1]
    # Finding monthly profits/losses for each month
    for i in range(count - 1):
        monthly_profits_losses.append(profits_losses_value[i+1] - profits_losses_value[i])
    # Finding the average of the monthly profits/losses
    for row in monthly_profits_losses:
        monthly_profits_losses_value = monthly_profits_losses_value + row
    
    # Finding the requested information 
    average_profits_losses = round(monthly_profits_losses_value/(count-1), 2)
    maximum = max(monthly_profits_losses)
    minimum = min(monthly_profits_losses)
    maximum_month = list1[monthly_profits_losses.index(maximum)+1][0]
    minimum_month = list1[monthly_profits_losses.index(minimum)+1][0]
    
    # Preparing the output
    output = str((f'''          Financial Analysis
          -------------------------------------------------------
          Total Months: {count}
          Total: {totalprofitsLosses}
          Average Change: ${average_profits_losses}
          Greatest Increase in Profits: {maximum_month} (${maximum})
          Greatest Decrease in Profits: {minimum_month} (${minimum})          
          '''))
    
    print(output)
    
    savepath = os.path.join('PyBank', 'analysis.txt')
    with open(savepath, 'w') as output_file:
        output_file.write(output)
    
