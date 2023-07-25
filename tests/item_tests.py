import pytest

from src.Vacancy import Vacancy


@pytest.fixture
def vacancy():
    vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Moscow",
                      "Требования: опыт работы от 3 лет...")
    return vacancy


def test_init(vacancy):
    assert vacancy.title == "Python Developer"
    assert vacancy.link == "<https://hh.ru/vacancy/123456>"
    assert vacancy.salary == "100 000-150 000 руб."
    assert vacancy.area == "Moscow"
    assert vacancy.description == "Требования: опыт работы от 3 лет..."


def test_attribute_error_title(vacancy):
    with pytest.raises(AttributeError):
        vacancy.title = "Python"


def test_attribute_error_link(vacancy):
    with pytest.raises(AttributeError):
        vacancy.link = "<https://hh.ru/"


def test_attribute_error_salary(vacancy):
    with pytest.raises(AttributeError):
        vacancy.salary = "10 руб."


def test_attribute_error_area(vacancy):
    with pytest.raises(AttributeError):
        vacancy.area = "New-York"


def test_attribute_error_description(vacancy):
    with pytest.raises(AttributeError):
        vacancy.description = "Требования:"


def test_eq_gt_lt(vacancy):
    vacancy2 = Vacancy("Python", "https://hh.ru/", "50 000-100 000 руб.", "Moscow", "Требования:")
    assert (vacancy > vacancy2) is True