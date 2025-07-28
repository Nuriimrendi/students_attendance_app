# courses.py

from student import Student  # Import the Student class to associate students with courses

class Course:
    def __init__(self, course_id=None, course_name=None):
        self.course_id = course_id
        self.course_name = course_name
        self.students = []  # List to store enrolled students

    def set_course_info(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

    def add_student(self, student):
        """Method to enroll a student in this course."""
        if isinstance(student, Student):
            self.students.append(student)
        else:
            print(f"Invalid student: {student}")

    def get_students(self):
        """Return the list of students enrolled in the course."""
        return self.students

    def __str__(self):
        return f"Course ID: {self.course_id}, Course Name: {self.course_name}"

