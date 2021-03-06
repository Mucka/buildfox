# BuildFox ninja generator

import os
import platform
from lib_util import which

def discover():
	vars = {
		"variation": "debug"
	}

	if which("cl") and which("link") and which("lib"):
		vars["toolset_msc"] = "true"
		if os.environ.get("VS140COMNTOOLS"):
			vars["toolset_msc_ver"] = "2015"
		elif os.environ.get("VS130COMNTOOLS"):
			vars["toolset_msc_ver"] = "2013"
		elif os.environ.get("VS120COMNTOOLS"):
			vars["toolset_msc_ver"] = "2012"

	if which("clang"):
		vars["toolset_clang"] = "true"

	if which("gcc") and which("g++"):
		vars["toolset_gcc"] = "true"

	if vars.get("toolset_msc"):
		vars["toolset"] = "msc"
	elif vars.get("toolset_clang"):
		vars["toolset"] = "clang"
	elif vars.get("toolset_gcc"):
		vars["toolset"] = "gcc"
	else:
		raise ValueError("Can't find any compiler, expected cl, clang, gcc executables")

	if not which("ninja"):
		print("Warning ! Can't find ninja executable")

	vars["system"] = platform.system()
	vars["machine"] = platform.machine()
	cwd = os.getcwd().replace("\\", "/")
	if cwd and cwd != "." and not cwd.endswith("/"):
		cwd += "/"
	vars["cwd"] = cwd

	return vars
