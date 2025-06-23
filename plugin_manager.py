import importlib
import os
from typing import List, Type
from interfaces import TextAnalyzer


class PluginManager:
    def __init__(self, plugin_folder: str = "analyzers"):
        self.plugin_folder = plugin_folder
        self.plugins: List[TextAnalyzer] = []

    def load_plugins(self):
        for filename in os.listdir(self.plugin_folder):
            if filename.endswith(".py"):
                module_name = filename[:-3]
                try:
                    module = importlib.import_module(f"{self.plugin_folder}.{module_name}")
                    for attr in dir(module):
                        obj = getattr(module, attr)
                        if isinstance(obj, type):
                            plugin = obj()
                            required = ["name", "version", "description", "analyze", "analyze_async"]
                            if all(hasattr(plugin, method) for method in required):
                                self.plugins.append(plugin)
                except Exception as e:
                    print(f"Error loading {filename}: {e}")

    def get_plugins(self) -> List[TextAnalyzer]:
        return self.plugins
