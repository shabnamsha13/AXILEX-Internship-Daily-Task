# Student Management System
students = {}
roll = input("Enter Roll Number: ")
name = input("Enter Name: ")
marks = input("Enter Marks: ")

students[roll] = {"Name": name, "Marks": marks}
print("\nStudent Records:")
for r, details in students.items():
    print("Roll No:", r)
    print("Name:", details["Name"])
    print("Marks:", details["Marks"])
