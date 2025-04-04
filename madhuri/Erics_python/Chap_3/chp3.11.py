#3-11. Intentional Error: If you haven’t received an index error in one of your
#programs yet, try to make one happen. Change an index in one of your programs
#to produce an index error. Make sure you correct the error before closing
#the program

# List of cities
places=['New York','London','Paris','Tokyo','Cairo']
# Intentionally cause an IndexError by accessing an invalid index
try:
    print("\nAccessing an invalid index (7):")
    print(places[7])  # This will cause an IndexError because the list only has 5 elements
except IndexError as e:
    print(f"An error occurred: {e}")

    # Correcting the error by accessing a valid index
    print("\nNow accessing a valid index (2):")
    print(places[2])  # This will work, since index 2 is valid (London)
