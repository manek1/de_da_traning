#10-5. Programming Poll: Write a while loop that asks people why they like
#programming. Each time someone enters a reason, add their reason to a file
#that stores all the responses

# Programming Poll
filename = 'programming_poll.txt'

print("Welcome to the Programming Poll!")
print("Type 'quit' to exit.\n")

while True:
    response = input("Why do you like programming? ")

    if response.lower() == 'quit':
        print("Thank you for participating in the poll!")
        break

    # Append the response to the file
    with open(filename, 'a') as file:
        file.write(response + '\n')

    print("Thanks! Your response has been recorded.\n")