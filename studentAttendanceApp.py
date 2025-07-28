import sys
import PyQt5
from PyQt5 import QtCore 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from loginui import Ui_Form
from dashboard import Ui_MainWindow  
import res_rc  
import resoruces_rc
import requests
from user import *
from courses import *
import pandas as pd
import openpyxl
from PyQt5.QtChart import *
from PyQt5.QtGui import *

user = User()
base_ip = "ip"
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()  
        self.ui.setupUi(self)
        self.ui.loginButton.clicked.connect(self.tryLogin)
        
        self.resize(625, 565)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.centerWindow()

        # Create the close button
        self.closeButton = QPushButton('X', self)
        self.closeButton.setGeometry(QRect(self.width() -110, 65, 20, 20))
        self.closeButton.setStyleSheet(
            "QPushButton {"
            "   background-color: red;"
            "   color: white;"
            "   border: none;"
            "   font-weight: bold;"
            "}"
            "QPushButton:hover {"
            "   background-color: darkred;"
            "}"
        )
        self.closeButton.clicked.connect(self.close)
        self.closeButton.setCursor(Qt.PointingHandCursor)

    def centerWindow(self):
        screen = QDesktopWidget().screenGeometry()
        window = self.geometry()
        x = (screen.width() - window.width()) // 2
        y = (screen.height() - window.height()) // 2
        self.move(x, y)
    
    def tryLogin(self):
        username = self.ui.usernameText.text()
        password = self.ui.passwordText.text()

        print(f"username: {username}, password: {password}")

        if username == "admin" and password == "password":
            self.handle_successful_login("admin")
            return
        
        # Make the API request to authenticate
        api_url = f"http://{base_ip}:5000/authenticate?email={username}&password={password}"
        
        try:
            response = requests.get(api_url)  # Send GET request to the API
            response.raise_for_status()  # Raise an exception if the response status code is not 2xx
            
            # Parse the response JSON
            data = response.json()

            # Check if the response contains the expected structure
            if 'info' in data and 'courses' in data:
                user_info = data['info']
                courses_data = data['courses']

                # Create a new User object and set user information
                self.user = User()
                self.user.set_user_info(
                    user_info["instructor_id"], 
                    user_info["name"], 
                    user_info["surname"], 
                    user_info["email"], 
                    password  # Assuming the password is the one provided by the user
                )

                # Add courses to the user
                for course_data in courses_data:
                    course = Course(course_data["course_id"], course_data["course_name"])
                    self.user.add_course(course)

                # Proceed to the dashboard with the populated user
                self.open_dashboard()

            else:
                print("Hellooo")
                QMessageBox.warning(self, "Login Failed", "Invalid response from server. No user data found.")

        except requests.exceptions.RequestException as e:
            QMessageBox.warning(self, "Login Failed, Wrong username or password!")
    
    def handle_successful_login(self, username):
        """
        Handle the case when the user logs in as 'admin' or a test user.
        Mock data will be used for the admin login.
        """
        print(f"Successfully logged in as {username}")

        # Simulate mock data for the admin user (you can adjust the data to your needs)
        if username == "admin":
            # Mocked user info
            user_info = {
                "instructor_id": 0,
                "name": "Admin",
                "surname": "User",
                "email": "admin@example.com"
            }

            # Mocked courses the admin is teaching
            courses_data = [
                {"course_id": 25, "course_name": "Course 1"},
                {"course_id": 26, "course_name": "Course 2"},
                {"course_id": 24, "course_name": "Güldenaz"}
            ]

            # Create a User object and set the mock user information
            self.user = User()
            self.user.set_user_info(
                user_info["instructor_id"], 
                user_info["name"], 
                user_info["surname"], 
                user_info["email"], 
                "password"  # Mock password for the admin
            )

            # Add mocked courses to the user's courses list
            for course_data in courses_data:
                course = Course(course_data["course_id"], course_data["course_name"])
                self.user.add_course(course)

            print("Courses for the user:")
            for course in self.user.get_courses():
                print(f"- {course.course_name} (ID: {course.course_id})")
            
            # Proceed to the dashboard with the populated user and courses
            self.open_dashboard()

        else:
            # If not 'admin', proceed with normal login or authentication logic
            self.authenticate_via_api()

    def open_dashboard(self):
        # Transition to the DashboardWindow
        self.dashboard = DashboardWindow(self.user)
        self.dashboard.set_instructor_info_from_user()
        self.dashboard.show()
        self.close()  # Close the login window

class DashboardWindow(QMainWindow):
    def __init__(self, user):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.user = user
        self.course_pages = {}

        self.ui.mainscreen.setCurrentIndex(0)
    
        attendance_page = self.ui.mainscreen.widget(3)

# Apply a light gray stylesheet to the dashboard page
        
        attendance_page.setStyleSheet("""
            QTableWidget {
                background-color: #f5f5f5;  /* Light gray background, matching the main widget */
                color: #333333;  /* Dark gray text */
                border: 1px solid #c0c0c0;  /* Light gray border around the table */
            }

            QTableWidget::item {
                padding: 8px;  /* Consistent padding with other widgets */
                background-color: #f5f5f5;  /* Slightly lighter gray background for items */
                color: #333333;  /* Dark gray text for items */
            }

            QTableWidget::item:selected {
                background-color: #a0a0a0;  /* Darker gray when an item is selected */
                color: white;  /* White text for selected items */
            }

            QTableWidget::horizontalHeader {
                background-color: #e0e0e0;  /* Light gray background for the header */
                color: #333333;  /* Dark gray text in header */
                font-weight: bold;  /* Bold text for header */
            }

            QTableWidget::horizontalHeader::section {
                padding: 10px;  /* Consistent padding for header sections */
                border: 1px solid #c0c0c0;  /* Light gray border for header sections */
            }

            QTableWidget::verticalHeader {
                background-color: #e0e0e0;  /* Light gray background for the vertical header */
                color: #333333;  /* Dark gray text in vertical header */
            }

            QTableWidget::verticalHeader::section {
                padding: 10px;  /* Consistent padding for vertical header sections */
                border: 1px solid #c0c0c0;  /* Light gray border for vertical header sections */
            }

            QTableWidget QTableCornerButton::section {
                background-color: #e0e0e0;  /* Light gray for the corner button */
                border: 1px solid #c0c0c0;  /* Border for corner button */
            }

            QScrollBar:vertical {
                background: #e0e0e0;  /* Light gray scrollbar background */
                width: 10px;  /* Scrollbar width */
            }

            QScrollBar::handle:vertical {
                background: #c0c0c0;  /* Slightly darker gray for the scrollbar handle */
                min-height: 20px;  /* Minimum height for the scrollbar handle */
            
            QStackedWidget {
                background:rgb(95, 83, 83);
            }
    
        """)

        # Connect buttons to respective pages
        self.ui.dashboardbuttonwide.clicked.connect(lambda: self.switch_page(0))  # Dashboard page
        self.ui.attendancebuttonwide.clicked.connect(lambda: self.switch_page(3))  # Attendance page
        self.ui.statButton.clicked.connect(lambda: self.switch_page(5))
        self.ui.logoutbuttonwide.clicked.connect(self.handle_logout)
        self.ui.submitbutton.clicked.connect(self.fetch_and_populate_attendance)
        self.ui.calendarWidget.clicked.connect(self.store_date)
        self.ui.coursesComboBox.currentIndexChanged.connect(self.store_selected_course)
        self.ui.coursesComboBox.currentIndexChanged.connect(self.get_course_id_from_name)
        self.ui.statComboBox.currentIndexChanged.connect(self.update_top_pie_chart)
        self.init_top_pie_chart()
        self.create_bar_charts()
        self.setup_empty_attendance_table()
        self.populate_course_combo_box()
        self.populate_course_combo_box_stat()


    def get_students_for_course(self, course_id):
        """
        Fetches the students for the selected course via an HTTP request to the API.
        """
        # URL to fetch students for the given course ID
        url = f"http://{base_ip}:5000/getStudents?course_id={course_id}"

        try:
            # Send a GET request to the API
            response = requests.get(url)
          # Raise an exception for HTTP errors
            print("Hello")
            # Parse the JSON response from the API
            data = response.json()

            # Extract the students list from the API response
            students = data.get("data", [])
            
            # Debugging: Check if student data is being fetched correctly
            print(f"Students for course {course_id}: {students}")

            return students

        except requests.exceptions.RequestException as e:
            # Handle any network or HTTP errors
            print(f"Error fetching students for course {course_id}: {e}")
            return []  # Return an empty list in case of an error

    def set_instructor_info_from_user(self):
        """
        Set the instructor's information on the dashboard.
        Uses the `user` object directly to retrieve the data.
        """
        # Get instructor info from the User object
        name = self.user.name  # Using self.user instead of 'user'
        surname = self.user.surname
        email = self.user.email

        # Format the name and surname
        full_name = f"{name} {surname}"

        # Set the instructor's information in the respective labels
        self.ui.labelInstructorName.setText(full_name)  # Update name label
        self.ui.labelInstructorEmail.setText(email)  # Update email label

        # Dynamically create course buttons
        self.setup_course_buttons()

    def setup_course_buttons(self):
        courses = self.user.get_courses()
        course_layout = QGridLayout()  # Create a new grid layout

        # Clear existing items in the previous layout if necessary
        existing_layout = self.ui.course_layout  # Assuming you have a layout placeholder
        if existing_layout is not None:
            for i in reversed(range(existing_layout.count())):
                widget_to_remove = existing_layout.itemAt(i).widget()
                if widget_to_remove is not None:
                    widget_to_remove.setParent(None)
        
        # Set the new layout to your placeholder widget
        self.ui.course_layout = course_layout
        self.ui.course_widget.setLayout(course_layout) # Assuming you set it to a widget that holds the layout

        # Define a style for the buttons
        button_style = """
            QPushButton {
                min-width: 200px;
                min-height: 100px;
                border-radius: 5px;
                background-color: #d3d3d3;  /* Light gray background */
                color: #333333;  /* Dark gray text */
                font-size: 18px;
                margin: 10px;
                border: 1px solid #ccc;  /* Light border */
            }
            QPushButton:hover {
                background-color: #b0b0b0;  /* Slightly darker gray on hover */
            }
            QPushButton:pressed {
                background-color: #a0a0a0;  /* Even darker when pressed */
            }
        """

        # Add a button for each course
        for index, course in enumerate(courses):
            button = QPushButton(course.course_name)
            button.setStyleSheet(button_style)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

            # Create a unique connection for each button to open the corresponding course page
            button.clicked.connect(lambda _, course_id=course.course_id: self.open_course_page(course_id))

            # Calculate the row and column positions
            row = index // 2
            col = index % 2

            # Add the button to the grid layout
            course_layout.addWidget(button, row, col)

        # Set some spacing for the grid layout
        course_layout.setHorizontalSpacing(20)
        course_layout.setVerticalSpacing(20)
    
    def open_course_page(self, course_id):
        print(f"Opening course page for course ID: {course_id}")

        # Fetch the course name based on course_id (assume self.get_course_name is a function that returns the course name)
        course_name = self.user.find_course_name_by_id(course_id)

        # Ensure the course page is properly created if not already
        if course_id not in self.course_pages:
            # Create the course page for the selected course
            course_page = QWidget()  # Create a new QWidget for the course page
            table_widget = QTableWidget()  # The table to display student info

            # Set up the QTableWidget (same setup as in your code)
            table_widget.setRowCount(0)
            table_widget.setColumnCount(5)
            table_widget.setHorizontalHeaderLabels(["Student ID", "Name", "Surname", "Email", "Attendance"])
            table_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            header = table_widget.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.Stretch)
            table_widget.setStyleSheet("""
                /* Your styles here */
            """)

            # Create a layout for the course page
            layout = QVBoxLayout()

            # Create a horizontal layout for the course name and refresh button
            top_layout = QHBoxLayout()

            # Create a label to display the course name
            course_name_label = QLabel(f"Course: {course_name}")
            top_layout.addWidget(course_name_label)

            # Create a "Refresh" button and add it to the top layout
            refresh_button = QPushButton("Refresh")
            refresh_button.clicked.connect(lambda: self.populate_attendance_table(course_id, table_widget))
            print(f"Course page is refreshed, with course_id {course_id}")
            top_layout.addWidget(refresh_button)

            # Add the top layout to the main layout
            layout.addLayout(top_layout)

            # Add the table widget to the main layout
            layout.addWidget(table_widget)

            # Create an "Export to Excel" button
            export_button = QPushButton("Export to Excel")
            export_button.clicked.connect(lambda: self.export_to_excel(course_id, table_widget))
            layout.addWidget(export_button)

            # Set the layout for the course page widget
            course_page.setLayout(layout)

            # Store the page and the table_widget for later use
            self.course_pages[course_id] = {'course_page': course_page, 'table_widget': table_widget}

            # Add the course page to the QStackedWidget
            self.ui.mainscreen.addWidget(course_page)

        # Get the table widget and course page from the stored course_pages dictionary
        course_data = self.course_pages.get(course_id)
        if course_data:
            course_page = course_data['course_page']
            table_widget = course_data['table_widget']

            # Populate the attendance table
            self.populate_attendance_table(course_id, table_widget)

            # Switch to the page corresponding to the course_id
            index = self.ui.mainscreen.indexOf(course_page)
            self.ui.mainscreen.setCurrentIndex(index)

            # Ensure the table is visible
            course_page.show()

    def populate_attendance_table(self, course_id, table_widget):
        """
        Populate the attendance table with student data for a specific course.
        """
        # Fetch the students for the selected course (this can be replaced with real data later)
        students = self.get_students_for_course(course_id)

        # Debugging: check if students data is being fetched correctly
        print(f"Students for course {course_id}: {students}")

        if not students:
            print(f"No students found for course {course_id}")
        
        # Update the attendance table widget
        table_widget.setRowCount(len(students))  # Set the row count to match the student data
        table_widget.setColumnCount(5)  # Set to 5 columns (Student ID, Name, Surname, Email, Attendance)
        table_widget.setHorizontalHeaderLabels(["Student ID", "Name", "Surname", "Email", "Attendance"])

        # Populate the table with student data
        for row, student in enumerate(students):
            table_widget.setItem(row, 0, QTableWidgetItem(str(student["student_id"])))  # Student ID
            table_widget.setItem(row, 1, QTableWidgetItem(student["name"]))  # Name
            table_widget.setItem(row, 2, QTableWidgetItem(student["surname"]))  # Surname
            table_widget.setItem(row, 3, QTableWidgetItem(student["email"]))  # Email
            table_widget.setItem(row, 4, QTableWidgetItem(str(student["total_hours_attended"])))  # Total hours attended  # Attendance status (mock data for now)
        
        # Check the number of rows in the table after population
        print(f"Rows in attendance table: {table_widget.rowCount()}")

    def export_to_excel_1(self, table_widget):
        # Open file dialog to select where to save the Excel file
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(None, "Save File", "", "Excel Files (*.xlsx);;All Files (*)", options=options)
        
        if file_path:
            # Create a new workbook and sheet
            wb = openpyxl.Workbook()
            sheet = wb.active
            sheet.title = "Attendance Data"
            
            # Write headers to Excel file (dynamically from table headers)
            headers = []
            for col in range(table_widget.columnCount()):
                headers.append(table_widget.horizontalHeaderItem(col).text())
            sheet.append(headers)
            
            # Write rows to Excel file
            for row in range(table_widget.rowCount()):
                row_data = []
                for col in range(table_widget.columnCount()):
                    item = table_widget.item(row, col)
                    row_data.append(item.text() if item else "")
                sheet.append(row_data)
            
            # Save the workbook to the selected file
            wb.save(file_path)
            print(f"File saved to {file_path}")

    def export_to_excel(self, course_id, table_widget):
        # Open file dialog to select where to save the Excel file
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(None, "Save File", "", "Excel Files (*.xlsx);;All Files (*)", options=options)
        
        if file_path:
            # Create a new workbook and sheet
            wb = openpyxl.Workbook()
            sheet = wb.active
            sheet.title = f"Course {course_id} Attendance"
            
            # Write headers to Excel file
            headers = ["Student ID", "Name", "Surname", "Email", "Attendance"]
            sheet.append(headers)
            
            # Write rows to Excel file
            for row in range(table_widget.rowCount()):
                row_data = []
                for col in range(table_widget.columnCount()):
                    item = table_widget.item(row, col)
                    row_data.append(item.text() if item else "")
                sheet.append(row_data)
            
            # Save the workbook to the selected file
            wb.save(file_path)
            print(f"File saved to {file_path}")

    def setup_empty_attendance_table(self):
        """
        Set up the attendance table with headers but no data.
        """
        self.ui.attendanceTableWidget.setColumnCount(5)
        self.ui.attendanceTableWidget.setHorizontalHeaderLabels(["Student ID", "Name", "Surname", "Email", "Attendance"])
        self.ui.attendanceTableWidget.setRowCount(0)  # No rows initially

        header = self.ui.attendanceTableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

    def populate_course_combo_box(self):
        """
        Populate the course ComboBox with courses taught by the logged-in user.
        """
        # Clear any existing items in the combo box
        self.ui.coursesComboBox.clear()
        # Get the courses taught by the logged-in user (assuming user.get_courses() returns a list of Course objects)
        courses = self.user.get_courses()
        
        # Add courses to the ComboBox
        for course in courses:
            # Assuming the Course object has a 'course_name' attribute
            self.ui.coursesComboBox.addItem(course.course_name)

    def populate_course_combo_box_stat(self):
        """
        Populate the course ComboBox with courses taught by the logged-in user.
        """
        # Clear any existing items in the combo box
        self.ui.statComboBox.clear()
        # Get the courses taught by the logged-in user (assuming user.get_courses() returns a list of Course objects)
        courses = self.user.get_courses()
        
        # Add courses to the ComboBox
        for course in courses:
            # Assuming the Course object has a 'course_name' attribute
            self.ui.statComboBox.addItem(course.course_name)

    def store_selected_course(self):
        # Get the selected item from the combo box
        selected_course = self.ui.coursesComboBox.currentText()
        
        # Print or store the selected item
        print(f"Selected course: {selected_course}")
        
        # You can store it in a variable or use it as needed
        self.selected_course = selected_course
        print(selected_course)
        return selected_course

    def store_date(self, date):
        """
        Store the selected date and update the label.
        """
        selected_date = date.toString("yyyy-MM-dd")  # Format the date as YYYY-MM-DD
        #self.selected_date_label.setText(f"Selected Date: {selected_date}")
        print(selected_date)
        # You can store the date as needed (e.g., in a variable, file, database, etc.)
        return selected_date

    def populate_attendance_table_1(self, students):
        """
        Populate the QTableWidget with the student data.
        """
        # Clear existing rows in the table
        self.ui.attendanceTableWidget.setRowCount(0)
        
        # Set column count and headers
        self.ui.attendanceTableWidget.setColumnCount(5)
        self.ui.attendanceTableWidget.setHorizontalHeaderLabels(["Student ID", "Name", "Surname", "Email", "Attendance"])
        

        # Populate the table with student data
        for student in students:
            row_position = self.ui.attendanceTableWidget.rowCount()
            self.ui.attendanceTableWidget.insertRow(row_position)
            
            self.ui.attendanceTableWidget.setItem(row_position, 0, QTableWidgetItem(str(student["student_id"])))  # Name
            self.ui.attendanceTableWidget.setItem(row_position, 1, QTableWidgetItem(student["name"]))  # Surname
            self.ui.attendanceTableWidget.setItem(row_position, 2, QTableWidgetItem(str(student["surname"])))  # Student ID
            self.ui.attendanceTableWidget.setItem(row_position, 3, QTableWidgetItem(str(student["email"])))  # Attendance
            self.ui.attendanceTableWidget.setItem(row_position, 4, QTableWidgetItem(str(student["attendance"])))  # Attendance  
        
        self.ui.Export_to_Excel.clicked.connect(lambda: self.export_to_excel_1(self.ui.attendanceTableWidget))

    def get_course_id_from_name(self, course_name):
        # This is just an example, modify according to your data.
        courses = self.user.get_courses()  # Assume this gives you a list of courses
        for course in courses:
            if course.course_name == course_name:
                print(course.course_id)
                return course.course_id
        return None

    def fetch_and_populate_attendance(self):
        """
        Fetch the attendance data from the server and populate the QTableWidget.
        """
        # Get the selected course ID from the combo box
        selected_course_name = self.ui.coursesComboBox.currentText()
        print(f"selected course is {selected_course_name}")
        # Here you will need to map the course name to its corresponding course ID.

        # Assuming you have a method to map course name to course ID.
        course_id = self.get_course_id_from_name(selected_course_name)
        print(course_id)
        
        # Get the selected date from the calendar widget
        selected_date = self.ui.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        
        # Construct the URL for the API request
        url = f"http://{base_ip}:5000/getAttendanceSheetAt?course_id={course_id}&attendance_date={selected_date}"
        
        try:
            # Make the API request
            response = requests.get(url)
            response_data = response.json()
            
            # Check if the request was successful
            if response_data["status"] == "success":
                # Extract the student data
                students = response_data["data"]
                print("students are fetched")
                print(f"students{students}")
                # Update the table with the fetched data
                self.populate_attendance_table_1(students)
            else:
                print("Failed to fetch attendance data.")
        
        except Exception as e:
            print(f"An error occurred: {e}")

    def switch_page(self, page_index):
        """
        Switches the current page of the QStackedWidget.
        :param page_index: Index of the page in QStackedWidget to display.
        """
        self.ui.mainscreen.setCurrentIndex(page_index)

    def handle_logout(self):
        # Create and show a new LoginWindow
        self.login_window = LoginWindow()
        self.login_window.show()
        
        # Close the current DashboardWindow
        self.close()

    def init_top_pie_chart(self):
        # Set up the QChartView for the top pie chart
        self.top_pie_chart_view = QChartView()
        self.top_pie_chart_view.setRenderHint(QPainter.Antialiasing)
        top_layout = QVBoxLayout(self.ui.StatPieChartTop)
        top_layout.addWidget(self.top_pie_chart_view)
    
    def update_top_pie_chart(self, index):
        # Example data for each course (adjust as needed)
        data_sets = [
            {"Attended": 74, "Not Attended": 26},  # Course 1
            {"Attended": 68, "Not Attended": 32},  # Course 2
            {"Attended": 47, "Not Attended": 53},  # Course 3
            {"Attended": 45, "Not Attended": 55}   # Course 4
        ]
        # Select the data set based on the combo box index
        if 0 <= index < len(data_sets):
            data = data_sets[index]
        else:
            data = {}

        # Create and display the pie chart with the selected data
        self.create_pie_chart(self.top_pie_chart_view, data)
    
    def create_pie_chart(self, chart_view, data):
        """
        Helper function to create and display a pie chart with the provided data.
        """
        series = QPieSeries()
        for label, value in data.items():
            slice_ = series.append(label, value)
            slice_.setLabelVisible(True)  # Make the label visible
            slice_.setLabel(f"{label}: {value}")  # Set label to show both label and value

        chart = QChart()
        chart.addSeries(series)
        
        # Get the selected course name from the combo box
        course_name = self.ui.statComboBox.currentText()
        
        # Set the title of the new chart
        chart.setTitle(f"{course_name} : Statistics")
        
        # Set the chart to the chart view
        chart_view.setChart(chart)
        
    def create_bar_charts(self):
        # LEFT CHART: Time-based attendance
        time_slots = ["08:00 - 09:00", "09:00 - 10:00", "10:00 - 11:00", "11:00 - 12:00", "12:00 - 13:00", 
                    "13:00 - 14:00", "14:00 - 15:00", "15:00 - 16:00"]
        
        # Example attendance percentages for each time slot
        attendance_left = [40, 50, 60, 45, 70, 80, 65, 50]  # Example attendance data in percentage

        bar_set_left = QBarSet("Attendance (%)")
        bar_set_left.append(attendance_left)

        bar_series_left = QBarSeries()
        bar_series_left.append(bar_set_left)

        chart_left = QChart()
        chart_left.addSeries(bar_series_left)
        chart_left.setTitle("Hourly Attendance")

        axis_x_left = QBarCategoryAxis()
        axis_x_left.append(time_slots)  # Time slots as categories on x-axis

        axis_y_left = QValueAxis()
        axis_y_left.setRange(0, 100)  # Range from 0% to 100%

        # Set font for axis labels
        font = QFont()
        font.setPointSize(8)  # Set font size for axis labels
        axis_x_left.setLabelsFont(font)
        axis_y_left.setLabelsFont(font)

        # Rotate the X-axis labels vertically
        axis_x_left.setLabelsAngle(90)  # Rotate labels by 90 degrees (vertical)

        chart_left.setAxisX(axis_x_left, bar_series_left)
        chart_left.setAxisY(axis_y_left, bar_series_left)

        chart_view_left = QChartView(chart_left)
        chart_view_left.setRenderHint(QPainter.Antialiasing)
        
        # Add the chart to the left widget layout if not already done
        if not self.ui.statPieChartBottomLeft.layout():
            self.ui.statPieChartBottomLeft.setLayout(QVBoxLayout())  # Ensure layout is set

        self.ui.statPieChartBottomLeft.layout().addWidget(chart_view_left)

        # RIGHT CHART: Department-based attendance
        departments = ["Computer Engineering", "Electrical Engineering", "Mechanical Engineering", "Industrial Engineering"]
        
        # Example department attendance percentages
        attendance_right = [75, 60, 85, 50]  # Attendance percentages for each department

        bar_set_right = QBarSet("Attendance (%)")
        bar_set_right.append(attendance_right)

        bar_series_right = QBarSeries()
        bar_series_right.append(bar_set_right)

        chart_right = QChart()
        chart_right.addSeries(bar_series_right)
        chart_right.setTitle("Department Attendance")

        axis_x_right = QBarCategoryAxis()
        axis_x_right.append(departments)  # Departments as categories on x-axis

        axis_y_right = QValueAxis()
        axis_y_right.setRange(0, 100)  # Range from 0% to 100%

        # Set font for axis labels
        axis_x_right.setLabelsFont(font)  # Reuse the same font for consistency
        axis_y_right.setLabelsFont(font)

        # Rotate the X-axis labels vertically
        axis_x_right.setLabelsAngle(90)  # Rotate labels by 90 degrees (vertical)

        chart_right.setAxisX(axis_x_right, bar_series_right)
        chart_right.setAxisY(axis_y_right, bar_series_right)

        chart_view_right = QChartView(chart_right)
        chart_view_right.setRenderHint(QPainter.Antialiasing)

        # Add the chart to the right widget layout if not already done
        if not self.ui.statPieChartBottomRight.layout():
            self.ui.statPieChartBottomRight.setLayout(QVBoxLayout())  # Ensure layout is set

        self.ui.statPieChartBottomRight.layout().addWidget(chart_view_right)

if __name__ == "__main__":
    # Initialize the application
    app = QApplication(sys.argv)

    # Show the login window first
    login_window = LoginWindow()
    login_window.show()

    # Execute the application
    sys.exit(app.exec_())



