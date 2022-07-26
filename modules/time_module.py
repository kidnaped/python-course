import time

#print(time.ctime(0))    # convert a time expressed in seconds since epoch to a readable string
#                         epoch = when your computer thinks time began (reference point)

#print(time.time())      # return current seconds since Epoch

#print(time.ctime(time.time()))  # return cuttent time

#time_object = time.localtime()
#print(time_object)     # prints time object structure
#local_time = time.strftime("%d %B %Y %H:%M:%S", time_object) # for sybolic syntax see the time.strftime() documentation
#print(local_time)

#time_string = "25 July 2022"
#time_object = time.strptime(time_string, "%d %B %Y")
#print(time_object)

# (year, month, day, hours, minutes, seconds, day of week, day of the year, dst)
#time_tuple = (2022, 7, 25, 22, 35, 0, 0, 0, 0)
#time_string = time.asctime(time_tuple) # time representation of given values from a tuple
#print(time_string)

time_tuple = (2022, 7, 25, 22, 35, 0, 0, 0, 0)
time_string = time.mktime(time_tuple) # time representation in seconds since Epoch of given values from tuple
print(time_string)
