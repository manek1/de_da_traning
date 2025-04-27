#5-1. Conditional Tests: Write a series of conditional tests. Print a statement
#describing each test and your prediction for the results of each test. Your code
#should look something like this:
#car = 'subaru'
#print("Is car == 'subaru'? I predict True.")
#print(car == 'subaru')
#print("\nIs car == 'audi'? I predict False.")
#print(car == 'audi')
#• Look closely at your results, and make sure you understand why each line
#evaluates to True or False.
#• Create at least 10 tests. Have at least 5 tests evaluate to True and another
#5 tests evaluate to False.

car = 'subaru'

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')  # True

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')  # False

print("\nIs car != 'audi'? I predict True.")
print(car != 'audi')  # True

print("\nIs car == 'Subaru'? I predict False.")
print(car == 'Subaru')  # False (case-sensitive)

print("\nIs car.lower() == 'subaru'? I predict true.")
print(car.lower() == 'subaru')  # True

print("\nIs car.upper() == 'SUBARU'? I predict True.")
print(car.upper() == 'SUBARU')  # True

print("\nIs len(car) == 6? I predict True.")
print(len(car) == 6)  # True

print("\nIs len(car) > 10? I predict False.")
print(len(car) > 10)  # False

print("\nIs car.startswith('sub')? I predict True.")
print(car.startswith('sub'))  # True

print("\nIs car.endswith('z')? I predict False.")
print(car.endswith('z'))  # False