year = 2021 #enter year to evalutate whether or not it is a leap year

if (year%4) == 0: #is this divisible by 4?
	print(year, 'is a leapyear')
elif (year%100) !=0 and (year%400) == 0: #is this a leap year when not divisible by 4?
	print(year, 'is a leapyear')
else:
	print(year, 'is not a leapyear') #if it failes the third criteria its not a leap year
