import os 
import csv

election_data_csv = os.path.join("..","Resources","election_data.csv")


####Functions for PyPoll####

def percentFinder(part, whole):
    percent = part / whole
    return percent * 100



#open the file and read it // next section of code
with open(election_data_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")

    #store the header and go next to the data
    #Ballot ID,County,Candidate (INDEX)
    csv_header = next(csvfile)

    #variables
    totalVotes = 0
    candidateName = ''
    candidateVotes = 0
    listOfVotes=[]
    previousCandidate =''


    #read through each r ow of data after the header (loop)
    for row in csv_reader:

        #keeps track of total votes cast
        totalVotes += 1


        #listing all the canidites


        candidateName = row[2]


        if previousCandidate == '':
            candidateVotes +=1
            previousCandidate = candidateName
        elif candidateName == previousCandidate:
            candidateVotes +=1        
        elif candidateName != previousCandidate:
            listOfVotes.append(previousCandidate)
            listOfVotes.append(int(candidateVotes))
            previousCandidate = candidateName
            candidateVotes = 0 
  
#Printing into terminal
print(f"\nElection Results \n --------------------")
print(f"Total Votes: {totalVotes}\n-----------------")



""" The results :(
['Charles Casper Stockham', 19723, 'Diana DeGette', 17962, 'Raymon Anthony Doane', 1168, 'Charles Casper Stockham', 57187, 'Diana DeGette', 239281, 'Raymon Anthony Doane', 9584, 'Charles Casper Stockham', 8301, 'Diana DeGette', 15646]
""" 

"""
Charles has elements: NAME0 , Vote1, NAME6 , Vote7 , NAME12 , Vote13
Diana has elements: NAME2, Vote3 , NAME8, Vote9, NAME14, Vote15
Raymon : NAME4, Vote5, NAME10 , NAME11

"""

#list manipulation
#Charles Name0 , Vote1 + Vote 7 + Vote 13
#Diana Name2, Vote3 + 9 + 15
#Raymon Name4, 5 + 11

temphold = 0

#Charles
temphold = int(listOfVotes[1]) + int(listOfVotes[7]) + int(listOfVotes[13])
listOfVotes[1] = temphold
temphold = 0

#Diana
temphold = int(listOfVotes[3]) + int(listOfVotes[9]) + int(listOfVotes[15])
listOfVotes[3] = temphold
temphold = 0

#Raymon
temphold = int(listOfVotes[5]) + int(listOfVotes[11]) 
listOfVotes[5] = temphold

del listOfVotes[6:16]


#print(listOfVotes) #Clean list with clear vote counters per 
# ['Charles Casper Stockham', 85211, 'Diana DeGette', 272889, 'Raymon Anthony Doane', 10752]

print(f"{listOfVotes[0]} : {round(percentFinder(listOfVotes[1],totalVotes),3)}% ({listOfVotes[1]})")
print(f"{listOfVotes[2]} : {round(percentFinder(listOfVotes[3],totalVotes),3)}% ({listOfVotes[3]})")
print(f"{listOfVotes[4]} : {round(percentFinder(listOfVotes[5],totalVotes),3)}% ({listOfVotes[5]})")
print("----------------")

#find winner
if listOfVotes[1] > listOfVotes[3] and listOfVotes[1] > listOfVotes[5]:
    print(f"Winner: {listOfVotes[0]}")
elif listOfVotes[3] > listOfVotes[1] and listOfVotes[3] > listOfVotes[5]:
    print(f"Winner: {listOfVotes[2]}")
else:
    print(f"Winner: {listOfVotes[4]}")

print(f"\n\nA csv file with the results has been made in this file!")


#export to a csv file 
outputPath = os.path.join("outputVoteCount.csv")


with open(outputPath, 'w') as file:

    csvWriter = csv.writer(file, delimiter = ",")

    #use writeRow function 
    csvWriter.writerow([f"Election Results \n --------------------"])
    csvWriter.writerow([f"Total Votes: {totalVotes}\n-----------------"])
    csvWriter.writerow([f"{listOfVotes[0]} : {round(percentFinder(listOfVotes[1],totalVotes),3)}% ({listOfVotes[1]})"])
    csvWriter.writerow([f"{listOfVotes[2]} : {round(percentFinder(listOfVotes[3],totalVotes),3)}% ({listOfVotes[3]})"])
    csvWriter.writerow([f"{listOfVotes[4]} : {round(percentFinder(listOfVotes[5],totalVotes),3)}% ({listOfVotes[5]})"])

    #find winner
    if listOfVotes[1] > listOfVotes[3] and listOfVotes[1] > listOfVotes[5]:
        csvWriter.writerow([f"Winner: {listOfVotes[0]}"])
    elif listOfVotes[3] > listOfVotes[1] and listOfVotes[3] > listOfVotes[5]:
        csvWriter.writerow([f"Winner: {listOfVotes[2]}"])
    else:
        csvWriter.writerow([f"Winner: {listOfVotes[4]}"])

