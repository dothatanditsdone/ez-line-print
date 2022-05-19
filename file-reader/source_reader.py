#gets data from a CSV file

import csv


def watchFile (fileLoc):
    with open(fileLoc, 'r') as curFile: #set file to variable
        csv_reader = csv.reader(curFile) #read file to variable
        for csv_reader_line in csv_reader: #loop through csv
            print(csv_reader_line) #print to console for debugging
            read_list = [] #empty array
            for sublist in csv_reader: #loop through file, create array of elements
                for item in sublist:
                    print(item)
                    read_list.append(item)
    return read_list

# Set a file to be the default in case no file location is passed to the function
fileLoc = 'E:\LocalRepository\Auto-Line-Printer\ez-line-print\ALP_WatchFolder\SampleCSV.csv' #default file if nothing is passed to function
read_list = watchFile(fileLoc)


print(read_list) #print the final array to console for debugging


#return(read_list)
