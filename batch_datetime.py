import datetime

now = datetime.datetime(2003, 8, 4, 12, 30, 45)

print now
print repr(now)
print type(now)
print now.year, now.month, now.day
print now.hour, now.minute, now.second
print now.microsecond


# >>>different representation of date and time
import datetime
import time

now = datetime.datetime.now()

print now
print now.ctime()
print now.isoformat()
print now.strftime("%Y%m%dT%H%M%S")


# >>>date
import datetime

d = datetime.date(2003, 7, 29)

print d
print d.year, d.month, d.day

print datetime.date.today()

# >>>>time
import datetime

t = datetime.time(18, 54, 32)

print t
print t.hour, t.minute, t.second, t.microsecond

# >>>>>datetime
import datetime

now = datetime.datetime.now()

d = now.date()
t = now.time()

print now
print d, t
print datetime.datetime.combine(d, t)



#Read more: https://pymotw.com/2/datetime/
#read more: https://www.guru99.com/date-time-and-datetime-classes-in-python.html
# SAMPLE CODES


# from datetime import date
# from datetime import time
# from datetime import datetime
# def main():
#  	 ##DATETIME OBJECTS
#      #Get today's date from datetime class
# 	   today=datetime.now()
#   #print today
#   # Get the current time
#   #t = datetime.time(datetime.now())
#   #print "The current time is", t
#  #weekday returns 0 (monday) through 6 (sunday)
#      wd = date.weekday(today)
#  #Days start at 0 for monday
#       days= ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
#       print "Today is day number %d" % wd
#       print "which is a " + days[wd]
#
# if __name__== "__main__":
#     main()



#Example file for formatting time and date output
#
# from datetime import datetime
# def main():
#    #Times and dates can be formatted using a set of predefined string
#    #Control codes
#       now= datetime.now() #get the current date and time
#       #%c - local date and time, %x-local's date, %X- local's time
#       print now.strftime("%c")
#       print now.strftime("%x")
#       print now.strftime("%X")
# ##### Time Formatting ####
#       #%I/%H - 12/24 Hour, %M - minute, %S - second, %p - local's AM/PM
#       print now.strftime("%I:%M:%S %p") # 12-Hour:Minute:Second:AM
#       print now.strftime("%H:%M") # 24-Hour:Minute
#
# if __name__== "__main__":
#     main()



# #
# #Example file for working with timedelta objects
# #
#    from datetime import date
#    from datetime import time
#    from datetime import datetime
#    from datetime import timedelta
# # construct a basic timedelta and print it
#    print timedelta(days=365,hours=8,minutes=15)
# # print today's date
#    print "today is: " + str(datetime.now())
# # print today's date one year from now
#    print "one year from now it will be:" + str(datetime.now() + timedelta (days=365))
# #create a timedelta that uses more than one argument
# #print "in one week and 4 days it will be " + str(datetime.now() + timedelta(weeks=1, days=4))
# #How many days until New Year's Day?
# 	today= date.today() #get todays date
# 	nyd= date(today.year,1,1) #get New Year Day for the same year
# #use date comparison to see if New Year Day has already gone for this year
# #if it has, use the replace() function to get the date for next year
#    if nyd < today:
#  	  print "New Year day is already went by %d days ago" % ((today-nyd).days)