Frontend = {"Anu", "Ammu", "Rahul", "Arun"}
Backend = {"Rahul", "Arun", "Meera", "Vishnu"}

Backend.add("Arathi")
Frontend.remove("Ammu")
print("Both Coures:",Frontend & Backend)
print("only backend:",Backend-Frontend)

print("Total Unique Students:",len(Frontend|Backend))
courses = {
    "Frontent":len(Frontend),
    "Backend": len(Backend)
}
for course, students in courses.items():
    print(course, ":", students)
    
update_courses ={
    **{courses:count for courses,count in courses.items()},
    "Fullstack":sum (courses.values())
}
print(update_courses)

