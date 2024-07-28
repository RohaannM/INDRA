import sys
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton
from PyQt6.QtCore import QTimer
import MySQLdb as mdb

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.table_widget = QTableWidget()
        self.blinking_button = QPushButton("Blinking Button")
        self.blinking_button.setStyleSheet("background-color: lightgray;")

        layout = QVBoxLayout(self)
        layout.addWidget(self.table_widget)
        layout.addWidget(self.blinking_button)

        # Create a timer for automatic refresh
        self.refresh_timer = QTimer(self)
        self.refresh_timer.timeout.connect(self.refresh_data)
        self.refresh_timer.start(3000)  # Refresh every 3000 ms (3 seconds)

        self.blink_timer = QTimer(self)
        self.blink_timer.timeout.connect(self.blink_button)
        self.blink_state = False
        self.error_count = 0

        self.refresh_data()

    def refresh_data(self):
        # Database connection details
        host = 'localhost'
        user = 'root'  # Replace with your MySQL username
        password = ''  # Replace with your MySQL password
        database = 'esp32_data'

        try:
            # Connect to the database
            conn = mdb.connect(host=host, user=user, passwd=password, db=database)
            cursor = conn.cursor()

            # Query the table for rows where val1 or val2 is 0
            query = "SELECT id, val1, val2 FROM project WHERE val1 = 0 OR val2 = 0"
            cursor.execute(query)
            rows = cursor.fetchall()

            # Set the table row and column count
            self.table_widget.setRowCount(len(rows))
            self.table_widget.setColumnCount(4)
            self.table_widget.setHorizontalHeaderLabels(['ID', 'val1', 'val2', 'Error'])

            # Populate the table with data
            self.error_count = 0
            for row_index, row in enumerate(rows):
                id, val1, val2 = row
                errors = []
                if val1 == 0:
                    errors.append("ldr is having issue")
                if val2 == 0:
                    errors.append("asci error")
                error_msg = ', '.join(errors)

                self.table_widget.setItem(row_index, 0, QTableWidgetItem(str(id)))
                self.table_widget.setItem(row_index, 1, QTableWidgetItem(str(val1)))
                self.table_widget.setItem(row_index, 2, QTableWidgetItem(str(val2)))
                self.table_widget.setItem(row_index, 3, QTableWidgetItem(error_msg))

                if errors:
                    self.error_count += 1

            # Resize columns to fit the contents
            self.table_widget.resizeColumnsToContents()

            # Optionally, set a minimum width for each column
            for i in range(4):
                self.table_widget.setColumnWidth(i, 200)  # Set all columns to have at least 200 width

            if self.error_count > 0:
                self.start_blinking()
            else:
                self.stop_blinking()

        except mdb.Error as e:
            print(f"Error connecting to MySQL database: {e}")
        finally:
            if conn:
                conn.close()

    def start_blinking(self):
        self.blinking_button.setText(f"{self.error_count} Error(s) Found")
        self.blink_timer.start(500)  # Blink every 500 ms

    def stop_blinking(self):
        self.blinking_button.setStyleSheet("background-color: lightgray;")
        self.blinking_button.setText("Blinking Button")
        self.blink_timer.stop()

    def blink_button(self):
        if self.blink_state:
            self.blinking_button.setStyleSheet("background-color: lightgray;")
        else:
            self.blinking_button.setStyleSheet("background-color: red;")
        self.blink_state = not self.blink_state

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
