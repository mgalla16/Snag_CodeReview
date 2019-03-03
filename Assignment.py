import sys
import csv
print("Hello Snag!\n")
########################################################################

filename = sys.argv[1]      #grabs csv filename from command line
cols = [i.split("=")[0].lower() for i in sys.argv[2:]]      #list of columns from extra parameters
vals = [i.split("=")[1].lower() for i in sys.argv[2:]]      #list of desired values for each parameter
try:
    with open(filename, newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        headers = [i.lower() for i in next(reader)]     #grabs header row, I always assume there is a header row. It is possible to have the program accept a parameter to indicate if there is one
        keys = [headers.index(col) for col in cols]     #makes list of the index in the header row where each argument column occurs so we can check the correct location in each row
        arg_dict = dict(zip(keys, vals))        #zipped them into a dict for easy access
        successful = 0
        unsuccessful = 0
        for row in reader:
            success_flag = 1        #holds success state for the row i.e. have any of the conditions specified in the parameters failed?
            for key,value in arg_dict.items():
                if row[key].lower() != value.lower():
                    success_flag = 0
            if success_flag == 1:  #if none failed, increment the success counter and print the row
                successful += 1
                #insert code here to change what happens on success
                print(row)
            else:                   #if one or more failed increment unsuccessful counter.
                #insert code here to 
                unsuccessful += 1
        print("Successful: "+str(successful))
        print("Unsuccessful: "+str(unsuccessful))      
except Exception as e:
    print(e)

########################################################NOTES#####################################################################
#
#1. Error checking is minimal. I was able to get away with this in for this code because I know it well and could pinpoint issues
#   quickly. In production this would have to be expanded at least to account for likely breaking points
#
#2. Assumes a header row. It is quite possible to have an indicator parameter to tell the script if there is a header row. I chose
#   to exclude that for ease of use and given that parameters had column names its likely that this would be used on csvs with headers
#
#3. In real life I would just usew Pandas for this
