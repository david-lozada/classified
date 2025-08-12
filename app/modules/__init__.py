# app/modules/__init__.py
class ModuleLoader:
    def __init__(self, parent):
        self.parent = parent
        self._load_core_modules()
        
    def _load_core_modules(self):
        from .dashboard import Dashboard
        from .settings import Settings
        
        self.dashboard = Dashboard(self.parent)
        self.settings = Settings(self.parent)