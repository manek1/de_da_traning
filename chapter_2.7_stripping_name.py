"""2-7. Stripping Names: Store a person’s name, and include some whitespace
characters at the beginning and end of the name. Make sure you use each
character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(),
rstrip(), and strip()."""

# Store a name with extra whitespace and special characters
name = "\t  Mayuri Kale  \n"

# Print the name with whitespace shown
print("Original name (with whitespace):")
print(name)

# Use the three stripping methods
print("Using lstrip():", name.lstrip())  # Removes spaces/tabs/newlines from the left
print("Using rstrip():", name.rstrip())  # Removes from the right
print("Using strip():", name.strip())    # Removes from both sides
