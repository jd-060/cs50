# Ask user for a simple clause (a string)
UserStatement = input ("Tell me a quick detail about yourself: ")

# Remove leading/trailing spaces, and convert all letters to lower case
UserStatement = UserStatement.strip().lower()

# Output the user's converted clause
print("Whispermode: ", UserStatement)




