from setuptools import setup

plugin_identifier = "printcounter"
plugin_package = "octoprint_printcounter"
plugin_name = "OctoPrint-PrintCounter"
plugin_version = "0.1.0"
plugin_description = "A plugin to count how many times a G-code file has been printed"
plugin_author = "Your Name"
plugin_author_email = "you@example.com"
plugin_url = "https://github.com/yourusername/octoprint-printcounter"
plugin_license = "AGPLv3"

plugin_requires = []

setup(
    name=plugin_name,
    version=plugin_version,
    description=plugin_description,
    author=plugin_author,
    author_email=plugin_author_email,
    url=plugin_url,
    license=plugin_license,
    packages=[plugin_package],
    install_requires=plugin_requires,
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "octoprint.plugin": [
            f"{plugin_identifier} = {plugin_package}"
        ]
    },
    package_data={
        plugin_package: ["static/js/printcounter.js", "templates/printcounter.jinja2"]
    }
)
