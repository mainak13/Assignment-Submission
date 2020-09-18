Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##Assignment for flight height landing
>>> num = int(input("Enter a number: "))
Enter a number: 3500
>>> 
if 1000 < num < 5000:
    print(“Bring down to 1000")
elif 0 < num < 999:
    print("Safe to Land")
else:
    print("Turn around")
	  
SyntaxError: invalid character in identifier
>>> 
if 1000 < num < 5000:
    print("Bring down to 1000")
elif 0 < num < 999:
    print("Safe to Land")
else:
    print("Turn around")

    
Bring down to 1000
>>> 