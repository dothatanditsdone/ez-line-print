#gets data from a CSV file

import csv


def watchFile (fileName):
    with open(fileName, 'r') as curFile: #set file to variable
        csv_reader = csv.reader(curFile) #read file to variable
        for csv_reader_line in csv_reader: #loop through csv
            print(csv_reader_line) #print to console for debugging
            read_list = [] #empty array
            for sublist in csv_reader: #loop through file, create array of elements
                for item in sublist:
                    print(item)
                    read_list.append(item)
    return read_list

#Set a file 
fileName = 'E:\LocalRepository\Auto-Line-Printer\ALP_WatchFolder\SampleCSV.csv' #default file if nothing is passed to function
read_list = watchFile(fileName)


print(read_list) #print the final array to console for debugging


#return(read_list)
