import subprocess as sp
import tempfile as tmp

import toml


BUMP = "bumpline/cli.py"


class TestIncreaseMicro:
    "Release :: Increase Micro"
    tmp_file = tmp.NamedTemporaryFile()

    def test_with_major(self):
        """test with major version ::
        should return previous major, minor and micro + 1"""
        with open(self.tmp_file.name, "w") as file:
            file.write('[project]\nversion = "1"\n')

        result = sp.run([BUMP, self.tmp_file.name, "micro"])
        version = toml.load(self.tmp_file.name)["project"]["version"]

        assert version == "1.0.1"

    def test_with_minor(self):
        """test with minor version ::
        should return previous major, minor and micro + 1"""
        with open(self.tmp_file.name, "w") as file:
            file.write('[project]\nversion = "1.5"\n')

        result = sp.run([BUMP, self.tmp_file.name, "micro"])
        version = toml.load(self.tmp_file.name)["project"]["version"]

        assert version == "1.5.1"

    def test_with_micro(self):
        """test with micro version ::
        should return previous major, minor and micro + 1"""
        with open(self.tmp_file.name, "w") as file:
            file.write('[project]\nversion = "1.5.2"\n')

        result = sp.run([BUMP, self.tmp_file.name, "micro"])
        version = toml.load(self.tmp_file.name)["project"]["version"]

        assert version == "1.5.3"

    def test_with_major_add_alpha(self):
        with open(self.tmp_file.name, "w") as file:
            file.write('[project]\nversion = "1"\n')

        result = sp.run([BUMP, "--alpha", self.tmp_file.name, "micro"])
        version = toml.load(self.tmp_file.name)["project"]["version"]

        assert version == "1.0.1a"

    def test_with_major_add_beta(self):
        with open(self.tmp_file.name, "w") as file:
            file.write('[project]\nversion = "1"\n')

        result = sp.run([BUMP, "--beta", self.tmp_file.name, "micro"])
        version = toml.load(self.tmp_file.name)["project"]["version"]

        assert version == "1.0.1b"

    def test_with_major_add_rc(self):
        with open(self.tmp_file.name, "w") as file:
            file.write('[project]\nversion = "1"\n')

        result = sp.run([BUMP, "--rc", self.tmp_file.name, "micro"])
        version = toml.load(self.tmp_file.name)["project"]["version"]

        assert version == "1.0.1rc"

    def test_with_minor_add_alpha(self):
        with open(self.tmp_file.name, "w") as file:
            file.write('[project]\nversion = "1.4"\n')

        result = sp.run([BUMP, "--alpha", self.tmp_file.name, "micro"])
        version = toml.load(self.tmp_file.name)["project"]["version"]

        assert version == "1.4.1a"

    def test_with_minor_add_beta(self):
        with open(self.tmp_file.name, "w") as file:
            file.write('[project]\nversion = "1.4"\n')

        result = sp.run([BUMP, "--beta", self.tmp_file.name, "micro"])
        version = toml.load(self.tmp_file.name)["project"]["version"]

        assert version == "1.4.1b"

    def test_with_minor_add_rc(self):
        with open(self.tmp_file.name, "w") as file:
            file.write('[project]\nversion = "1.4"\n')

        result = sp.run([BUMP, "--rc", self.tmp_file.name, "micro"])
        version = toml.load(self.tmp_file.name)["project"]["version"]

        assert version == "1.4.1rc"

    def test_with_micro_add_alpha(self):
        with open(self.tmp_file.name, "w") as file:
            file.write('[project]\nversion = "1.4.9"\n')

        result = sp.run([BUMP, "--alpha", self.tmp_file.name, "micro"])
        version = toml.load(self.tmp_file.name)["project"]["version"]

        assert version == "1.4.10a"

    def test_with_micro_add_beta(self):
        with open(self.tmp_file.name, "w") as file:
            file.write('[project]\nversion = "1.4.9"\n')

        result = sp.run([BUMP, "--beta", self.tmp_file.name, "micro"])
        version = toml.load(self.tmp_file.name)["project"]["version"]

        assert version == "1.4.10b"

    def test_with_micro_add_rc(self):
        with open(self.tmp_file.name, "w") as file:
            file.write('[project]\nversion = "1.4.9"\n')

        result = sp.run([BUMP, "--rc", self.tmp_file.name, "micro"])
        version = toml.load(self.tmp_file.name)["project"]["version"]

        assert version == "1.4.10rc"
