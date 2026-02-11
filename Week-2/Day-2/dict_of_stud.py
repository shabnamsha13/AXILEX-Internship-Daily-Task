# Create dictionary of student details
student = {
    "Name": "SHABNAM",
    "USN": "4UB24MC087",
    "Course": "MCA",
    "Semester": 4,
    "College": "UBDT College"
}
print(student) 
print("Student Details:")
for key, value in student.items():
    print(key, ":", value)
