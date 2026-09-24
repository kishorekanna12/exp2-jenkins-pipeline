

def generate_report(course_name, student_count):
    filename = "build_report.txt"
    with open(filename, "w") as f:
        f.write(f"Course Name: {course_name}\n")
        f.write(f"Students Enrolled: {student_count}\n")
    print(f"Successfully generated {filename}")

if __name__ == "__main__":
   
    COURSE = "DevOps Engineering"
    STUDENT_COUNT = 60 
    
    generate_report(COURSE, STUDENT_COUNT)
