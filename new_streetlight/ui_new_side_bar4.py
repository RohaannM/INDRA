from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt, Slot
from PySide6.QtGui import QIcon, QFont
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame, QStackedWidget, QSizePolicy, QApplication, QMessageBox, QComboBox, QTableWidget, QTableWidgetItem,  QFrame
from PySide6.QtWebEngineWidgets import QWebEngineView
import folium
import io
import sys
import MySQLdb as mdb  # Ensure you have the MySQLdb module installed
from Custom_Widgets.Widgets import QCustomSlideMenu
from PySide6.QtCore import Qt
from PyQt6.QtGui import QTextCharFormat, QColor, QTextCursor, QTextBlockFormat
import icons_rc
from message3 import ClientApp
from database2 import MainWindow as DatabaseWindow
from PyQt6.QtCore import QTimer


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(708, 395)

        # Central Widget Setup
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
                                          " border:none;\n"
                                          "background-color:transparent;\n"
                                          "color:#fff\n"
                                          "}\n"
                                          "#centralwidget{\n"
                                          " background-color:#040f13;\n"
                                          "}\n"
                                          "#side_menu{\n"
                                          " background-color:#071e26;\n"
                                          " border-radius:20px;\n"
                                          "}\n"
                                          "QPushButton{\n"
                                          " padding:10px;\n"
                                          " background-color:#040f13;\n"
                                          " border-radius:5px;\n"
                                          "}\n"
                                          "#mainbody{\n"
                                          " background-color:#071e26;\n"
                                          " border-radius:10px;\n"
                                          "}")

        # Main Layout
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")

        # Header Setup
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 50))
        self.header.setMaximumSize(QSize(16777215, 50))
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)

        # Header Layout
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        # Header Left Section - Menu Button
        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 30))
        self.frame_3.setMaximumSize(QSize(16777215, 30))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.MENU = QPushButton(self.frame_3)
        self.MENU.setObjectName(u"MENU")
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.MENU.setIcon(icon)
        self.MENU.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.MENU)
        self.horizontalLayout_2.addWidget(self.frame_3, 0)
        self.horizontalLayout_2.setAlignment(Qt.AlignLeft)

        # Header Center Section - Title
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)
        self.horizontalLayout_2.addWidget(self.frame)
        self.verticalLayout.addWidget(self.header)

        # Side Menu Setup
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.side_menu = QCustomSlideMenu(self.frame_2)
        self.side_menu.setObjectName(u"side_menu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.side_menu.sizePolicy().hasHeightForWidth())
        self.side_menu.setSizePolicy(sizePolicy1)
        self.side_menu.setMaximumSize(QSize(150, 16777215))  # Set a valid maximum size
        self.verticalLayout_2 = QVBoxLayout(self.side_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        # Side Menu Buttons
        self.frame_4 = QFrame(self.side_menu)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(150, 0))
        self.frame_4.setMaximumSize(QSize(150, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(24, 21))
        self.pushButton_2.setStyleSheet("QPushButton { text-align: left; padding-left: 30px; }")
        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/message-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(24, 24))
        self.pushButton_3.setStyleSheet("QPushButton { text-align: left; padding-left: 30px; }")
        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/bell (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(24, 24))
        self.pushButton_4.setStyleSheet("QPushButton { text-align: left; padding-left: 30px; }")
        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_4)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QSize(24, 24))
        self.pushButton_5.setStyleSheet("QPushButton { text-align: left; padding-left: 30px; }")
        self.verticalLayout_3.addWidget(self.pushButton_5)

        self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignTop)
        self.horizontalLayout.addWidget(self.side_menu)

        self.mainbody = QStackedWidget(self.frame_2)
        self.mainbody.setObjectName(u"mainbody")
        self.mainbody.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainbody.sizePolicy().hasHeightForWidth())
        self.mainbody.setSizePolicy(sizePolicy2)

        # Adding Pages to Main Body
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.page1_layout = QVBoxLayout(self.page1)
        self.page1_layout.setObjectName(u"page1_layout")

        self.frame_a = QFrame(self.page1)
        self.frame_a.setObjectName(u"frame_a")
        self.frame_a.setStyleSheet("background-color: white;")
        self.frame_a.setFrameShape(QFrame.StyledPanel)
        self.frame_a.setFrameShadow(QFrame.Raised)

        self.frame_b = QFrame(self.page1)
        self.frame_b.setObjectName(u"frame_b")
        self.frame_b.setFrameShape(QFrame.StyledPanel)
        self.frame_b.setFrameShadow(QFrame.Raised)

        self.page1_layout.addWidget(self.frame_a)
        self.page1_layout.addWidget(self.frame_b)
        self.mainbody.addWidget(self.page1)

        # Page 2
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.page2.setStyleSheet(u"*{\n"
                         " background-color:#040f13;\n"
                         "}")

        # Add horizontal layout for the frames
        self.page2Layout = QHBoxLayout(self.page2)

        # Create first frame (white)
        self.frame_white = QFrame(self.page2)
        self.frame_white.setStyleSheet("background-color: white;")
        self.frame_white.setFrameShape(QFrame.StyledPanel)
        self.frame_white.setFrameShadow(QFrame.Raised)

        # Create vertical layout for buttons in frame_white
        self.frame_white_layout = QVBoxLayout(self.frame_white)

        # Create and add buttons to frame_white
        self.button_ip1 = QPushButton("Connect to IP1", self.frame_white)
        self.button_ip1.setStyleSheet("color: black;")
        self.button_ip1.clicked.connect(lambda: self.connect_to_server("192.168.182.133"))
        self.frame_white_layout.addWidget(self.button_ip1)

        self.button_ip2 = QPushButton("Connect to IP2", self.frame_white)
        self.button_ip2.setStyleSheet("color: black;")
        self.button_ip2.clicked.connect(lambda: self.connect_to_server("192.168.182.15"))
        self.frame_white_layout.addWidget(self.button_ip2)

        self.button_ip3 = QPushButton("Connect to IP3", self.frame_white)
        self.button_ip3.setStyleSheet("color: black;")
        self.button_ip3.clicked.connect(lambda: self.connect_to_server("192.168.1.3"))
        self.frame_white_layout.addWidget(self.button_ip3)

        self.page2Layout.addWidget(self.frame_white)


        # Create second frame (grey)
        self.frame_grey = QFrame(self.page2)
        #self.frame_grey.setStyleSheet("background-color: grey;")
        self.frame_grey.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_grey.setFrameShadow(QFrame.Raised)

        # Add frames to the layout with stretch factors
        self.page2Layout.addWidget(self.frame_white, 1)  # Stretch factor 1
  

        self.frame_grey_layout = QVBoxLayout(self.frame_grey)  # Ensure self.frame_grey is a QWidget

        # Instantiate ClientApp
        self.client_app = ClientApp()

        # Create a central widget and set its layout
        central_widget1 = QWidget()
        frame_grey_layout = QVBoxLayout()  # Initialize a new layout for central_widget1
        central_widget1.setLayout(frame_grey_layout)

        # Add the central widget to your frame_grey_layout
        self.frame_grey_layout.addChildWidget(central_widget1)  # Add central_widget1 to frame_grey_layout

        # Add frame_grey to the page2 layout with stretch factor
        self.page2Layout.addWidget(self.frame_grey, 4) 
        self.mainbody.addWidget(self.page2)
        # Page 3
        self.page3_container = QWidget()
        self.page3_layout = QVBoxLayout(self.page3_container)
        self.table_widget = QTableWidget()
        self.blinking_button = QPushButton("Blinking Button")
        self.blinking_button.setStyleSheet("background-color: lightgray;")

        self.page3_layout.addWidget(self.table_widget)
        self.page3_layout.addWidget(self.blinking_button)
        self.mainbody.addWidget(self.page3_container)

        #Page 4
        self.page4 = QLabel("This is page 4")
        self.page4.setAlignment(Qt.AlignCenter) 
        self.mainbody.addWidget(self.page4)
        self.horizontalLayout.addWidget(self.mainbody)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        # Retranslate UI Method
        self.retranslateUi(MainWindow)

        # Connect Buttons to Slots
        self.pushButton_2.clicked.connect(lambda: self.change_page(0))
        self.pushButton_3.clicked.connect(lambda: self.change_page(1))
        self.pushButton_4.clicked.connect(lambda: self.change_page(2))
        self.pushButton_5.clicked.connect(lambda: self.change_page(3))

        self.refresh_timer = QTimer()
        self.refresh_timer.timeout.connect(self.refresh_data)
        self.refresh_timer.start(3000)  # Refresh every 3000 ms (3 seconds)

        self.blink_timer = QTimer()
        self.blink_timer.timeout.connect(self.blink_button)
        self.blink_state = False
        self.error_count = 0

        self.refresh_data()



        # Setup Folium Map in frame_a
        self.setup_map()

        # Database related UI elements
        self.comboBox = QComboBox(self.frame_b)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.currentIndexChanged.connect(self.LoadTableData)
        self.tableWidget = QTableWidget(self.frame_b)
        self.tableWidget.setObjectName(u"tableWidget")

        frame_b_layout = QVBoxLayout(self.frame_b)
        frame_b_layout.setObjectName(u"frame_b_layout")
        frame_b_layout.addWidget(self.comboBox)
        frame_b_layout.addWidget(self.tableWidget)

        # Connect Database
        self.DBConnection()

        QMetaObject.connectSlotsByName(MainWindow)
    
    def connect_to_server(self, server_ip):
        # Stop previous client thread if running
        if self.client_app.client_thread:
            self.client_app.client_thread.stop()
            self.client_app.client_thread.wait()  # Ensure the thread has completely stopped

        # Start new client thread with the given IP address
        self.client_app.start_client(server_ip)
        self.client_app.client_thread.message_received.connect(self.display_received_message)

    def display_received_message(self, message):
        format = QTextCharFormat()
        format.setForeground(QColor("green"))

        cursor = self.client_app.text_edit.textCursor()  # Access text_edit from ClientApp
        cursor.movePosition(QTextCursor.MoveOperation.End)
        cursor.setBlockFormat(self.client_app.get_left_aligned_format())
        cursor.insertText(f"Received: {message}\n", format)

        self.client_app.text_edit.setTextCursor(cursor)  # Update the ClientApp's text_edit



    def change_frame_color(self, color):
        self.frame_grey.setStyleSheet(f"background-color: {color};")


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.MENU.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"STREET LIGHT MONITORING", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"MESSAGES", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"NOTIFICATION", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"SETTINGS", None))

    @Slot()
    def change_page(self, index):
        self.mainbody.setCurrentIndex(index)

    def setup_map(self, table_name=None):
        # Define coordinates for different tables
        table_coords = {
            'sub1': [
                (21.749231662252758, 88.44446213277794),
                (22.742282547829127, 88.39574896234674),
                (23.75353989987697, 88.4704528658834),
                (24.74714697252383, 88.41567000328985),
                (25.717123202735824, 88.41691506834879),
                (26.747892414327502, 88.38196529923562),
                (22.561496123840236, 88.49018012343026),
                (22.5624472635428, 88.49043761548559),
                (22.574527669571054, 88.43298122919083),
            ],
            'sub2': [
                (26.797537835835055, 88.36718414815859),
                (26.76818630776784, 88.45107475277307),
                (26.817689705934118, 88.41841718594628),
                (26.791167954979247, 88.38909745044522),
                (26.76818630776784, 88.45107475277307),
                (26.745856909817277, 88.39168461621679)
            ]
        }

         # Connect to the database to fetch the status
        if table_name in table_coords:
            coordinates = table_coords[table_name]
            m = folium.Map(location=coordinates[0], zoom_start=8)

            cursor = self.db.cursor()
            cursor.execute(f"SELECT status FROM {table_name}")
            statuses = cursor.fetchall()
            cursor.close()

            # Add markers with appropriate colors
            for idx, coord in enumerate(coordinates):
                status = statuses[idx][0]
                color = 'red' if status == 'Inactive' else 'green'
            
                folium.Marker(
                location=coord,
                popup=f"Pole No: {idx + 1}",  # Popup message with index+1
                tooltip='Click for more info',
                icon=folium.Icon(color=color)
            ).add_to(m)

            # Save map data to a HTML file
            data = io.BytesIO()
            m.save(data, close_file=False)
            data.seek(0)

            # Create a QWebEngineView to display the map
            webView = QWebEngineView()
            webView.setHtml(data.getvalue().decode())

            # Get the existing layout, or create one if it does not exist
            layout = self.frame_a.layout()
            if layout is None:
                layout = QVBoxLayout()
                layout.setObjectName(u"frame_a_layout")
                self.frame_a.setLayout(layout)
            else:
                # Clear existing layout
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget:
                        widget.deleteLater()

            # Add the new widget to the layout
            layout.addWidget(webView)

    def DBConnection(self):
        try:
            # Attempt to connect to the database
            self.db = mdb.connect('localhost', 'root', '', 'sih')
            # Populate combobox with table names
            self.PopulateTableNames()
            # Display success message
            print('Connection', 'Database Connected Successfully') 

        except mdb.Error as e:
            # Display error message if connection fails
            print('Connection', 'Database Connected Successfully')
            # Exit the application with error code
            sys.exit(1)

    def PopulateTableNames(self):
        cursor = self.db.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        self.comboBox.clear()
        for table in tables:
            self.comboBox.addItem(table[0])
        cursor.close()

    def LoadTableData(self):
        table_name = self.comboBox.currentText()
        print(table_name)
        if table_name:
            cursor = self.db.cursor()
            cursor.execute(f"SELECT * FROM {table_name}")
            data = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            self.setup_map(table_name)

            self.tableWidget.setColumnCount(len(columns))
            self.tableWidget.setHorizontalHeaderLabels(columns)
            self.tableWidget.setRowCount(len(data))

            for row_num, row_data in enumerate(data):
                for col_num, cell_data in enumerate(row_data):
                    self.tableWidget.setItem(row_num, col_num, QTableWidgetItem(str(cell_data)))

            cursor.close()
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
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
