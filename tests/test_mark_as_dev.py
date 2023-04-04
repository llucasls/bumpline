import subprocess as sp
import tempfile as tmp

import toml


BUMP = "bumpline/cli.py"


class TestMarkAsDev:
    tmp_file = tmp.NamedTemporaryFile()

    def test_add_dev(self):
        with open(self.tmp_file.name, "w") as file:
            file.write('[project]\nversion = "1.5.2"\n')

        result = sp.run([BUMP, self.tmp_file.name, "-d"])
        version = toml.load(self.tmp_file.name)["project"]["version"]

        assert version == "1.5.2.dev"

    def test_increase_dev(self):
        with open(self.tmp_file.name, "w") as file:
            file.write('[project]\nversion = "1.5.2.dev"\n')

        result = sp.run([BUMP, self.tmp_file.name, "-d"])
        version = toml.load(self.tmp_file.name)["project"]["version"]

        assert version == "1.5.2.dev1"

    def test_remove_dev(self):
        with open(self.tmp_file.name, "w") as file:
            file.write('[project]\nversion = "1.5.2.dev"\n')

        result = sp.run([BUMP, self.tmp_file.name, "-D"])
        version = toml.load(self.tmp_file.name)["project"]["version"]

        assert version == "1.5.2"
