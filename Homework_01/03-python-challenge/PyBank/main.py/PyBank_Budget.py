#Import modules
import os
import csv

# Define function Py_bank and have it accept months and profit_losses as it's sole parameter
def py_bank(months, profit_losses):

    # Get total months from column 0 using len    
    total_months = (len(months))
            
    # Total amount of "Profit/Losses" over the entire period
    p_l_total = (sum(profit_losses))

    # for to index profit_losses in order to call on each value in profit_losses
    for index, i in enumerate(profit_losses):
        
        # Using if to skip the first month since we want to 
        # use that month as the second part of the equation.
        if index > 0:
            # Now that we skipped the first month we can start the equation.
            # net_total.append is so that we can seperate each value and send to net_total []
            # Identify the index in profit_losses to start at one (due to index > 0 above) 
            # and then subtract from the previous month with with profit_losses[index -1].
            net_total.append((profit_losses[index]) - ((profit_losses[index -1])))

    # Get total average of the changes in "Profit/Losses" over the entire period by sum
    #the net_total list created above and /  it by the len of that list.
    average_changes = sum(net_total) / len(net_total)

    # Greatest increase in profits and losses over the entire period
    # Using net_total list that was created to store with each change value
    # we use the max and min function to get the greatest increase and decrease amount. 
    greatest_increase = max(net_total)

    greatest_decrease = min(net_total)
    
    # Using the net_total data we can once again call on index
    # to get the max and min amounts but since we purposely skiped the first month
    # we need to add it back so that we can data matches correctly. 
    greatest_increase_month = (net_total.index(max(net_total))) + 1
    greatest_decrease_month = (net_total.index(min(net_total))) + 1

    # print all statements

    print("Financial Analysis")
    print("----------------------------------")
    print(f"Total Months: {int(total_months)}")
    print(f"Total: $ {int(p_l_total)}")
    print(f"Average Change: $ {int(average_changes)}")
    print(f"Greatest Increase in Profits: {str(months[greatest_increase_month])} ${int(max(net_total))}")
    print(f"Greatest Decrease in Profits: {str(months[greatest_decrease_month])} ${int(min(net_total))}")

#Create path to retrieve data from the Resources folder and Budget_Data csv file
budget_csv = os.path.join("..", "Resources", "Budget_Data.csv")

months = []
profit_losses = []
net_total = []

#Open csv path as csv_file
with open(budget_csv, 'r') as csv_file:
    # Create csv_reader from csv_file and seperate by coma
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Skip header
    csv_header = next(csv_reader)

    for row in csv_reader:
        months.append(row[0])
        profit_losses.append(int(row[1]))


# output_file = os.path.join("output.csv")

# with open(output_file, "w") as datafile:    

#     writer = csv.writer(datafile)

#     writer.writerows("Financial Analysis")

#     writer.writerows(0)

py_bank(months, profit_losses)
    
