#gets data from a specific CSV file

import csv

#Default watch folder routine


def watchFile (fileName):
    with open(fileName, 'r') as default_watchFile: #set default file to variable
        csv_reader = csv.reader(default_watchFile) #read file to variable
        for csv_reader_line in csv_reader: #loop through csv
            print(csv_reader_line) #print to console for debugging
            read_list = [] #empty array
            for sublist in csv_reader: #loop through file, create array of elements
                for item in sublist:
                    print(item)
                    read_list.append(item)
    return read_list


fileName = 'E:\LocalRepository\Auto-Line-Printer\ALP_WatchFolder\SampleCSV.csv'

read_list = watchFile(fileName)


print(read_list) #print the final array to console for debugging


#return(read_list)
