from feba66_apps.hello import core


def test_sample():
    assert core is not None


def test_hello_world():
    assert core.hello_world() == "Hello, World!"
