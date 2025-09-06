import requests

from src.api.abstract_api import AbstractAPI


class HeadHunterAPI(AbstractAPI):
    """Класс для работы с API HeadHunter"""

    def __init__(self):
        self.__base_url = "https://api.hh.ru/vacancies"
        self._connect_to_api()

    def _connect_to_api(self) -> None:
        """Подключение к API HeadHunter"""
        try:
            response = requests.get(self.__base_url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка подключения к API: {e}")
            raise

    def get_vacancies(self, search_query: str,
                      per_page: int = 100) -> list[dict]:
        """
        Получение вакансий по поисковому запросу

        :param search_query: Поисковый запрос
        :param per_page: Количество вакансий на странице
        :return: Список вакансий
        """
        params = {
            "text": search_query,
            "per_page": per_page,
            "area": 113,  # Россия
            "only_with_salary": True,
        }

        try:
            response = requests.get(self.__base_url, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get("items", [])
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при получении вакансий: {e}")
            return []
        except (ValueError, KeyError) as e:
            print(f"Ошибка при обработке ответа: {e}")
            return []
