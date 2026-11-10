python_students = {"Alice", "Bob", "Charlie"}
data_science = {"Charlie", "David", "Eve"}

python_students.add("Frank")
data_science.remove("Eve")

print("Both:", python_students & data_science)

print("Only Python:", python_students - data_science)

print("All Students:", python_students | data_science)

courses = {"python":len(python_students),"data science":len(data_science)}

for course, students in courses.items():
    print(f"Course: {course}, Students: {students}")

expected_growth = {
    course: students * 2
    for course, students in courses.items()
}

print("Expected Growth:", expected_growth)