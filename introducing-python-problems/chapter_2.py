#Problem 2.1: How many seconds are in an hour? Use the intepreter as a calculator and multiply the number of seconds in a minute (60) by the number of minutes in an hour (also 60).
print(60*60)

#Problem 2.2: Assign the result form the previous task (seconds in an hour) to a variable called seconds_per_hour
seconds_per_hour = 60*60
print(seconds_per_hour)

#Problem 2.3: How many seconds are in a day? Use your seconds_per_hour variable
seconds_per_hour = 60*60
print(seconds_per_hour*24)

#Problem 2.4: Calculate seconds per day again, but this time save the result in a variable called seconds_per_day.
seconds_per_hour = 60*60
seconds_per_day = seconds_per_hour*24
print(seconds_per_day)

#Problem 2.5: Divide seconds_per_day by seconds_per_hour. Use floating point division.
seconds_per_hour = 60*60
seconds_per_day = seconds_per_hour*24
print(seconds_per_day/seconds_per_hour)

#Problem 2.6: Divide seconds_per_day by seconds_per_hour, using integer division. Did this number agree with the floating point value from the previous question, aside from the final .0?
seconds_per_hour = 60*60
seconds_per_day = seconds_per_hour*24
print(seconds_per_day//seconds_per_hour)
