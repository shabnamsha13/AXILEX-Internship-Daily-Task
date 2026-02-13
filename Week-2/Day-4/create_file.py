# create a file and write data into it
file = open("student.txt", "w")   # "w" mode creates file if not exists
file.write("Name: Sam\n")
file.write("Course: MCA\n")
file.write("Subject: Python Programming\n")
file.close()  
print("File created and data written successfully!!")
