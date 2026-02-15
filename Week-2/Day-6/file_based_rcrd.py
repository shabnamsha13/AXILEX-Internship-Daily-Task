# file based record system
name = input("Enter Name: ")
age = input("Enter Age: ")

file = open("records.txt", "a")
file.write("Name: " + name + ", Age: " + age + "\n")
file.close()

print("Record Saved Successfully!")
file = open("records.txt", "r")
print("\nSaved Records:")
print(file.read())
file.close()
