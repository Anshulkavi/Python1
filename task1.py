name = input("Enter the student's name: ").lower()

student = {
    'viru': 25,
    'virat': 30,
    'sachin': 43,
    'saiyara': 45,
    'alice': 55,
}

if name in student:
    print(f"{name}'s marks: {student.get(name)}")
else:
    print("student not found.")
