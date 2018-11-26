import datetime

def f_to_c(f):
    # We expect a string like '56.3F', but to
    # convert this to celsius we'll need to do
    # some calculations and that will require 
    # we convert this string to a float (a number
    # with decimals).
    
    # strip the 'F' from the end
    f = f.rstrip('F')
    # Convert to a float
    f = float(f)
    # Calculate celsius
    c = (f-32) / 1.8
    return c


def date_to_weekday_name(date):
    # `weekday()` returns Monday as 0 and Sunday as 6
    # Convert the `date` string to a Python date
    # We do this using the `strptime` function which parses
    # a string into a date.  We provide the data '%Y-%m-%d' to 
    # describe how the string looks.  In this case, it is a four
    # digit year, two digit month, and two digit day all separated
    # by dashes.
    python_date = datetime.datetime.strptime(date, '%Y-%m-%d')
    weekday = python_date.weekday()
    if weekday == 0:
        return 'Mon'
    elif weekday == 1:
        return 'Tue'
    elif weekday == 2:
        return 'Wed'
    elif weekday == 3:
        return 'Thu'
    elif weekday == 4:
        return 'Fri'
    elif weekday == 5:
        return 'Sat'
    elif weekday == 6:
        return 'Sun'


# It is possible to `tsv = open('3_vera.tsv', 'r')`, but by doing
# it this way (within a `with` block), we get the benefit of Python
# automatically closing the file as soon our close exits the `with` 
# block (i.e., we don't have to call `.close()` on the file)
with open('3_vera.tsv') as f:
    # We will use the function `enumerate` to add a counter for every
    # time it returns data.  Since we will get data for each line, this
    # counter will return the line number.  In Python, we start counting 
    # at zero, so our first line will be zero.
    for line_number, line_data in enumerate(f):
        # We have a file header for our TSV file (names for each of our
        # "columns").  You can use this in your code, but for this simple
        # program we will also ignore it.  We will do this by skipping
        # the first line
        if line_number == 0:
            # If you uncomment the next two lines you will see the file
            # header before it skips it:
            # print('File Header:')
            # print(line_data)
            # `continue` causes the program to immediately start the next
            # cycle of the `for` loop, so in this case we move immediately
            # to the next line.
            continue
        # Previously with a CSV file we `split` on ',', so with a TSV file
        # we only have to change this character from a comma to a tab (\t).
        # We use `rstrip` before that to remove the trailing newline (\n) 
        # character.
        city, date, temp_f = line_data.rstrip('\n').split('\t')
        # We will use the function we wrote above convert temp_f to celsius.
        # We store the value `return`d by `f_to_c` by using the equal sign:
        temp_c = f_to_c(temp_f)
        # We will use the other function we wrote above to convert date
        # to a weekday.
        weekday = date_to_weekday_name(date)
        # Print the results to the screen (we could also write to a file, but we don't have to)
        print(city, date, weekday, temp_f, temp_c)
        # Just show a few lines--not all of them.  After line number 10 we will break (exit the loop)
        if line_number == 10:
            break