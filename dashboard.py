# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard_copy.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1076, 729)
        MainWindow.setMaximumSize(QtCore.QSize(1076, 729))
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons/38439452-9882-4db8-9abd-97a82dba0fd8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.icon_text_widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_text_widget.sizePolicy().hasHeightForWidth())
        self.icon_text_widget.setSizePolicy(sizePolicy)
        self.icon_text_widget.setMaximumSize(QtCore.QSize(250, 1666666))
        self.icon_text_widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.icon_text_widget.setStyleSheet("QWidget{\n"
"background-color: rgb(227, 227, 227);\n"
"text-align: left;\n"
"padding: 5px;\n"
"}\n"
"")
        self.icon_text_widget.setObjectName("icon_text_widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.icon_text_widget)
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.aguiconwide = QtWidgets.QLabel(self.icon_text_widget)
        self.aguiconwide.setMaximumSize(QtCore.QSize(80, 80))
        self.aguiconwide.setText("")
        self.aguiconwide.setPixmap(QtGui.QPixmap(":/images/icons/38439452-9882-4db8-9abd-97a82dba0fd8.png"))
        self.aguiconwide.setScaledContents(True)
        self.aguiconwide.setObjectName("aguiconwide")
        self.horizontalLayout_3.addWidget(self.aguiconwide)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelInstructorName = QtWidgets.QLabel(self.icon_text_widget)
        self.labelInstructorName.setStyleSheet("QLabel#labelInstructorName {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    \n"
"}\n"
"")
        self.labelInstructorName.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelInstructorName.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelInstructorName.setText("")
        self.labelInstructorName.setObjectName("labelInstructorName")
        self.verticalLayout.addWidget(self.labelInstructorName)
        self.labelInstructorEmail = QtWidgets.QLabel(self.icon_text_widget)
        self.labelInstructorEmail.setStyleSheet("QLabel#labelInstructorEmail {\n"
"      font-size: 14px;\n"
"    font-weight: normal;\n"
"    font-style: italic;\n"
"    color: #666;\n"
"}")
        self.labelInstructorEmail.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelInstructorEmail.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelInstructorEmail.setText("")
        self.labelInstructorEmail.setObjectName("labelInstructorEmail")
        self.verticalLayout.addWidget(self.labelInstructorEmail)
        self.dashboardbuttonwide = QtWidgets.QPushButton(self.icon_text_widget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/icons/dashboard (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dashboardbuttonwide.setIcon(icon1)
        self.dashboardbuttonwide.setCheckable(False)
        self.dashboardbuttonwide.setAutoRepeat(False)
        self.dashboardbuttonwide.setAutoExclusive(True)
        self.dashboardbuttonwide.setObjectName("dashboardbuttonwide")
        self.verticalLayout.addWidget(self.dashboardbuttonwide)
        self.attendancebuttonwide = QtWidgets.QPushButton(self.icon_text_widget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/icons/report (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.attendancebuttonwide.setIcon(icon2)
        self.attendancebuttonwide.setCheckable(False)
        self.attendancebuttonwide.setAutoExclusive(True)
        self.attendancebuttonwide.setObjectName("attendancebuttonwide")
        self.verticalLayout.addWidget(self.attendancebuttonwide)
        self.statButton = QtWidgets.QPushButton(self.icon_text_widget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/icons/trend (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.statButton.setIcon(icon3)
        self.statButton.setObjectName("statButton")
        self.verticalLayout.addWidget(self.statButton)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 355, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.logoutbuttonwide = QtWidgets.QPushButton(self.icon_text_widget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/icons/logout (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logoutbuttonwide.setIcon(icon4)
        self.logoutbuttonwide.setCheckable(False)
        self.logoutbuttonwide.setAutoExclusive(True)
        self.logoutbuttonwide.setObjectName("logoutbuttonwide")
        self.verticalLayout_5.addWidget(self.logoutbuttonwide)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.horizontalLayout_5.addWidget(self.icon_text_widget)
        self.main_screen_widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_screen_widget.sizePolicy().hasHeightForWidth())
        self.main_screen_widget.setSizePolicy(sizePolicy)
        self.main_screen_widget.setMaximumSize(QtCore.QSize(861, 841))
        self.main_screen_widget.setObjectName("main_screen_widget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.main_screen_widget)
        self.verticalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.header_widget = QtWidgets.QWidget(self.main_screen_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_widget.sizePolicy().hasHeightForWidth())
        self.header_widget.setSizePolicy(sizePolicy)
        self.header_widget.setMaximumSize(QtCore.QSize(16777215, 120))
        self.header_widget.setMouseTracking(True)
        self.header_widget.setStyleSheet("QWidget{\n"
"background-color: rgb(227, 227, 227);\n"
"text-align: left;\n"
"padding: 5px;\n"
"}\n"
"")
        self.header_widget.setObjectName("header_widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.header_widget)
        self.horizontalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_7.addWidget(self.header_widget)
        self.mainscreen = QtWidgets.QStackedWidget(self.main_screen_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.mainscreen.sizePolicy().hasHeightForWidth())
        self.mainscreen.setSizePolicy(sizePolicy)
        self.mainscreen.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.mainscreen.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.mainscreen.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.mainscreen.setLineWidth(2)
        self.mainscreen.setMidLineWidth(4)
        self.mainscreen.setObjectName("mainscreen")
        self.dashboardpage = QtWidgets.QWidget()
        self.dashboardpage.setObjectName("dashboardpage")
        self.gridLayout = QtWidgets.QGridLayout(self.dashboardpage)
        self.gridLayout.setObjectName("gridLayout")
        self.course_widget = QtWidgets.QWidget(self.dashboardpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.course_widget.sizePolicy().hasHeightForWidth())
        self.course_widget.setSizePolicy(sizePolicy)
        self.course_widget.setObjectName("course_widget")
        self.layoutWidget = QtWidgets.QWidget(self.course_widget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 791, 631))
        self.layoutWidget.setObjectName("layoutWidget")
        self.course_layout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.course_layout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.course_layout.setContentsMargins(15, 15, 15, 15)
        self.course_layout.setObjectName("course_layout")
        self.coursesButtonDynamic = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coursesButtonDynamic.sizePolicy().hasHeightForWidth())
        self.coursesButtonDynamic.setSizePolicy(sizePolicy)
        self.coursesButtonDynamic.setStyleSheet("background-color: rgb(130, 28, 23);")
        self.coursesButtonDynamic.setCheckable(True)
        self.coursesButtonDynamic.setAutoExclusive(True)
        self.coursesButtonDynamic.setObjectName("coursesButtonDynamic")
        self.course_layout.addWidget(self.coursesButtonDynamic)
        self.gridLayout.addWidget(self.course_widget, 0, 0, 1, 1)
        self.mainscreen.addWidget(self.dashboardpage)
        self.notificationspage = QtWidgets.QWidget()
        self.notificationspage.setObjectName("notificationspage")
        self.notifications = QtWidgets.QLabel(self.notificationspage)
        self.notifications.setGeometry(QtCore.QRect(20, 10, 761, 751))
        self.notifications.setObjectName("notifications")
        self.mainscreen.addWidget(self.notificationspage)
        self.Coursespage = QtWidgets.QWidget()
        self.Coursespage.setObjectName("Coursespage")
        self.mainscreen.addWidget(self.Coursespage)
        self.Attendancepage = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Attendancepage.sizePolicy().hasHeightForWidth())
        self.Attendancepage.setSizePolicy(sizePolicy)
        self.Attendancepage.setObjectName("Attendancepage")
        self.splitter = QtWidgets.QSplitter(self.Attendancepage)
        self.splitter.setGeometry(QtCore.QRect(20, 20, 791, 621))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setMinimumSize(QtCore.QSize(563, 0))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.coursesComboBox = QtWidgets.QComboBox(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coursesComboBox.sizePolicy().hasHeightForWidth())
        self.coursesComboBox.setSizePolicy(sizePolicy)
        self.coursesComboBox.setMinimumSize(QtCore.QSize(161, 0))
        self.coursesComboBox.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: lightgray;\n"
"}")
        self.coursesComboBox.setObjectName("coursesComboBox")
        self.coursesComboBox.addItem("")
        self.coursesComboBox.addItem("")
        self.coursesComboBox.addItem("")
        self.verticalLayout_2.addWidget(self.coursesComboBox)
        self.Export_to_Excel = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Export_to_Excel.sizePolicy().hasHeightForWidth())
        self.Export_to_Excel.setSizePolicy(sizePolicy)
        self.Export_to_Excel.setObjectName("Export_to_Excel")
        self.verticalLayout_2.addWidget(self.Export_to_Excel)
        self.submitbutton = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submitbutton.sizePolicy().hasHeightForWidth())
        self.submitbutton.setSizePolicy(sizePolicy)
        self.submitbutton.setStyleSheet("background-color: rgb(130, 28, 23);")
        self.submitbutton.setCheckable(False)
        self.submitbutton.setAutoExclusive(True)
        self.submitbutton.setObjectName("submitbutton")
        self.verticalLayout_2.addWidget(self.submitbutton)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        self.calendarWidget.setStyleSheet("QCalendarWidget {\n"
"    background-color: rgb(154, 153, 150);  /* Soft gray background */\n"
"    border: 1px solid rgb(190, 190, 190);  /* Subtle border */\n"
"    border-radius: 20px;  /* Rounded corners */\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"    background-color: rgb(154, 153, 150);  /* Medium gray for navigation buttons */\n"
"    color: black;  /* Black text */\n"
"    font-size: 14px;\n"
"    height: 20px;\n"
"    width: 90px;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    margin: 3px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton::hover {\n"
"    background-color: rgb(180, 180, 180);  /* Darker gray on hover */\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView {\n"
"    background-color: rgb(240, 240, 240);  /* Light background for days */\n"
"    selection-background-color: rgb(160, 160, 160);  /* Dark gray for selected day */\n"
"    selection-color: white;  /* White text for selected day */\n"
"    font-size: 16px;\n"
"    gridline-color: rgb(0, 0, 0);  /* Light grid lines */\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"     /* Slightly darker alternate background */\n"
"    \n"
"    alternate-background-color: rgb(154, 153, 150);\n"
"}\n"
"\n"
"QCalendarWidget QHeaderView::section {\n"
"    background-color: rgb(154, 153, 150);  /* Light gray for header */\n"
"    color: black;  /* Black text */\n"
"    font-size: 13px;\n"
"    border: 1px solid rgb(190, 190, 190);  /* Border for header sections */\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox {\n"
"    background-color: rgb(154, 153, 150);  /* Spinbox background */\n"
"    border: 1px solid rgb(190, 190, 190);  /* Border */\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::up-button, QCalendarWidget QSpinBox::down-button {\n"
"    background-color: rgb(210, 210, 210);  /* Same as spinbox background */\n"
"    border: none;\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::up-button::hover, QCalendarWidget QSpinBox::down-button::hover {\n"
"    background-color: rgb(180, 180, 180);  /* Darker gray on hover */\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::up-arrow, QCalendarWidget QSpinBox::down-arrow {\n"
"    width: 7px;\n"
"    height: 7px;\n"
"}\n"
"")
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout_2.addWidget(self.calendarWidget, 0, 0, 1, 1)
        self.attendanceTableWidget = QtWidgets.QTableWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attendanceTableWidget.sizePolicy().hasHeightForWidth())
        self.attendanceTableWidget.setSizePolicy(sizePolicy)
        self.attendanceTableWidget.setMinimumSize(QtCore.QSize(404, 600))
        self.attendanceTableWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.attendanceTableWidget.setStyleSheet("")
        self.attendanceTableWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.attendanceTableWidget.setObjectName("attendanceTableWidget")
        self.attendanceTableWidget.setColumnCount(2)
        self.attendanceTableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.attendanceTableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.attendanceTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.attendanceTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.attendanceTableWidget.setItem(0, 0, item)
        self.mainscreen.addWidget(self.Attendancepage)
        self.PolicyPage = QtWidgets.QWidget()
        self.PolicyPage.setObjectName("PolicyPage")
        self.Policy = QtWidgets.QLabel(self.PolicyPage)
        self.Policy.setGeometry(QtCore.QRect(10, 10, 771, 751))
        self.Policy.setObjectName("Policy")
        self.mainscreen.addWidget(self.PolicyPage)
        self.StatisticsPage = QtWidgets.QWidget()
        self.StatisticsPage.setObjectName("StatisticsPage")
        self.layoutWidget2 = QtWidgets.QWidget(self.StatisticsPage)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 340, 801, 341))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.statPieChartBottomLeft = QtWidgets.QWidget(self.layoutWidget2)
        self.statPieChartBottomLeft.setObjectName("statPieChartBottomLeft")
        self.horizontalLayout_2.addWidget(self.statPieChartBottomLeft)
        self.statPieChartBottomRight = QtWidgets.QWidget(self.layoutWidget2)
        self.statPieChartBottomRight.setObjectName("statPieChartBottomRight")
        self.horizontalLayout_2.addWidget(self.statPieChartBottomRight)
        self.layoutWidget3 = QtWidgets.QWidget(self.StatisticsPage)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 10, 801, 321))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.statComboBox = QtWidgets.QComboBox(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statComboBox.sizePolicy().hasHeightForWidth())
        self.statComboBox.setSizePolicy(sizePolicy)
        self.statComboBox.setObjectName("statComboBox")
        self.horizontalLayout_6.addWidget(self.statComboBox)
        spacerItem3 = QtWidgets.QSpacerItem(450, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.StatPieChartTop = QtWidgets.QWidget(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StatPieChartTop.sizePolicy().hasHeightForWidth())
        self.StatPieChartTop.setSizePolicy(sizePolicy)
        self.StatPieChartTop.setObjectName("StatPieChartTop")
        self.verticalLayout_3.addWidget(self.StatPieChartTop)
        self.mainscreen.addWidget(self.StatisticsPage)
        self.HelpPage = QtWidgets.QWidget()
        self.HelpPage.setObjectName("HelpPage")
        self.Help = QtWidgets.QLabel(self.HelpPage)
        self.Help.setGeometry(QtCore.QRect(10, 20, 771, 741))
        self.Help.setObjectName("Help")
        self.mainscreen.addWidget(self.HelpPage)
        self.SettingsPage = QtWidgets.QWidget()
        self.SettingsPage.setObjectName("SettingsPage")
        self.Settings = QtWidgets.QLabel(self.SettingsPage)
        self.Settings.setGeometry(QtCore.QRect(10, 10, 771, 751))
        self.Settings.setObjectName("Settings")
        self.mainscreen.addWidget(self.SettingsPage)
        self.ProfilePage = QtWidgets.QWidget()
        self.ProfilePage.setObjectName("ProfilePage")
        self.Profile = QtWidgets.QLabel(self.ProfilePage)
        self.Profile.setGeometry(QtCore.QRect(10, 10, 771, 751))
        self.Profile.setObjectName("Profile")
        self.mainscreen.addWidget(self.ProfilePage)
        self.SearchPage = QtWidgets.QWidget()
        self.SearchPage.setObjectName("SearchPage")
        self.Search = QtWidgets.QLabel(self.SearchPage)
        self.Search.setGeometry(QtCore.QRect(20, 20, 761, 741))
        self.Search.setObjectName("Search")
        self.mainscreen.addWidget(self.SearchPage)
        self.coursePage = QtWidgets.QWidget()
        self.coursePage.setObjectName("coursePage")
        self.lineEdit = QtWidgets.QLineEdit(self.coursePage)
        self.lineEdit.setGeometry(QtCore.QRect(50, 80, 411, 241))
        self.lineEdit.setObjectName("lineEdit")
        self.mainscreen.addWidget(self.coursePage)
        self.verticalLayout_7.addWidget(self.mainscreen)
        self.horizontalLayout_5.addWidget(self.main_screen_widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.mainscreen.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Attendance Tracking"))
        MainWindow.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.dashboardbuttonwide.setText(_translate("MainWindow", "Dashboard"))
        self.attendancebuttonwide.setText(_translate("MainWindow", "Attendance"))
        self.statButton.setText(_translate("MainWindow", "Statistics"))
        self.logoutbuttonwide.setText(_translate("MainWindow", "Log Out"))
        self.coursesButtonDynamic.setText(_translate("MainWindow", "Internet Of Things"))
        self.notifications.setText(_translate("MainWindow", "Notifications"))
        self.coursesComboBox.setItemText(0, _translate("MainWindow", "courseName"))
        self.coursesComboBox.setItemText(1, _translate("MainWindow", "IOT"))
        self.coursesComboBox.setItemText(2, _translate("MainWindow", "COMP413"))
        self.Export_to_Excel.setText(_translate("MainWindow", "Export to Excel"))
        self.submitbutton.setText(_translate("MainWindow", "Submit"))
        item = self.attendanceTableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "asdasdasd"))
        item = self.attendanceTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "adasd"))
        item = self.attendanceTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "asdasd"))
        __sortingEnabled = self.attendanceTableWidget.isSortingEnabled()
        self.attendanceTableWidget.setSortingEnabled(False)
        item = self.attendanceTableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "asd"))
        self.attendanceTableWidget.setSortingEnabled(__sortingEnabled)
        self.Policy.setText(_translate("MainWindow", "Policy"))
        self.Help.setText(_translate("MainWindow", "Help"))
        self.Settings.setText(_translate("MainWindow", "Settings"))
        self.Profile.setText(_translate("MainWindow", "Profile"))
        self.Search.setText(_translate("MainWindow", "Search"))
        self.lineEdit.setText(_translate("MainWindow", "course"))
import resoruces_rc
