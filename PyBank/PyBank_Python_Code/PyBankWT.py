import os
import csv

budget_data_csv = os.path.join("..", "Resources", "budget_data.csv")


####Functions for the PyBank#########

def netTotalF(current_Month,total): #keeping a running sum of the net total
    total += current_Month
    return total


def largestChangeF(thisProfit,lastProfit, largestProfit):
    change = thisProfit - lastProfit

    if change > largestProfit:
        return change
    else:
        return largestProfit

def worstChangeF(thisProfit,lastProfit, worstProfit):
    change = thisProfit - lastProfit

    if change < worstProfit:
        return change
    else:
        return worstProfit


def averageChangeF(thisProfit,lastProfit):
    change = thisProfit - lastProfit
    return change


#open the file and read it // Next section of code main()
with open(budget_data_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter =",")

    #store the header and go next to the data
    csv_header = next(csvfile)

    #Create a Variable to store the running total and etc
    netTotal = 0
    totalMonths = 0
    lastMonth = ''
    lastProfit = 0
    largestChange = 0
    worstChange = 0
    changeTotal = 0
    runningLarge = 0
    largestMonth = ''
    runningWorst = 0
    worstMonth = ''
    averageList = []
    averageTotal = 0

    

    #read through each row of data after the header (This is where Data extraction is)
    for row in csv_reader:
        
        #create a variable for the current month 
        currentMonth = row[0]
 

        #create a variable for the current month's profit/loss
        currentProfit = int(row[1])
        

        #collecting the important data // running vital functions!!

        netTotal = netTotalF(int(row[1]),netTotal) #Calculate netTotal

        totalMonths += 1 #keep a total of months


        #section to find the largest Change + month
        largestChange = largestChangeF(currentProfit,lastProfit,largestChange)

        if largestChange > runningLarge:
            largestMonth = currentMonth
            runningLarge = largestChange
        else:
            runningLarge = largestChange


        #section to find the worst change + month
        worstChange = worstChangeF(currentProfit,lastProfit,worstChange)
        if worstChange < runningWorst:
            worstMonth = currentMonth
            runningWorst = worstChange
        else:
            runningWorst = worstChange


        averageList.append(averageChangeF(currentProfit,lastProfit)) 

        





        #resetting the loop for next itteration
        lastMonth = row[0]
        lastProfit = int(row [1])
#end of reading file


#This shows the profits/losses per month, and the following adds it and averages it to find the correct total!
#had to remove the first index because of the fact that it doesn't show change at the beg of a list
#thank you Dantrell Person :)
#print(averageList)

del averageList[0]
averageListSum = sum(averageList) / len(averageList)

#prints to terminal
print(f"Financial Analysis\n -----------------------------------")
print(f"Total Months {totalMonths}")
print(f"Total:{netTotal}")
print(f"Average Change: ${round(averageListSum,2)}")
print(f"Greatest Increase in Profits: {largestMonth} ${largestChange}")
print(f"Greatest Decrease in Profits: {worstMonth} ${worstChange}")
print("A .csv summary was made in this file!")


#prints to .txt
outputPath = os.path.join("outputFinancials.csv")


with open(outputPath, 'w') as file:

    csvWriter = csv.writer(file, delimiter = ",")

    #use writeRow function 
    csvWriter.writerow([f"Financial Analysis"])
    csvWriter.writerow(["-----------------------------------"])
    csvWriter.writerow([f"Total Months {totalMonths}"])
    csvWriter.writerow([f"Total: {netTotal}"])
    csvWriter.writerow([f"Average Change: ${round(averageListSum,2)}"])
    csvWriter.writerow([f"Greatest Increase in Profits: {largestMonth} ${largestChange}"])
    csvWriter.writerow([f"Greatest Decrease in Profits: {worstMonth} ${worstChange}"])

    