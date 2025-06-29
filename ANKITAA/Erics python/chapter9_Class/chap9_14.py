#9-14. Dice: The module random contains functions that generate random numbers
#in a variety of ways. The function randint() returns an integer in the
#range you provide. The following code returns a number between 1 and 6:
#from random import randint
#x = randint(1, 6)
#Make a class Die with one attribute called sides, which has a default
#value of 6. Write a method called roll_die() that prints a random number
#between 1 and the number of sides the die has. Make a 6-sided die and roll
#it 10 times.
#Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from random import randint

class Die:
    """A class representing a die with a customizable number of sides."""

    def __init__(self, sides=6):
        """Initialize the die with a given number of sides."""
        self.sides = sides

    def roll_die(self):
        """Return a random number between 1 and the number of sides."""
        return randint(1, self.sides)

# Roll a 6-sided die 10 times
print("Rolling a 6-sided die:")
six_sided = Die()
for _ in range(10):
    print(six_sided.roll_die())

# Roll a 10-sided die 10 times
print("\nRolling a 10-sided die:")
ten_sided = Die(10)
for _ in range(10):
    print(ten_sided.roll_die())

# Roll a 20-sided die 10 times
print("\nRolling a 20-sided die:")
twenty_sided = Die(20)
for _ in range(10):
    print(twenty_sided.roll_die())