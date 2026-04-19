from PyQt5.QtWidgets import QMainWindow, QTextEdit, QLabel, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DangerWrite Pro ⚠️")
        self.setGeometry(200, 200, 900, 600)

        self.label = QLabel("Keep typing or everything will disappear in 5 seconds!")

        self.editor = QTextEdit()
        self.editor.setPlaceholderText("Start writing...")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.editor)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)