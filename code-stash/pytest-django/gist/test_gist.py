"""
 Run pytests
 pytest test_gist.py -v -p no:warnings -s
"""
import pytest


def test_first_test() -> None:
    assert 1 == 1


# to skip a test
@pytest.mark.skip
def test_should_be_skipped() -> None:
    assert 1 == 2


# conditional skip
@pytest.mark.skipif(4 > 1, reason="Skipped because 4>1")
def test_should_be_skipped_if() -> None:
    assert 1 == 2


# for flaky test, to not fail the tests if this fails
@pytest.mark.xfail
def test_dont_care_if_fails() -> None:
    assert 1 == 1


# to mark a slow running test
@pytest.mark.slow
def test_with_custom_marker() -> None:
    pass


class Company:
    def __init__(self, name: str, stock_symbol: str) -> None:
        self.name = name
        self.stock_symbol = stock_symbol

    def __str__(self) -> str:
        return f"{self.name}:{self.stock_symbol}"


@pytest.fixture
def company() -> Company:
    return Company(name="Rolls-Royce", stock_symbol="RR")


def test_with_fixture(company: Company) -> None:
    print(f"Printing {company} from fixture")


@pytest.mark.parametrize("company_name", ["TikTok", "Instagram", "Twitch"])
def test_parametrized(company_name: str) -> None:
    print(f"\nTest with {company_name}")


@pytest.mark.parametrize(
    "company_name",
    ["TikTok", "Instagram", "Twitch"],
    ids=["TIKTOK TEST", "INSTAGRAM TEST", "TWITCH TEST"],
)
def test_parametrized_with_id(company_name: str) -> None:
    print(f"\nTest with {company_name}")


def raise_custom_exception() -> None:
    raise ValueError("My custom Exception")


def test_raise_custom_exception_pass() -> None:
    with pytest.raises(ValueError) as e:
        raise_custom_exception()
    assert "My custom Exception" == str(e.value)