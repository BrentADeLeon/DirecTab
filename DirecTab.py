#Setting all necessary imports
import os
import os.path
import pandas as pd
import time
from datetime import date as dt

#Setting a variable to specify the path
#Specify Path Here in between apostrophe marks
target_path = ('Directory/Folder Path Here')

#This command is to dig all the way down to the lowest level of the path
explore_path = os.walk(target_path)

#Setting a current date variable to add to the file name / final product
today = dt.today()
curdate = today.strftime('%m%d%y')

#Setting empty lists to store incoming data from for loop
rootdata = []
filedata = []
mod_date = []
create_date = []
file_size = []


#For loop to grab, pull, and append specified data from explore_path and then contain that info in the empty lists above
for root , dirname , files in explore_path:
    for file in files:
        try:
            mtime = time.ctime(os.path.getmtime(root + '\\' + file))
            crtime = time.ctime(os.path.getctime(root + '\\' + file))
            fsize = os.path.getsize(root + '\\' + file)
            rootdata.append(root)
            filedata.append(file)
            mod_date.append(mtime)
            create_date.append(crtime)
            file_size.append(fsize)
        except OSError:
            pass


#Converting Data to tabular data through pandas
#Grabbing List data from lines 20 - 24
directory = {'RootData': rootdata,
             'FileData': filedata,
             'CreateDate': create_date,
             'ModifiedDate': mod_date,
             'FileSize(Bytes)' : file_size
             }

#Setting up the Data Frame and the stored in variable 'df'
df = pd.DataFrame(directory, columns= ['RootData' , 'FileData' , 'CreateDate' ,'ModifiedDate' , 'FileSize(Bytes)'])

#Converts Data frame 'df' to CSV then is stored in variable 'csvconvert'
csvconvert = df.to_csv(r'Path to store csv here' + str(curdate) + '.csv' , index = False , header= True)   

#This will execute csvconvert aka The Whole Program.
print(csvconvert)
print('The file has finished processing. You can now view the file in your set path')
        

 