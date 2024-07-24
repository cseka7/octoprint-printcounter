# setup.py
from setuptools import setup

try:
	import octoprint_setuptools
except ImportError:
	print("Could not import OctoPrint's setuptools, are you sure you are running that under "
	      "the same python installation that OctoPrint is installed under?")
	import sys
	sys.exit(-1)


plugin_identifier = "printcounter"
plugin_package = "octoprint_printcounter"
plugin_name = "OctoPrint-PrintCounter"
plugin_version = "0.1.0"
plugin_description = "A plugin to count how many times a G-code file has been printed"
plugin_author = "Adam Csoka"
plugin_author_email = "cseka7@gmail.com"
plugin_url = "https://github.com/yourusername/octoprint-printcounter"
plugin_license = "AGPLv3"
plugin_requires = []


setup_parameters = octoprint_setuptools.create_plugin_setup_parameters(
	identifier=plugin_identifier,
	package=plugin_package,
	name=plugin_name,
	version=plugin_version,
	description=plugin_description,
	author=plugin_author,
	mail=plugin_author_email,
	url=plugin_url,
	license=plugin_license,
	requires=plugin_requires,
)

setup(**setup_parameters)

#setup(
    #name=plugin_name,
    #version=plugin_version,
    #description=plugin_description,
    #author=plugin_author,
    #author_email=plugin_author_email,
    #url=plugin_url,
    #license=plugin_license,
    #packages=[plugin_package],
    #install_requires=plugin_requires,
    #include_package_data=True,
    #zip_safe=False,
    #entry_points={
        #"octoprint.plugin": [
            #"printcounter = octoprint_printcounter"
        #]
    #},
    #package_data={
        #"": ["static/js/printcounter.js", "templates/printcounter.jinja2"]
    #}
)
