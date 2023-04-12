from bumpline.separate_version import split_version_string


def test_split_version_release1():
    version = "5"
    assert split_version_string(version) == ("", "5", "", "", "")

def test_split_version_release2():
    version = "5.4"
    assert split_version_string(version) == ("", "5.4", "", "", "")

def test_split_version_release3():
    version = "5.4.3"
    assert split_version_string(version) == ("", "5.4.3", "", "", "")

def test_split_version_release4():
    version = "5.4.3rc2"
    assert split_version_string(version) == ("", "5.4.3", "rc2", "", "")

def test_split_version_release5():
    version = "5.4a"
    assert split_version_string(version) == ("", "5.4", "a", "", "")

def test_split_version_release6():
    version = "1!5.4.3"
    assert split_version_string(version) == ("1", "5.4.3", "", "", "")

def test_split_version_release7():
    version = "1!6.0b"
    assert split_version_string(version) == ("1", "6.0", "b", "", "")

def test_split_version_release8():
    version = "5.4.3.post"
    assert split_version_string(version) == ("", "5.4.3", "", ".post", "")

def test_split_version_release9():
    version = "5.4.3.dev"
    assert split_version_string(version) == ("", "5.4.3", "", "", ".dev")

def test_split_version_release10():
    version = "1!2.3.4rc5.post6.dev7"
    assert split_version_string(version) == ("1", "2.3.4", "rc5", ".post6", ".dev7")
