# append new data to the existing file
with open("student.txt", "a") as file:
    file.write("\nUniversity: VTU")
    file.write("\nYear: 2nd Year MCA")

print("Data appended successfully.")
