import re
import csv
import datetime


tsv = open('3_vera.tsv', 'r')
fileContent =  tsv.read()

fileContent = re.sub('\t', ',', fileContent) # convert from tab to comma
csv_file = open('3_vera.csv', 'w')
csv_file.write(fileContent)
csv_file.close()

# code below I found on the internet and matched for my code, 
# but I still don't completly understand how it works
# Problem: at the end (after running this code) I have an empty csv file 
# Comment: It seems I can't use breakpoint on my work PC (in Visual Code)
with open('3_vera.csv','r') as csvinput:
    with open('4_vera.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)
       
    
        # d = datetime.date(reader[1])
 
        alls = []
        row = next(reader)
        row.append('weekday')
        alls.append(row)

        num = 10  
        for row in reader:
            row.append(num)
            alls.append(row)           
        writer.writerows(alls)

            

        

        
