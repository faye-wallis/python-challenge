import os, csv, pathlib
from statistics import mean


#set filepath using os.path.join to allow use between different operating systems
# os.chdir()
# filepath = os.path.join(".", "Resources", "budget_data.csv")
filepath = pathlib.Path(__file__).parent / 'Resources' / 'budget_data.csv'
#open csv, store header, and assign starter variables

with open(filepath, 'r') as budget_data:

    reader = csv.reader(budget_data)
    header = next(budget_data)
    rows = list(reader)
    total_months = len(rows)
    total = [sum(int(r[1]) for r in rows)][0]
    change_list = []
    increase = 0
    decrease = 0
    greatest_increase = []
    greatest_decrease = []
    
    #iterate over rows in csv, storing and evaluating profit change as it goes
    for r in range(len(rows)):
        if rows[r] != rows[-1]:
           
            current_value = int(rows[r][1])
            next_value = int(rows[r+1][1])
            current_month = rows[r][0]
            next_month = rows[r+1][0]
            change = int(next_value) - int(current_value)
            change_list.append(change)
 
            if change > increase:
                increase = change
                greatest_increase = [next_month, change]
            elif change < decrease:
                decrease = change
                greatest_decrease = [next_month, change]

    #calculate average change, store results to variable, export to text file, and print
    average_change = mean(change_list)

    results = f'''
          Financial Analysis
          ------------------------------
          Total Months: {total_months}
          Total: ${total}
          Average Change: {"{:.2f}".format(average_change)}
          Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})
          Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})
            '''
    
    output_path = filepath = pathlib.Path(__file__).parent / 'analysis.txt'
    with open(output_path, 'w') as analysis:
        analysis.write(results)

    print(results)