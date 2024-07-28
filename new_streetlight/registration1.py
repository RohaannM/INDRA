import sys
import ast
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QFormLayout, QMessageBox, QFrame, QSpacerItem, QSizePolicy
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class SignUpWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SignUp")
        self.setGeometry(300, 200, 925, 500)
        self.setFixedSize(925, 500)
        self.setStyleSheet("background-color: white;")

        self.initUI()

    def initUI(self):
        main_layout = QHBoxLayout()

        # Left frame for the image
        left_frame = QFrame(self)
        left_frame.setFixedSize(462, 500)
        left_frame.setStyleSheet("background-color: #fff;")
        left_frame_layout = QVBoxLayout(left_frame)
        left_frame_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.img_label = QLabel(left_frame)
        pixmap = QPixmap("login (1).png")
        self.img_label.setPixmap(pixmap)
        self.img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        left_frame_layout.addWidget(self.img_label)

        # Right frame for the signup form
        right_frame = QFrame(self)
        right_frame.setFixedSize(463, 500)
        right_frame.setStyleSheet("background-color: white;")
        right_frame_layout = QVBoxLayout(right_frame)
        right_frame_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        right_frame_layout.setContentsMargins(30, 30, 30, 30)  # Add margin around the content

        # Heading
        self.heading = QLabel("SignUp")
        self.heading.setStyleSheet("color: #57a1f8; font-size: 23px; font-weight: bold; font-family: 'Microsoft YaHei UI Light';")
        self.heading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        right_frame_layout.addWidget(self.heading)

        # Form Layout
        form_layout = QVBoxLayout()  # Use QVBoxLayout for vertical arrangement
        form_layout.setSpacing(20)  # Add spacing between form fields

        # Username field
        self.user = QLineEdit()
        self.user.setPlaceholderText("Username")
        self.user.setStyleSheet("color: black;")
        self.user.setFixedWidth(300)
        form_layout.addWidget(self.user)

        # Password field
        self.code = QLineEdit()
        self.code.setPlaceholderText("Password")
        self.code.setStyleSheet("color: black;")
        self.code.setEchoMode(QLineEdit.EchoMode.Password)
        self.code.setFixedWidth(300)
        form_layout.addWidget(self.code)

        # Confirm Password field
        self.conform_code = QLineEdit()
        self.conform_code.setPlaceholderText("Confirm Password")
        self.conform_code.setStyleSheet("color: black;")
        self.conform_code.setEchoMode(QLineEdit.EchoMode.Password)
        self.conform_code.setFixedWidth(300)
        form_layout.addWidget(self.conform_code)

        right_frame_layout.addLayout(form_layout)

        # SignUp Button
        self.sign_up_btn = QPushButton("Sign Up")
        self.sign_up_btn.setStyleSheet("background-color: #57a1f8; color: white; padding: 7px; border: none;")
        self.sign_up_btn.setFixedWidth(300)  # Match the width with input fields
        self.sign_up_btn.clicked.connect(self.signup)
        form_layout.addWidget(self.sign_up_btn)

        # Account label and Sign in button
        signup_layout = QHBoxLayout()
        self.signup_label = QLabel("I have an account")
        self.signup_label.setStyleSheet("color: black;")
        signup_layout.addWidget(self.signup_label)

        self.signin_btn = QPushButton("Sign in")
        self.signin_btn.setStyleSheet("background-color: white; color: #57a1f8; border: none;")
        self.signin_btn.clicked.connect(self.show_login)
        signup_layout.addWidget(self.signin_btn)

        # Adjust spacing and alignment
        signup_layout.setSpacing(10)  # Space between label and button
        signup_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        right_frame_layout.addLayout(signup_layout)

    
        main_layout.addWidget(left_frame)
        main_layout.addWidget(right_frame)

        self.setLayout(main_layout)


    def signup(self):
        username = self.user.text()
        password = self.code.text()
        conform_password = self.conform_code.text()

        if password == conform_password:
            try:
                with open('datasheet.txt', 'r+') as file:
                    d = file.read()
                    try:
                        r = ast.literal_eval(d)
                    except:
                        r = {}

                    r[username] = password
                    file.seek(0)
                    file.truncate()
                    file.write(str(r))

                    msg_box = QMessageBox(QMessageBox.Icon.Critical, "Success", "Registration Successfull", parent=self)
                    msg_box.setStyleSheet("""
        QLabel { color: black; }
        QMessageBox QPushButton {
            background-color: #57a1f8;  
            color: white;              
            border: 2px solid #006bb3; 
            border-radius: 5px;        
            padding: 5px 10px;         
        }
        QMessageBox QPushButton:hover {
            background-color: #4591e0; 
            border: 2px solid #0056a0; 
        }
        QMessageBox QPushButton:pressed {
            background-color: #357ab8; 
            border: 2px solid #004080; /* Button border color when pressed */
        }
    """)
                msg_box.exec()

            except FileNotFoundError:
                with open('datasheet.txt', 'w') as file:
                    file.write(str({username: password}))

        else:
            msg_box = QMessageBox(QMessageBox.Icon.Critical, "Invalid", "Password doenot match", parent=self)
            msg_box.setStyleSheet("""
            QLabel { color: black; }
            QMessageBox QPushButton {
            background-color: #57a1f8;  
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

    def show_login(self):
        self.close()
        if self.parent():
            self.parent().show()   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SignUpWindow()
    window.show()
    sys.exit(app.exec())
