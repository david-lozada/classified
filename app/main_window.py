# app/main_window.py
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QStatusBar
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Classified")
        self._setup_ui()
        
    def _setup_ui(self):
        """Initialize all main view components"""
        # Central widget with main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout(central_widget)
        
        # Add status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")
        
        # Window properties
        self.setMinimumSize(800, 600)
        
    def _setup_modules(self):
        """Initialize and arrange modules"""
        # Create container for modules
        modules_container = QWidget()
        modules_layout = QHBoxLayout(modules_container)
        
        # Add modules to layout
        if hasattr(self.application, 'modules'):
            for name, module in self.application.modules.items():
                modules_layout.addWidget(module)
        
        self.main_layout.addWidget(modules_container, stretch=1)