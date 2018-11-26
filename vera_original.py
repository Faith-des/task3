import re
import csv
import datetime


# It is possible to open a file this way, but then you have
# to remember to `tsv.close()` when you are done with it.
tsv = open('3_vera.tsv', 'r')

# This is good, but a common way to write variables in Python
# is to separate words with underscores.  So, this would become
# file_content
fileContent = tsv.read()

# This is a good approach if you have to change all occurrences of 
# some text to something else.  There is an easier way in our case
# (in the other file I sent), but this technique is good to remember
# if you'd need it in the future
fileContent = re.sub('\t', ',', fileContent)  # convert from tab to comma

# this is very good!
csv_file = open('3_vera.csv', 'w')
csv_file.write(fileContent)
csv_file.close()


# It is good to name your functions so they can easily be understood by
# people who are not familiar with your code.  This makes sense (wd=weekday),
# but it would be better to write `def weekday()` or something like that.
def wd(a):
    """This is called a docstring, and it can be helpful to include these
    with your functions to very briefly describe what they do.  They are
    optional."""
    # I am not sure about these next two lines.
    k = a.split(',')
    w = datetime.date(str(k))
    # This is a good approach, in fact I like it better than what I
    # suggested in the previous file (where I manually figured out each
    # day of the week).  Nice!
    wd = w.strftime('%A')
    return wd


# Same notes re: naming of the function
def ondo(b):
    # Since our temperatures have decimals, we will
    # want to use `float()` instead of `int()`
    netsu = int(b.rstrip('F'))
    c = (netsu-32)/1.8  # As we discussed on Skype, use . instead of ,
    return c


with open('3_vera.csv', 'r') as csvinput:
    with open('4_vera.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        alls = []
        row = next(reader)
        row.append('weekday')
        alls.append(row)

        num = 10
        for row in reader:
            row.append(num)
            alls.append(row)
            wd(row[1])
            ondo(row[2])
        writer.writerows(alls)
