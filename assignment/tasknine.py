minute = input("type the number of minutes used: ")
minute = int(minute)
hour = minute//60
minutes= minute%60
seconds= minute % 360
print(hour, "hours",minutes ,"minutes", seconds, "seconds")
