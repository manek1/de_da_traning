#3-1.  Names:  Store the names of a few of your friends in a list called  names  Print each person’s name by accessing each element in the list, one at a time
friends=['Ash', 'chandni','monica','Prajakta','Shamli']
print(friends[0])
print(friends[-1])
print(friends[1])
print(friends[2])
print(friends[3])

#3-2.  Greetings:  Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them  The text of each mes-sage should be the same, but each message should be personalized with the person’s name

print('I love my girls: '+ friends[1].title()+','+friends[2].title()+','+friends[3]+' and '+friends[-1])

#3-3.  Your Own List:  Think of your favorite mode of transportation, such as a
#motorcycle or a car, and make a list that stores several examples  Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle ”

vehicles=['Dio','Kia','Ford','G-wagon']
print('Ash had a black '+vehicles[0]+' in Baramati'+' and Pramod a black '+vehicles[1]+'.'+'Currently the red '+vehicles[2]+' is a saviour!'+'But he does hope to get a '+vehicles[3]+'!')

#3-4. G uest List:  If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner  Then use your list to print a message to each person, inviting them to dinner
guest_list=['Priyanka','Gandhiji','Hitler','Abdul Kalam''']
print('Hi '+guest_list[0]+','+guest_list[1]+','+guest_list[2]+' and '+guest_list[3]+'. I would love for you to visit my home! ')

#3-5.  Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations  You’ll have to think of someone else to invite