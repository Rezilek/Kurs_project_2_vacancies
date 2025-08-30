import pytest

from src.models.vacancy import Vacancy


@pytest.fixture
def sample_vacancy():
    return Vacancy(
        title="Python Developer",
        url="https://hh.ru/vacancy/123",
        salary={"from": 100000, "to": 150000, "currency": "RUR"},
        description="Требуется Python разработчик",
    )


@pytest.fixture
def sample_vacancy_no_salary():
    return Vacancy(
        title="Python Developer",
        url="https://hh.ru/vacancy/123",
        salary=None,
        description="Требуется Python разработчик",
    )


def test_vacancy_creation(sample_vacancy):
    """Тест создания вакансии"""
    assert sample_vacancy.title == "Python Developer"
    assert sample_vacancy.url == "https://hh.ru/vacancy/123"
    assert sample_vacancy.salary_from == 100000
    assert sample_vacancy.salary_to == 150000
    assert sample_vacancy.currency == "RUR"
    assert sample_vacancy.description == "Требуется Python разработчик"


def test_vacancy_no_salary(sample_vacancy_no_salary):
    """Тест вакансии без зарплаты"""
    assert sample_vacancy_no_salary.salary_from is None
    assert sample_vacancy_no_salary.salary_to is None
    assert sample_vacancy_no_salary.currency is None


def test_vacancy_comparison(sample_vacancy):
    """Тест сравнения вакансий"""
    higher_vacancy = Vacancy(
        title="Senior Python Developer",
        url="https://hh.ru/vacancy/124",
        salary={"from": 200000, "to": 250000, "currency": "RUR"},
        description="Требуется Senior Python разработчик",
    )

    lower_vacancy = Vacancy(
        title="Junior Python Developer",
        url="https://hh.ru/vacancy/125",
        salary={"from": 50000, "to": 80000, "currency": "RUR"},
        description="Требуется Junior Python разработчик",
    )

    assert higher_vacancy > sample_vacancy
    assert lower_vacancy < sample_vacancy
    assert sample_vacancy == sample_vacancy


def test_cast_to_object_list():
    """Тест преобразования списка словарей в список объектов"""
    vacancies_data = [
        {
            "name": "Python Developer",
            "alternate_url": "https://hh.ru/vacancy/123",
            "salary": {"from": 100000, "to": 150000, "currency": "RUR"},
            "snippet": {"requirement": "Требуется Python разработчик"},
        }
    ]

    vacancies = Vacancy.cast_to_object_list(vacancies_data)
    assert len(vacancies) == 1
    assert isinstance(vacancies[0], Vacancy)
    assert vacancies[0].title == "Python Developer"
