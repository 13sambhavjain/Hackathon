import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QRadioButton, QPushButton,
    QVBoxLayout, QHBoxLayout, QMessageBox
)
from PyQt5.QtGui import QFont, QPixmap, QPalette, QBrush
from PyQt5.QtCore import Qt

class SimulationSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simulation Selector")
        self.image_path = "car_background.jpeg"  # <-- Ensure image file is in the same folder
        self.init_window_size()
        self.set_background_image()
        self.init_ui()

    def init_window_size(self):
        screen = QApplication.primaryScreen().availableGeometry()
        w = screen.width() // 2
        h = screen.height() // 2
        self.setGeometry(50, 50, w, h)

    def set_background_image(self):
        if os.path.exists(self.image_path):
            self.setAutoFillBackground(True)
            palette = QPalette()
            pixmap = QPixmap(self.image_path)
            if not pixmap.isNull():
                scaled = pixmap.scaled(
                    self.width(), self.height(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation
                )
                palette.setBrush(QPalette.Window, QBrush(scaled))
                self.setPalette(palette)
        else:
            print(f"Image not found: {self.image_path}")

    def resizeEvent(self, event):
        self.set_background_image()

    def init_ui(self):
        title = QLabel("Choose Simulation Mode")
        title.setFont(QFont("Arial", 24, QFont.Bold))  # 1.5× original size
        title.setStyleSheet("color: black; background: transparent;")

        self.auto_radio = QRadioButton("Automatic")
        self.manual_radio = QRadioButton("Manual")
        self.auto_radio.setChecked(True)

        radio_style = """
            QRadioButton {
                color: black;
                font-size: 21px;
                font-weight: bold;
                background: transparent;
                spacing: 20px;
            }
            QRadioButton::indicator {
                width: 24px;
                height: 24px;
            }
            QRadioButton::indicator:checked {
                background-color: red;
                border: 3px solid darkred;
                border-radius: 12px;
            }
            QRadioButton::indicator:unchecked {
                border: 3px solid red;
                border-radius: 12px;
            }
        """
        self.auto_radio.setStyleSheet(radio_style)
        self.manual_radio.setStyleSheet(radio_style)

        radio_layout = QHBoxLayout()
        radio_layout.addWidget(self.auto_radio)
        radio_layout.addSpacing(30)
        radio_layout.addWidget(self.manual_radio)

        self.submit_btn = QPushButton("Run Simulation")
        self.submit_btn.clicked.connect(self.on_submit)
        self.submit_btn.setStyleSheet("""
            QPushButton {
                background-color: red;
                color: white;
                border: none;
                border-radius: 12px;
                padding: 14px 32px;
                font-size: 21px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: darkred;
            }
        """)

        layout = QVBoxLayout()
        layout.addSpacing(20)
        layout.addWidget(title)
        layout.addSpacing(20)
        layout.addLayout(radio_layout)
        layout.addSpacing(20)
        layout.addWidget(self.submit_btn)
        layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        layout.setSpacing(25)
        layout.setContentsMargins(80, 40, 40, 40)  # ⬅ left margin increased

        self.setLayout(layout)

    def on_submit(self):
        mode = "Automatic" if self.auto_radio.isChecked() else "Manual"
        QMessageBox.information(self, "Simulation Started", f"Running {mode} simulation...")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimulationSelector()
    window.show()
    sys.exit(app.exec_())
