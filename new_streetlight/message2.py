import sys
import socket
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QInputDialog
)
from PyQt6.QtCore import QThread, pyqtSignal, Qt
from PyQt6.QtGui import QTextCharFormat, QColor, QTextCursor, QTextBlockFormat, QIcon

class ClientThread(QThread):
    message_received = pyqtSignal(str)

    def __init__(self, server_ip, server_port=12345):
        super().__init__()
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.server_ip, self.server_port))
        self.running = True

    def run(self):
        while self.running:
            try:
                response = self.client_socket.recv(1024).decode()
                if response:
                    self.message_received.emit(response)
            except ConnectionResetError:
                break   

    def send_message(self, message):
        self.client_socket.send(message.encode())

    def stop(self):
        self.running = False
        self.client_socket.close()

class ClientApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Client")
        self.setGeometry(100, 100, 600, 400)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.line_edit = QLineEdit()
        self.send_button = QPushButton()
        self.send_button.setIcon(QIcon("icons/send.svg"))  # Set the path to your send icon image
        self.send_button.clicked.connect(self.send_message)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.line_edit)
        input_layout.addWidget(self.send_button)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addLayout(input_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.client_thread = None

    def start_client(self, server_ip):
        self.client_thread = ClientThread(server_ip)
        self.client_thread.message_received.connect(self.display_received_message)
        self.client_thread.start()

    def send_message(self):
        message = self.line_edit.text()
        self.client_thread.send_message(message)
        self.display_sent_message(message)
        self.line_edit.clear()

    def display_sent_message(self, message):
        format = QTextCharFormat()
        format.setForeground(QColor("blue"))

        cursor = self.text_edit.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        cursor.setBlockFormat(self.get_right_aligned_format())
        cursor.insertText(f"Sent: {message}\n", format)

        self.text_edit.setTextCursor(cursor)

    def display_received_message(self, message):
        format = QTextCharFormat()
        format.setForeground(QColor("green"))

        cursor = self.text_edit.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        cursor.setBlockFormat(self.get_left_aligned_format())
        cursor.insertText(f"Received: {message}\n", format)

        self.text_edit.setTextCursor(cursor)

    def get_left_aligned_format(self):
        block_format = QTextBlockFormat()
        block_format.setAlignment(Qt.AlignmentFlag.AlignLeft)
        return block_format

    def get_right_aligned_format(self):
        block_format = QTextBlockFormat()
        block_format.setAlignment(Qt.AlignmentFlag.AlignRight)
        return block_format

    def closeEvent(self, event):
        if self.client_thread:
            self.client_thread.stop()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClientApp()

    server_ip, ok = QInputDialog.getText(window, "Server IP", "Enter server IP address:")
    if ok:
        window.start_client(server_ip)
        window.show()
        sys.exit(app.exec())
