Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def main():
	salelist = []
	print("The store's sales for each day of the week: ")
	for i in range(7):
		print("The store sale of the day", (i + 1),":$",sep="",end="")
		storesale = float(input(""))
		salelist.append(storesale)
	print("salelist:",end="")
	print(salelist)
	total = 0
	for element in salelist:
		total += element
	print("The total sales for the week: $",format(total,'.2f'),sep="")

	
>>> main()
The store's sales for each day of the week: 
The store sale of the day1:$345
The store sale of the day2:$875
The store sale of the day3:$273
The store sale of the day4:$492
The store sale of the day5:$183
The store sale of the day6:$49
The store sale of the day7:$394
salelist:[345.0, 875.0, 273.0, 492.0, 183.0, 49.0, 394.0]
The total sales for the week: $2611.00
>>> 