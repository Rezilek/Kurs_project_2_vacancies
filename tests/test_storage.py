import os

import pytest

from src.models.vacancy import Vacancy
from src.storage.json_storage import JSONStorage


@pytest.fixture
def storage(tmp_path):
    """Фикстура для тестирования хранилища с временным файлом"""
    test_file = tmp_path / "test_vacancies.json"
    storage = JSONStorage(filename=str(test_file))
    yield storage
    if os.path.exists(test_file):
        os.remove(test_file)


@pytest.fixture
def sample_vacancy():
    return Vacancy(
        title="Python Developer",
        url="https://hh.ru/vacancy/123",
        salary={"from": 100000, "to": 150000, "currency": "RUR"},
        description="Требуется Python разработчик",
    )


def test_storage_init(storage):
    """Тест инициализации хранилища"""
    assert os.path.exists(storage._JSONStorage__filename)


def test_add_vacancy(storage, sample_vacancy):
    """Тест добавления вакансии"""
    storage.add_vacancy(sample_vacancy)
    vacancies = storage.get_vacancies()
    assert len(vacancies) == 1
    assert vacancies[0].title == sample_vacancy.title


def test_duplicate_vacancy(storage, sample_vacancy):
    """Тест добавления дубликата вакансии"""
    storage.add_vacancy(sample_vacancy)
    storage.add_vacancy(sample_vacancy)
    vacancies = storage.get_vacancies()
    assert len(vacancies) == 1


def test_get_vacancies(storage, sample_vacancy):
    """Тест получения вакансий"""
    storage.add_vacancy(sample_vacancy)
    vacancies = storage.get_vacancies()
    assert len(vacancies) == 1
    assert isinstance(vacancies[0], Vacancy)


def test_delete_vacancy(storage, sample_vacancy):
    """Тест удаления вакансии"""
    storage.add_vacancy(sample_vacancy)
    vacancies = storage.get_vacancies()
    assert len(vacancies) == 1

    storage.delete_vacancy(sample_vacancy)
    vacancies = storage.get_vacancies()
    assert len(vacancies) == 0


def test_filter_vacancies(storage, sample_vacancy):
    """Тест фильтрации вакансий"""
    storage.add_vacancy(sample_vacancy)

    # Фильтр по ключевому слову
    filtered = storage.get_vacancies({"keyword": "Python"})
    assert len(filtered) == 1

    # Фильтр по несуществующему ключевому слову
    filtered = storage.get_vacancies({"keyword": "Java"})
    assert len(filtered) == 0

    # Фильтр по зарплате
    filtered = storage.get_vacancies({"salary_from": 90000})
    assert len(filtered) == 1

    filtered = storage.get_vacancies({"salary_from": 110000})
    assert len(filtered) == 0
