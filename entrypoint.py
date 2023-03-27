#!/usr/bin/env python3
import sys
import platform
import subprocess as sp


command = sp.run(["make", "test"])
print("python version: \x1b[32m", platform.python_version(), "\x1b[0m")


sys.exit(command.returncode)
