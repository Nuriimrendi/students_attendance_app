# student.py

class Student:
    def __init__(self, student_id, name, surname, email, attendance):
        self.student_id = student_id
        self.name = name
        self.surname = surname
        self.email = email
        self.attendance = attendance
        

    def __str__(self):
        return f"{self.name} {self.surname} - {self.email}"

def load_mocked_students():
    """
    This function returns a list of Student objects based on the mocked data.
    In the future, this will be replaced with real API calls.
    """
    mock_student_data = {
        "students": [
            [6, "Ahmet Furkan", "Kocabas", "ahmetfurkan.kocabas@agu.edu.tr", "3"],
            [7, "Enis", "Ozkan", "enis.ozkan@agu.edu.tr", "2"],
            [11, "Nuri", "Imrendi", "nuri.imrendi@agu.edu.tr", "1"]
        ]
    }

    students = []
    for data in mock_student_data['students']:
        student = Student(data[0], data[1], data[2], data[3], data[4])
        students.append(student)
    return students
