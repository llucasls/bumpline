#!/usr/bin/env python3
import os
import sys
import platform
import subprocess as sp
import pty
import argparse


def get_python_version(tty=False):
    implementation = platform.python_implementation()
    version = platform.python_version()

    if tty:
        blue = "\x1b[34m"
        yellow = "\x1b[33m"
        reset = "\x1b[00m"
        return f"{blue}{implementation} version: {yellow}{version}{reset}"
    else:
        return " ".join([implementation, "version:", version])


def write_test_to_tty():
    exit_code = 0
    # Run the command in a pty
    pid, fd = pty.fork()
    if pid == 0:
        # Child process
        status = sp.call(["make", "test"])
        os._exit(status)
    else:
        # Parent process
        try:
            while True:
                data = os.read(fd, 1024)
                if not data:
                    break
                sys.stdout.write(data.decode('utf-8'))
            _, status = os.waitpid(pid, 0)
            exit_code = os.WEXITSTATUS(status)
        except OSError:
            pass

    print(get_python_version(True))
    return exit_code


def write_test_to_file():
    with sp.Popen(["make", "test", "PYTEST_FLAGS=-v --mocha --color=no"],
                  stdout=sp.PIPE) as process:
        stdout, stderr = process.communicate()
        output = (stdout.decode("utf-8")
                  .replace("\x1b[31m", "")
                  .replace("\x1b[32m", "")
                  .replace("\x1b[0m", "")
                  .strip())
        print(output)

        return process.returncode


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--redirect-stdout", action="store_true")

    should_redirect = parser.parse_args().redirect_stdout

    if should_redirect:
        status = write_test_to_file()
    else:
        status = write_test_to_tty()

    return status


if __name__ == "__main__":
    sys.exit(main())
