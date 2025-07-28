# user.py

from courses import Course  # Import the Course class to associate courses with users

class User:
    def __init__(self, user_id=None, name=None, surname=None, email=None, password=None):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.courses = []  # List to store courses

    def set_user_info(self, user_id, name, surname, email, password):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password

    def add_course(self, course):
        """Method to add a course to the user's list."""
        self.courses.append(course)
    

    def get_courses(self):
        """Returns the list of courses that the user is teaching."""
        return self.courses
    
    def find_course_name_by_id(self, course_id):
        """Find the course name by course ID."""
        for course in self.courses:
            if course.course_id == course_id:
                return course.course_name
        return "Course not found"
    
    def __str__(self):
        return f"User ID: {self.user_id}, Name: {self.name} {self.surname}, Email: {self.email}"

    def print_courses(self):
        """Prints the courses the user is teaching."""
        if self.courses:
            for course in self.courses:
                print(course)
        else:
            print("No courses assigned.")
