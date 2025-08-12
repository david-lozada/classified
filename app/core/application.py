# app/core/application.py
class MainApplication(QMainWindow):
    def __init__(self):
        self.modules = {}
        self._load_modules()
    
    def _load_modules(self):
        # Option 1: Hardcoded module list
        module_names = ["dashboard", "settings"]
        
        # Option 2: Discover modules dynamically
        # module_names = discover_modules()
        
        for name in module_names:
            try:
                module = importlib.import_module(f"app.modules.{name}")
                if hasattr(module, "create"):
                    self.modules[name] = module.create(self)
                    self.modules[name].initialize()
            except ImportError as e:
                print(f"Failed to load module {name}: {e}")