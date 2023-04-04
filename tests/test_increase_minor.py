import subprocess as sp
import tempfile as tmp

import toml


BUMP = "bumpline/cli.py"


class TestIncreaseMinor:
    tmp_file = tmp.NamedTemporaryFile()

    def test_with_major(self):
        with open(self.tmp_file.name, "w") as file:
            file.write('[project]\nversion = "1"\n')

        result = sp.run([BUMP, self.tmp_file.name, "minor"])
        version = toml.load(self.tmp_file.name)["project"]["version"]

        assert version == "1.1"

    def test_with_minor(self):
        with open(self.tmp_file.name, "w") as file:
            file.write('[project]\nversion = "1.5"\n')

        result = sp.run([BUMP, self.tmp_file.name, "minor"])
        version = toml.load(self.tmp_file.name)["project"]["version"]

        assert version == "1.6"

    def test_with_micro(self):
        with open(self.tmp_file.name, "w") as file:
            file.write('[project]\nversion = "1.5.2"\n')

        result = sp.run([BUMP, self.tmp_file.name, "minor"])
        version = toml.load(self.tmp_file.name)["project"]["version"]

        assert version == "1.6.0"

    def test_with_major_add_alpha(self):
        with open(self.tmp_file.name, "w") as file:
            file.write('[project]\nversion = "1"\n')

        result = sp.run([BUMP, "--alpha", self.tmp_file.name, "minor"])
        version = toml.load(self.tmp_file.name)["project"]["version"]

        assert version == "1.1a"

    def test_with_major_add_beta(self):
        with open(self.tmp_file.name, "w") as file:
            file.write('[project]\nversion = "1"\n')

        result = sp.run([BUMP, "--beta", self.tmp_file.name, "minor"])
        version = toml.load(self.tmp_file.name)["project"]["version"]

        assert version == "1.1b"

    def test_with_major_add_rc(self):
        with open(self.tmp_file.name, "w") as file:
            file.write('[project]\nversion = "1"\n')

        result = sp.run([BUMP, "--rc", self.tmp_file.name, "minor"])
        version = toml.load(self.tmp_file.name)["project"]["version"]

        assert version == "1.1rc"

    def test_with_minor_add_alpha(self):
        with open(self.tmp_file.name, "w") as file:
            file.write('[project]\nversion = "1.4"\n')

        result = sp.run([BUMP, "--alpha", self.tmp_file.name, "minor"])
        version = toml.load(self.tmp_file.name)["project"]["version"]

        assert version == "1.5a"

    def test_with_minor_add_beta(self):
        with open(self.tmp_file.name, "w") as file:
            file.write('[project]\nversion = "1.4"\n')

        result = sp.run([BUMP, "--beta", self.tmp_file.name, "minor"])
        version = toml.load(self.tmp_file.name)["project"]["version"]

        assert version == "1.5b"

    def test_with_minor_add_rc(self):
        with open(self.tmp_file.name, "w") as file:
            file.write('[project]\nversion = "1.4"\n')

        result = sp.run([BUMP, "--rc", self.tmp_file.name, "minor"])
        version = toml.load(self.tmp_file.name)["project"]["version"]

        assert version == "1.5rc"

    def test_with_micro_add_alpha(self):
        with open(self.tmp_file.name, "w") as file:
            file.write('[project]\nversion = "1.4.9"\n')

        result = sp.run([BUMP, "--alpha", self.tmp_file.name, "minor"])
        version = toml.load(self.tmp_file.name)["project"]["version"]

        assert version == "1.5.0a"

    def test_with_micro_add_beta(self):
        with open(self.tmp_file.name, "w") as file:
            file.write('[project]\nversion = "1.4.9"\n')

        result = sp.run([BUMP, "--beta", self.tmp_file.name, "minor"])
        version = toml.load(self.tmp_file.name)["project"]["version"]

        assert version == "1.5.0b"

    def test_with_micro_add_rc(self):
        with open(self.tmp_file.name, "w") as file:
            file.write('[project]\nversion = "1.4.9"\n')

        result = sp.run([BUMP, "--rc", self.tmp_file.name, "minor"])
        version = toml.load(self.tmp_file.name)["project"]["version"]

        assert version == "1.5.0rc"
