import sys
filename = sys.argv[1]      #grabs csv filename from command line
cols = [i.split("=")[0].lower() for i in sys.argv[2:]]      #list of columns from extra parameters
vals = [i.split("=")[1].lower() for i in sys.argv[2:]]      #list of desired values for each parameter

try:
    file = open(filename, 'r')
    raw_text = file.read()
    file.close()
except FileNotFoundError as e:
    print("Could not find file '"+filename+"'")
    sys.exit(1)
lines = raw_text.strip().lower().split("\n")
lines = [line.split(",") for line in lines]
headers = lines.pop(0)
keys = [headers.index(col) for col in cols]
arg_dict = dict(zip(keys, vals))
successful = 0
unsuccessful = 0
for row in lines:
    success_flag = 1
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
