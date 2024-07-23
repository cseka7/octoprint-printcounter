import json
import os
from octoprint.plugin import EventHandlerPlugin, StartupPlugin

class PrintCounterPlugin(EventHandlerPlugin, StartupPlugin):
    def __init__(self):
        self.print_counts = {}

    def on_startup(self, host, port):
        self.load_counts()

    def get_data_folder(self):
        return self.get_plugin_data_folder()

    def load_counts(self):
        data_folder = self.get_data_folder()
        file_path = os.path.join(data_folder, "print_counts.json")
        try:
            with open(file_path, "r") as f:
                self.print_counts = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.print_counts = {}

    def save_counts(self):
        data_folder = self.get_data_folder()
        os.makedirs(data_folder, exist_ok=True)
        file_path = os.path.join(data_folder, "print_counts.json")
        with open(file_path, "w") as f:
            json.dump(self.print_counts, f)

    def on_event(self, event, payload):
        if event in ["PrintDone", "PrintFailed"]:
            file_path = payload["file"]
            if file_path in self.print_counts:
                self.print_counts[file_path] += 1
            else:
                self.print_counts[file_path] = 1
            self._logger.info(f"Print count for {file_path}: {self.print_counts[file_path]}")
            self.save_counts()

__plugin_name__ = "PrintCounter"
__plugin_version__ = "0.1.0"
__plugin_description__ = "A plugin to count how many times a G-code file has been printed"

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = PrintCounterPlugin()
