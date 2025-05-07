#6-12. Extensions: We’re now working with examples that are complex enough
#that they can be extended in any number of ways. Use one of the example programs
#from this chapter, and extend it by adding new keys and values, changing
#the context of the program or improving the formatting of the output.

# Expanded dictionary with more details per city
cities = {
    'paris': {
        'country': 'france',
        'population': 2148000,
        'fact': 'known as the City of Light',
        'language': 'french',
        'landmark': 'Eiffel Tower'
    },
    'tokyo': {
        'country': 'japan',
        'population': 13960000,
        'fact': 'largest metropolitan area in the world',
        'language': 'japanese',
        'landmark': 'Tokyo Tower'
    },
    'cairo': {
        'country': 'egypt',
        'population': 9900000,
        'fact': 'home to the Great Pyramids of Giza',
        'language': 'arabic',
        'landmark': 'Great Sphinx'
    },
    'new york': {
        'country': 'usa',
        'population': 8419000,
        'fact': 'nicknamed the Big Apple',
        'language': 'english',
        'landmark': 'Statue of Liberty'
    }
}

# Nicely formatted output
for city, info in cities.items():
    print(f"\n📍 {city.title()}")
    print(f"  🗺️ Country     : {info['country'].title()}")
    print(f"  👥 Population : {info['population']:,}")  # Format number with commas
    print(f"  🌍 Language    : {info['language'].title()}")
    print(f"  🏛️ Landmark    : {info['landmark']}")
    print(f"  📝 Fact        : {info['fact'].capitalize()}")