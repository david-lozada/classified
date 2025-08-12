import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QApplication
from app.main_window import MainWindow

def main():
    # Modern high DPI handling (Qt6)
    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )
    
    app = QApplication(sys.argv)
    primary_screen = app.primaryScreen()
    screen_geometry = primary_screen.availableGeometry()

    window = MainWindow()
    window.setGeometry(screen_geometry)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()