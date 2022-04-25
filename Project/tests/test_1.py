from package_1.main import second, some


def test_some():
    assert some("abv") is None


def test_second():
    """test_second tests the second function"""
    assert second() is None
