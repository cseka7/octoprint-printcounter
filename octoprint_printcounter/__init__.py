import json
import os
from octoprint.plugin import EventHandlerPlugin, StartupPlugin, TemplatePlugin, BlueprintPlugin
from flask import jsonify, make_response

class PrintCounterPlugin(EventHandlerPlugin, StartupPlugin, TemplatePlugin, BlueprintPlugin):
    def __init__(self):
        self.print_counts = {}

    def on_startup(self, host, port):
        self.load_counts()
        self.initialize_counts()

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

    def initialize_counts(self):
        files = self._file_manager.list_files(recursive=True)
        for location in files:
            for filename in files[location]:
                if filename.endswith(".gcode"):
                    file_path = self._file_manager.path_on_disk(location, filename)
                    if file_path not in self.print_counts:
                        self.print_counts[file_path] = 0
        self.save_counts()

    def reset_counts(self):
        self.print_counts = {}
        self.initialize_counts()
        self._logger.info("All print counts have been reset to 0.")

    @BlueprintPlugin.route("/get_count", methods=["GET"])
    def get_count(self):
    file_path = request.args.get('file_path')
    count = self.print_counts.get(file_path, 0)
    return make_response(jsonify({"count": count}), 200)

    def on_event(self, event, payload):
        if event in ["PrintDone", "PrintFailed"]:
            file_path = payload["file"]
            if file_path in self.print_counts:
                self.print_counts[file_path] += 1
            else:
                self.print_counts[file_path] = 1
            self._logger.info(f"Print count for {file_path}: {self.print_counts[file_path]}")
            self.save_counts()
        elif event == "FileAdded":
            file_path = payload["path"]
            if file_path.endswith(".gcode"):
                full_path = self._file_manager.path_on_disk(payload["origin"], file_path)
                if full_path not in self.print_counts:
                    self.print_counts[full_path] = 0
                    self._logger.info(f"Initialized print count for new file {full_path} to 0")
                    self.save_counts()

    @BlueprintPlugin.route("/reset_counts", methods=["POST"])
    def handle_reset_counts(self):
        self.reset_counts()
        return make_response(jsonify({"message": "All print counts have been reset to 0."}), 200)

    def get_template_configs(self):
        return [
            dict(type="settings", custom_bindings=False,  template= "printcounter.jinja2")
        ]

    def get_assets(self):
        return dict(
            js=["js/printcounter.js"]
        )

__plugin_name__ = "PrintCounter"
__plugin_version__ = "0.1.0"
__plugin_pythoncompat__ = ">=3.7,<4"
__plugin_description__ = "A plugin to count how many times a G-code file has been printed"

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = PrintCounterPlugin()
