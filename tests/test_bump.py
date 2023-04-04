import subprocess as sp
import tempfile as tmp

import toml


BUMP = "bumpline/cli.py"


def test_error_when_no_arguments_are_given():
    result = sp.run([BUMP], stdout=sp.PIPE, stderr=sp.PIPE)

    assert result.returncode == 2


def test_dont_change_version_when_release_isnt_given():
    with tmp.NamedTemporaryFile() as tmp_file:
        with open(tmp_file.name, "w") as file:
            file.write('[project]\nversion = "1.5"\n')

        result = sp.run([BUMP, tmp_file.name])
        version = toml.load(tmp_file.name)["project"]["version"]

        assert version == "1.5"
