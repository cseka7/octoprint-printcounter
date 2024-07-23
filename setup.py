# setup.py
plugin_requires = []

plugin_additional_data = []

plugin_additional_packages = []

plugin_ignored_packages = []

plugin_requires = ["octoprint>=1.4.0"]

from setuptools import setup

setup(
    name="octoprint-printcounter",
    version="0.1.0",
    description="A plugin to count how many times a G-code file has been printed",
    author="Adam Csoka",
    author_email="cseka7@gmail.com",
    url="https://github.com/cseka7/octoprint-printcounter",
    license="AGPLv3",
    packages=["octoprint_printcounter"],
    install_requires=plugin_requires,
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "octoprint.plugin": [
            "printcounter = octoprint_printcounter"
        ]
    },
    package_data={
        "": ["static/js/printcounter.js"]
    }
)
