#5-2. More Conditional Tests: You don’t have to limit the number of tests you
#create to 10. If you want to try more comparisons, write more tests and add
#them to conditional_tests.py. Have at least one True and one False result for
#each of the following:
#• Tests for equality and inequality with strings
#• Tests using the lower() function
#• Numerical tests involving equality and inequality, greater than and
#less than, greater than or equal to, and less than or equal to
#• Tests using the and keyword and the or keyword
#• Test whether an item is in a list
#• Test whether an item is not in a list

# 🔤 1. Tests for equality and inequality with strings
fruit = 'apple'
print("Is fruit == 'apple'? I predict True.")
print(fruit == 'apple')  # True

print("Is fruit != 'banana'? I predict True.")
print(fruit != 'banana')  # True

print("Is fruit == 'Apple'? I predict False.")
print(fruit == 'Apple')  # False (case-sensitive)

# 🔤 2. Tests using the lower() function
name = 'Alice'
print("Is name.lower() == 'alice'? I predict True.")
print(name.lower() == 'alice')  # True

print("Is name.lower() == 'ALICE'? I predict False.")
print(name.lower() == 'ALICE')  # False

# 🔢 3. Numerical tests
age = 21
print("Is age == 21? I predict True.")
print(age == 21)  # True

print("Is age != 18? I predict True.")
print(age != 18)  # True

print("Is age > 18? I predict True.")
print(age > 18)  # True

print("Is age < 18? I predict False.")
print(age < 18)  # False

print("Is age >= 21? I predict True.")
print(age >= 21)  # True

print("Is age <= 20? I predict False.")
print(age <= 20)  # False

# 🔗 4. Tests using 'and' and 'or'
height = 5.9
weight = 160

print("Is height > 5.5 and weight < 170? I predict True.")
print(height > 5.5 and weight < 170)  # True

print("Is height > 6 and weight < 150? I predict False.")
print(height > 6 and weight < 150)  # False

print("Is height > 6 or weight == 160? I predict True.")
print(height > 6 or weight == 160)  # True

print("Is height < 5 or weight > 200? I predict False.")
print(height < 5 or weight > 200)  # False

# 📦 5. Test whether an item is in a list
colors = ['red', 'blue', 'green']
print("Is 'blue' in colors? I predict True.")
print('blue' in colors)  # True

print("Is 'yellow' in colors? I predict False.")
print('yellow' in colors)  # False

# 6. Test whether an item is not in a list
print("Is 'purple' not in colors? I predict True.")
print('purple' not in colors)  # True

print("Is 'red' not in colors? I predict False.")
print('red' not in colors)  # False