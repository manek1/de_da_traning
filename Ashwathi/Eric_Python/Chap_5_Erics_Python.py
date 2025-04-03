#•	 Tests for equality and inequality with strings
a1='Ashwathi'
a2='ashwathi'
print('Start')
if a1==a2:
    print('Both the entered names are same')
else:
    print('The entered names are not same')
print('End')

#Tests using the lower() function
a1='Ashwathi'
a2='ashwathi'
print('Start')
if a1.lower()==a2:
    print('Both the entered names are same')
else:
    print('The entered names are not same')
print('End')

#•	 Test whether an item is in a list
items=['bat','ball','cat','rod']
item='bat'
if item in items:
    print('The entered item is present in the list')
else:
    print('The entered item is NOT present in the list')

#•	 Test whether an item is not in a list
item='cow'
if item not in items:
    print('The entered item is NOT present in the list')

#

