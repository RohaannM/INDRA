import sys
import ast
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QDialog, QFrame, QSpacerItem, QSizePolicy, QMainWindow

from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from registration1 import SignUpWindow
import importlib.util

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setGeometry(300, 200, 925, 500)
        self.setFixedSize(925, 500)
        self.setStyleSheet("background-color: white;")

        self.initUI()

    def initUI(self):
        main_layout = QHBoxLayout()

        # Left frame for the image
        
        left_frame = QFrame(self)
        left_frame.setFixedSize(462, 500)
        left_frame.setStyleSheet("background-color: #ffffff;")
        left_frame_layout = QVBoxLayout(left_frame)
        left_frame_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.img_label = QLabel(left_frame)
        pixmap = QPixmap("login.png")
        self.img_label.setPixmap(pixmap)
        left_frame_layout.addWidget(self.img_label)

        # Right frame for the login form
        right_frame = QFrame(self)
        right_frame.setFixedSize(463, 500)
        right_frame.setStyleSheet("background-color: white;")
        right_frame_layout = QVBoxLayout(right_frame)
        right_frame_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.heading = QLabel("Sign in")
        self.heading.setStyleSheet("color: #57a1f8; font-size: 23px; font-weight: bold; font-family: 'Microsoft YaHei UI Light';")
        self.heading.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the heading
        right_frame_layout.addWidget(self.heading)

        right_frame_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum))

        self.user = QLineEdit(self)
        self.user.setPlaceholderText("Username")
        self.user.setStyleSheet("color: black;")
        self.user.setFixedWidth(300)
        right_frame_layout.addWidget(self.user)

        right_frame_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum))


        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Password")
        self.password.setStyleSheet("color: black;")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password.setFixedWidth(300)
        right_frame_layout.addWidget(self.password)

        self.signin_btn = QPushButton("Sign in", self)
        self.signin_btn.setStyleSheet("background-color: #57a1f8; color: white; padding: 7px; border: none;")
        self.signin_btn.clicked.connect(self.signin)
        right_frame_layout.addWidget(self.signin_btn)

        signup_layout = QHBoxLayout()
        self.signup_label = QLabel("Don't have an account?")
        self.signup_label.setStyleSheet("color: black;")
        signup_layout.addWidget(self.signup_label)

        self.signup_btn = QPushButton("Sign up", self)
        self.signup_btn.setStyleSheet("background-color: white; color: #57a1f8; border: none;")
        self.signup_btn.clicked.connect(self.show_signup)
        signup_layout.addWidget(self.signup_btn)

        signup_layout.setSpacing(5)  # Reduce space between label and button
        signup_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        right_frame_layout.addLayout(signup_layout)

        main_layout.addWidget(left_frame)
        main_layout.addWidget(right_frame)

        self.setLayout(main_layout)

    def signin(self):
        username = self.user.text()
        password = self.password.text()

        try:
            with open('datasheet.txt', 'r') as file:
                d = file.read()
                r = ast.literal_eval(d)
        except:
            r = {}

        if username in r and r[username] == password:
            self.openAppWindow()
        else:
            msg_box = QMessageBox(QMessageBox.Icon.Critical, "Invalid", "Invalid username or password", parent=self)
            msg_box.setStyleSheet("""
        QLabel { color: black; }
        QMessageBox QPushButton {
            background-color: #57a1f8;  /* Button background color */
            color: white;              /* Button text color */
            border: 2px solid #006bb3; /* Button border color and width */
            border-radius: 5px;        /* Rounded corners for the border */
            padding: 5px 10px;         /* Padding inside the button */
        }
        QMessageBox QPushButton:hover {
            background-color: #4591e0; /* Button background color on hover */
            border: 2px solid #0056a0; /* Button border color on hover */
        }
        QMessageBox QPushButton:pressed {
            background-color: #357ab8; /* Button background color when pressed */
            border: 2px solid #004080; /* Button border color when pressed */
        }
    """)
            msg_box.exec()

    def openAppWindow(self):
        # Dynamically import the ui_side_bar4.py file
        module_name = 'ui_new_side_bar4'
        file_path = 'E:/new_streetlight/ui_new_side_bar4.py'  # Adjust the path accordingly

        spec = importlib.util.spec_from_file_location(module_name, file_path)
        ui_side_bar_module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = ui_side_bar_module
        spec.loader.exec_module(ui_side_bar_module)

        # Assuming ui_side_bar4.py contains a class named Ui_MainWindow
        if hasattr(ui_side_bar_module, 'Ui_MainWindow'):
            self.appWindow = QMainWindow()
            ui = ui_side_bar_module.Ui_MainWindow()
            ui.setupUi(self.appWindow)
            self.appWindow.show()
        else:
            # Fallback if the module does not contain the expected class
            self.appWindow = QDialog()
            self.appWindow.setWindowTitle("App")
            self.appWindow.setGeometry(300, 200, 925, 500)
            self.appWindow.setFixedSize(925, 500)
            self.appWindow.setStyleSheet("background-color: white;")

            label = QLabel("Failed to load Ui_MainWindow!", self.appWindow)
            label.setStyleSheet("font-size: 20px; font-weight: bold; color: red;")
            layout = QVBoxLayout()
            layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(label)
            self.appWindow.setLayout(layout)

            self.appWindow.exec()
    
    def show_signup(self):
        self.close()
        self.signup_window = SignUpWindow()
        self.signup_window.setParent(self, Qt.WindowType.Window)
        self.signup_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
