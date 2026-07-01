person = ["John", 25, "Engineer", "New York", "USA", "Single", "john@example"]
print(f"Name: {person[0]}")  # Output: Name: John
print(f"Age: {person[1]}")   # Output: Age: 25
print(f"Occupation: {person[2]}")  # Output: Occupation: Engineer
print(f"City: {person[3]}")   # Output: City: New York
print(f"Country: {person[4]}")  # Output: Country: USA
print(f"Marital Status: {person[5]}")  # Output: Marital Status: Single
print(f"Email: {person[6]}")  # Output: Email: john@example

#For loop to iterate through the list and print each value with its index
#to short the code we can use enumerate function which will give us index and value at the same time
#used loop
for i, value in enumerate(person):
    print(f"Index {i}: {value}")
