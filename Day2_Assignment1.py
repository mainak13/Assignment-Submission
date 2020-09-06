Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Lists#
>>> L = ["Gravitational Force", 9.8, 1947, [1,2], (M,13) ]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    L = ["Gravitational Force", 9.8, 1947, [1,2], (M,13) ]
NameError: name 'M' is not defined
>>> L = ["Gravitational Force", 9.8, 1947, [1,2], ("M",13) ]
>>> L
['Gravitational Force', 9.8, 1947, [1, 2], ('M', 13)]
>>> L[0]
'Gravitational Force'
>>> L[1]
9.8
>>> L[-2]
[1, 2]
>>> L[3:5]
[[1, 2], ('M', 13)]
>>> #Dictionaries#
>>> {"Haldiram":25, "Coke":35, "Chicken":100, "Papad":20, "Ice Cream":50 }
{'Haldiram': 25, 'Coke': 35, 'Chicken': 100, 'Papad': 20, 'Ice Cream': 50}
>>> DICT["Haldiram"]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    DICT["Haldiram"]
NameError: name 'DICT' is not defined
>>> DICT["Haldiram"]:
	
SyntaxError: invalid syntax
>>> DICT["Coke"]:
	
SyntaxError: invalid syntax
>>> DICT["Coke"]:35
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    DICT["Coke"]:35
NameError: name 'DICT' is not defined
>>> del{DICT['Coke']}
SyntaxError: cannot delete set display
>>> del(DICT['Coke'])
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    del(DICT['Coke'])
NameError: name 'DICT' is not defined
>>> thisdict = {
  "Starter": "Lays",
  "Food": "Chicken",
  "Drink": "Coke"
}
print(thisdict)
SyntaxError: multiple statements found while compiling a single statement
>>> DICT={"Starter": "Lays",  "Food": "Chicken",  "Drink": "Coke"}
>>> print(thisDICT)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(thisDICT)
NameError: name 'thisDICT' is not defined
>>> print(thisdict)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(thisdict)
NameError: name 'thisdict' is not defined
>>> print(DICT)
{'Starter': 'Lays', 'Food': 'Chicken', 'Drink': 'Coke'}
>>> x = DICT.get("Food")
>>> print(x)
Chicken
>>> DICT['Venue']='Terrace'
>>> print(DICT)
{'Starter': 'Lays', 'Food': 'Chicken', 'Drink': 'Coke', 'Venue': 'Terrace'}
>>> DICT['Day']='Sunday'
>>> print(DICT)
{'Starter': 'Lays', 'Food': 'Chicken', 'Drink': 'Coke', 'Venue': 'Terrace', 'Day': 'Sunday'}
>>> del(DICT['Day'])
>>> print(DICT)
{'Starter': 'Lays', 'Food': 'Chicken', 'Drink': 'Coke', 'Venue': 'Terrace'}
>>> 'Lays'in DICT
False
>>> 'Starter'in DICT
True
>>> 'Day'in DICT
False
>>> DICT.keys()
dict_keys(['Starter', 'Food', 'Drink', 'Venue'])
>>> DICT.values()
dict_values(['Lays', 'Chicken', 'Coke', 'Terrace'])
>>> Set1={"Sofa","Bed","Glass","Kitchen","Fan","Bed","movies","Chair"}
>>> Set1:
	
SyntaxError: invalid syntax
>>> Set1
{'Chair', 'Fan', 'Glass', 'Kitchen', 'Sofa', 'movies', 'Bed'}
>>> article_list =["Chair","Rack","Cupboard","Books","Rack","Chair","Iron"]
>>> print article_list
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(article_list)?
>>> print(article_list)
['Chair', 'Rack', 'Cupboard', 'Books', 'Rack', 'Chair', 'Iron']
>>> article_set = set(article_list)
>>> article_set
{'Chair', 'Rack', 'Iron', 'Books', 'Cupboard'}
>>> article_list.add("Bag")
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    article_list.add("Bag")
AttributeError: 'list' object has no attribute 'add'
>>> article_list
['Chair', 'Rack', 'Cupboard', 'Books', 'Rack', 'Chair', 'Iron']
>>> B={"Canon","Nikon","Leica","Sony","Pentax"}
>>> B.add("Fuji")
>>> B
{'Pentax', 'Nikon', 'Leica', 'Sony', 'Fuji', 'Canon'}
>>> B.remove("Sony")
>>> B
{'Pentax', 'Nikon', 'Leica', 'Fuji', 'Canon'}
>>> "Fuji"in B
True
>>> "Sony" in B
False
>>> Camera_set1={'Pentax', 'Nikon', 'Leica', 'Sony', 'Fuji', 'Canon'}
>>> Camera_set1
{'Pentax', 'Nikon', 'Leica', 'Sony', 'Fuji', 'Canon'}
>>> Camera_set2={'Hasselblad', 'Ricoch', 'Sigma', 'Sony', 'Fuji', 'Canon'}
>>> Camera_set2
{'Sony', 'Sigma', 'Fuji', 'Ricoch', 'Canon', 'Hasselblad'}
>>> Camera_set3=Camera_set1 & Camera_set2
>>> Camera_set3
{'Fuji', 'Canon', 'Sony'}
>>> Camera_set3.issubset(Camera_set1)
True
>>> #STRING OPERATIONS#
>>> 
>>> Name="Bahubali"
>>> Name[0:3]
'Bah'
>>> FullName="Arnab Goswami"
>>> FullName[0:2]
'Ar'
>>> FullName[6:9]
'Gos'
>>> FullName[::2]
'AnbGsai'
>>> #TUPLES#
>>> len("Arnab Goswami")
13
>>> Statement = FullName+"tells always that Nation wants to know"
>>> Statement
'Arnab Goswamitells always that Nation wants to know'
>>> C="Coke is alternate of Coca Cola"
>>> D=C.upper()
>>> D
'COKE IS ALTERNATE OF COCA COLA'
>>> B=D.lower()
>>> B
'coke is alternate of coca cola'
>>> E=C.replace('Coke','Pepsi')
>>> E
'Pepsi is alternate of Coca Cola'
>>> 