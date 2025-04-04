#3-10. Every Function: Think of something you could store in a list. For example,
#you could make a list of mountains, rivers, countries, cities, languages, or anything
#else you’d like. Write a program that creates a list containing these items
#and then uses each function introduced in this chapter at least once.

# 1. Create a list of places
places=['New York','sydney','Paris','Tokyo','Cairo']

# 2. Use len() to print the number of cities in the list
print(f"Number of places in the list: {len(places)}")

# 3. Use append() to add a new city to the list
places.append('Barcelona')
print("\nAfter appending Barcelona:")
print(places)

# 4. Use insert() to add a city at a specific position
places.insert(2, 'Rome')
print("\nAfter inserting Rome at index 2:")
print(places)

# 5. Use remove() to remove a specific city from the list
places.remove('New York')
print("\nAfter removing New York:")
print(places)

# 6. Use pop() to remove the last city from the list
last_city = places.pop()
print("\nAfter popping the last city:", last_city)
print(places)

# 7. Use sort() to sort the list alphabetically
places.sort()
print("\nAfter sorting alphabetically:")
print(places)

# 8. Use reverse() to reverse the order of the list
places.reverse()
print("\nAfter reversing the list:")
print(places)

# 9. Use sorted() to print the list in alphabetical order without changing the original list
print("\nSorted (without modifying original list):")
print(sorted(places))

# 10. Use reverse() again to change the order back to the original
places.reverse()
print("\nAfter reversing the list back to the original order:")
print(places)

# 11. Use count() to count how many times a certain city appears in the list
print("\nCount of 'Paris' in the list:", places.count('Paris'))

# 12. Use extend() to combine the cities list with another list of cities
more_cities = ['Berlin', 'Amsterdam']
places.extend(more_cities)
print("\nAfter extending the list with more cities:")
print(places)