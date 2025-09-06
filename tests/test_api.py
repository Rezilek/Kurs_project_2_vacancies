import pytest

from src.api.hh_api import HeadHunterAPI


@pytest.fixture
def hh_api():
    return HeadHunterAPI()


def test_hh_api_connection(hh_api):
    """Тест подключения к API"""
    # Проверка, что объект создается без ошибок
    assert hh_api is not None


def test_get_vacancies(hh_api):
    """Тест получения вакансий"""
    vacancies = hh_api.get_vacancies("Python")
    assert isinstance(vacancies, list)
    if vacancies:  # если API вернуло результаты
        assert all(isinstance(v, dict) for v in vacancies)
