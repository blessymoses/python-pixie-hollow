import pytest


def test_first_test() -> None:
    assert 1 == 1


# to skip a test
@pytest.mark.skip
def test_should_be_skipped() -> None:
    assert 1 == 2


# conditional skip
@pytest.mark.skipif(1 > 1, reason="Skipped because 4>1")
def test_should_be_skipped_if() -> None:
    assert 1 == 2