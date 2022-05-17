#gets data from a specific CSV file

import csv

#Default watch folder routine

with open('E:\LocalRepository\Auto-Line-Printer\ALP_WatchFolder\SampleCSV.csv', 'r') as default_watchFile: #set default file to variable
    csv_reader = csv.reader(default_watchFile) #read file to variable
    for csv_reader_line in csv_reader: #loop through csv
        print(csv_reader_line) #print to console for debugging
        read_list = [] #empty array
        for sublist in csv_reader: #loop through file, create array of elements
            for item in sublist:
                print(item)
                read_list.append(item)
print(read_list) #print the final array to console for debugging


#return(read_list)
