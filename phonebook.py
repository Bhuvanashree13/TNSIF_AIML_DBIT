phonebook = {"Ram": 9864543546, "Shyam": 9876543210, "Sita": 9988776655}
user_name = input("Enter the name of the user:")
if user_name in phonebook:
    new_number = int(input("Enter the new phone number: "))
    phonebook[user_name] = new_number
    print("Phone number is updated successfully.")
else:
    print("User not founnd")
phonebook["Mohan"] = 1234567890
print(phonebook)
user_name1 = input("Enter the name of the user to delete:")
if user_name1 in phonebook:
    del phonebook[user_name1]
    print("User deleted successfully.")
phonebook.clear()   # Used to clear the dictionary
print(phonebook)
print(phonebook.keys())
print(phonebook.values())