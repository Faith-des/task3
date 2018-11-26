import datetime
#str try
str = 'sensei ha kanashii'
print(str)
str2 = str.rstrip('ii')
print (str2)

# it works! delet spaces from right and left
string = '  sensei   '
print(string.strip())

# split try
x='blue,red,green'
a,b,c = x.split(',')
print(a)
# >>> blue 
# COOL!

# datetime try
y = datetime.datetime.now()
print(y) 
print(y.year)
# weekday
print(y.strftime("%A")) 

# create a date object
y2 = datetime.datetime(2020, 5, 17)
print(y2) 

#weekday!!!
str_date = '2018-11-13'
python_date = datetime.datetime.strptime(str_date, '%Y-%m-%d')
print(python_date)
print(python_date.strftime('%A'))