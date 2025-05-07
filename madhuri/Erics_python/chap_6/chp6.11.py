#6-11. Cities: Make a dictionary called cities. Use the names of three cities as
#keys in your dictionary. Create a dictionary of information about each city and
#include the country that the city is in, its approximate population, and one fact
#about that city. The keys for each city’s dictionary should be something like
#country, population, and fact. Print the name of each city and all of the information
#you have stored about it.

# Main dictionary with cities as keys
cities = {
    'paris': {
        'country': 'france',
        'population': 2148000,
        'fact': 'known as the City of Light'
    },
    'tokyo': {
        'country': 'japan',
        'population': 13960000,
        'fact': 'largest metropolitan area in the world'
    },
    'cairo': {
        'country': 'egypt',
        'population': 9900000,
        'fact': 'home to the Great Pyramids of Giza'
    }
}

# Loop through the cities and print the information
for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"  Country: {info['country'].title()}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact'].capitalize()}")