# app/modules/login.py
from PySide6.QtWidgets import (QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from PySide6.QtCore import Signal, Qt
import importlib
from pathlib import Path

class LoginDialog(QDialog):
    login_success = Signal(dict)  # Emits user data on success
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Login")
        self.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint)
        self.setFixedSize(350, 220)
        self.user_data = None
        self.available_roles = self._discover_roles()
        
        self._setup_ui()
    
    def _discover_roles(self):
        """Discover available user roles from modules"""
        roles = set()
        modules_path = Path(__file__).parent.parent / "modules"
        
        for module_file in modules_path.glob("*.py"):
            if module_file.name.startswith("_"):
                continue
                
            module_name = module_file.stem
            try:
                module = importlib.import_module(f"app.modules.{module_name}")
                if hasattr(module, "REQUIRED_ROLE"):
                    roles.add(module.REQUIRED_ROLE)
            except ImportError:
                continue
                
        return sorted(roles)
    
    def _setup_ui(self):
        layout = QVBoxLayout()
        
        # Username
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        
        # Password
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        
        # Role selection (dynamic based on modules)
        self.role_label = QLabel("Role:")
        self.role_combo = QComboBox()
        self.role_combo.addItems(self.available_roles)
        
        # Login button
        self.login_btn = QPushButton("Login")
        self.login_btn.clicked.connect(self._authenticate)
        
        layout.addWidget(QLabel("Username:"))
        layout.addWidget(self.username_input)
        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.password_input)
        layout.addWidget(self.role_label)
        layout.addWidget(self.role_combo)
        layout.addWidget(self.login_btn)
        
        self.setLayout(layout)
    
    def _authenticate(self):
        username = self.username_input.text()
        password = self.password_input.text()
        role = self.role_combo.currentText()
        
        # Replace with real authentication
        if username and password:  # Simple validation
            self.user_data = {
                "username": username,
                "role": role,
                "permissions": self._get_permissions_for_role(role)
            }
            self.login_success.emit(self.user_data)
            self.accept()
        else:
            QMessageBox.warning(self, "Error", "Invalid credentials")
    
    def _get_permissions_for_role(self, role):
        """Get module permissions for the selected role"""
        permissions = {}
        modules_path = Path(__file__).parent.parent / "modules"
        
        for module_file in modules_path.glob("*.py"):
            if module_file.name.startswith("_"):
                continue
                
            module_name = module_file.stem
            try:
                module = importlib.import_module(f"app.modules.{module_name}")
                if hasattr(module, "REQUIRED_ROLE"):
                    permissions[module_name] = (module.REQUIRED_ROLE == role)
            except ImportError:
                continue
                
        return permissions