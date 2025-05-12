'''6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary.'''

person={'first_name':'Ashwathi','last_name':'Nair','age':'27','city':'Dubai'}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

'''6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite 
number for each person, and store each as a value in your dictionary. Print 
each person’s name and their favorite number. For even more fun, poll a few 
friends and get some actual data for your program.'''

fav_no={'Ash':'9','Pra':'369','Bob':'7','Kian':'78'}
print(fav_no)

'''6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
•	 Think of five programming words you’ve learned about in the previous 
chapters. Use these words as the keys in your glossary, and store their 
meanings as values.
•	 Print each word and its meaning as neatly formatted output. You might 
print the word followed by a colon and then its meaning, or print the word 
on one line and then print its meaning indented on a second line. Use the 
newline character (\n) to insert a blank line between each word-meaning 
pair in your output.'''

glossary={
    'lists':"Collection of iems accessed from position",
    'dictionary':"Collection of items in key-value form",
    'classes':"Its a blueprint to create objects.  "
}
print("The glossary of items are: ")
for key in glossary:
    print(key+":\n\t"+glossary[key])

'''6-4. Glossary 2: Now that you know how to loop through a dictionary, clean 
up the code from Exercise 6-3 (page 102) by replacing your series of print
statements with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your 
glossary. When you run your program again, these new words and meanings 
should automatically be included in the output.'''

'''6-5. Rivers: Make a dictionary containing three major rivers and the country 
each river runs through. One key-value pair might be 'nile': 'egypt'.
•	 Use a loop to print a sentence about each river, such as The Nile runs 
through Egypt.
•	 Use a loop to print the name of each river included in the dictionary.
•	 Use a loop to print the name of each country included in the dictionary.'''

rivers={'Nile':'Egypt','Ganga':'Northern India','Kaveri':'South India'}
for key,value in rivers.items():
    print("\nThe river "+key+" runs through "+value)
print("The list of rivers are: ")
for key in rivers:
    print('\t'+key)
print("The list of countries are: ")
for value in rivers.values():
    print('\t'+value)

'''6-6. Polling: Use the code in favorite_languages.py (page 104).
•	 Make a list of people who should take the favorite languages poll. Include 
some names that are already in the dictionary and some that are not.
•	 Loop through the list of people who should take the poll. If they have 
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take 
the poll.'''
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
people_to_take_poll=['jen','max','sarah','edward','pluto']

print('\nThis is solution for 6-6 ')
for people in people_to_take_poll:
    if people in favorite_languages.keys():
        print(people.title()+' has already taken the poll.')
    else:
        print(people.title()+', please take the poll.')

'''6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three 
dictionaries in a list called people. Loop through your list of people. As you 
loop through the list, print everything you know about each person.'''

print("========================================================================")
person1={'first_name':'Ashwathi','last_name':'Nair','age':'28','city':'Dubai'}
person2={'first_name':'Ashwin','last_name':'Nair','age':'30','city':'Pune'}
person3={'first_name':'Natasha','last_name':'Nambiar','age':'30','city':'Chennai'}
people=[person1,person2,person3]

for person in people:
    print("The name of the person is "+person['first_name'].title()+" "+person['last_name'].title()+'.')
    print("The age is "+person['age']+", and they stay in "+person['city']+'.')
    print("-------------")

'''6-8. Pets: Make several dictionaries, where the name of each dictionary is the 
name of a pet. In each dictionary, include the kind of animal and the owner’s 
name. Store these dictionaries in a list called pets. Next, loop through your list 
and as you do print everything you know about each pet.'''

marcus={'Kind_of_animal':'Monkey','Owner_Name':'Ross'}
scooby={'Kind_of_animal':'Dog','Owner_Name':'Richie'}
kitty={'Kind_of_animal':'Cat','Owner_Name':'Phoebe'}

pets=[marcus,scooby,kitty]

for pet in pets:
    print("----------------")
    print("This pet is a "+pet['Kind_of_animal']+". It belongs to "+pet['Owner_Name']+".")

'''6-9. Favorite Places: Make a dictionary called favorite_places. Think of three 
names to use as keys in the dictionary, and store one to three favorite places 
for each person. To make this exercise a bit more interesting, ask some friends 
to name a few of their favorite places. Loop through the dictionary, and print 
each person’s name and their favorite places'''

favorite_places={'Pramod':['London','France','Peru'] , 'Avantika':['Leh','Bahamas','Switzerland'] ,'Subha':['Palakkad','Ooty','Kedarnath'] }
print("Below is a list of people and their favorite places to visit")
for person,places in favorite_places.items():
    print("The favourite places of "+person+" are: ")
    for place in places:
        print("\t"+place)

'''6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so 
each person can have more than one favorite number. Then print each person’s 
name along with their favorite numbers.'''

fav_no={'Ash':[9,10,28],'Pra':[369,936,639],'Bob':[7,9,8],'Kian':[78,96,14]}

print("This is a list of people along with their fav numbers")

for person,numbers in fav_no.items():
    print("----------------------------")
    print("The fav numbers of "+person+" are :")
    for number in numbers:
        print(number)

'''6-11. Cities: Make a dictionary called cities. Use the names of three cities as 
keys in your dictionary. Create a dictionary of information about each city and 
include the country that the city is in, its approximate population, and one fact 
about that city. The keys for each city’s dictionary should be something like 
country, population, and fact. Print the name of each city and all of the information you have stored about it.'''

Cities={'Jodhpur':{'Country':'India','Population':'1.4 billion','Fact':'It is known as the blue city'}
    ,'Kannur':{'Country':'India','Population':'1.4 billion','Fact':'It is known for Theyyam'}
    ,'Dubai':{'Country':'UAE','Population':'10.4 million','Fact':'It is famous for Burj Khalifa'} }

for city,info in Cities.items():
    print("----------------------------")
    print("Please find below the details for the city : "+city.title())
    print("The city is part of "+info['Country']+'. It has a population of '+info['Population']
          +'.'+info['Fact']+'.')

'''6-12. Extensions: We’re now working with examples that are complex enough 
that they can be extended in any number of ways. 
Use one of the example programs from this chapter, and extend it 
by adding new keys and values, changing the context of the program or 
improving the formatting of the output.'''

print("\n Ex 6-12: Not attempted this one as the exercises have already been attempted to have a standard formatting. ")



