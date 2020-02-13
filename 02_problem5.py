#prompt the user to enter a year

user_year = input('Please enter a valid year: ')
valid_year = int(user_year) #turns input into an integer

if valid_year >= 1900 and valid_year<= 9999: #checks to see if the year is a valid year
	if (valid_year%4) == 0: #typically if its divisible by 4 then it is a leap year
		print(valid_year, 'is a valid year and a leap year')
	elif(valid_year%100) !=0 and (valid_year%400) == 0: #another instance it could be a leap year is if not divisible by 100 but divisible by 400
		print(valid_year, 'is a valid year and a leapyear')
	else:
		print(valid_year, 'is a valid year but not a leapyear') #if it failes the third criteria its not a leap year
else:
	print(valid_year, 'is not a valid year') #when number is not in given range then will be prompted that it is not a valid year