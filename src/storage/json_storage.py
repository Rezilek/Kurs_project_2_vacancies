import json
import os
from typing import Any, Dict, List, Optional

from src.models.vacancy import Vacancy
from src.storage.abstract_storage import AbstractStorage


class JSONStorage(AbstractStorage):
    """Класс для работы с JSON-файлом как хранилищем вакансий"""

    def __init__(self, filename: str = "vacancies.json"):
        self.__filename = filename
        if not os.path.exists(self.__filename):
            with open(self.__filename, "w", encoding="utf-8") as file:
                json.dump([], file)

    def __read_vacancies(self) -> List[Dict[str, Any]]:
        """Чтение вакансий из файла"""
        try:
            with open(self.__filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def __write_vacancies(self, vacancies: List[Dict[str, Any]]) -> None:
        """Запись вакансий в файл"""
        with open(self.__filename, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)

    def __vacancy_to_dict(self, vacancy: Vacancy) -> Dict[str, Any]:
        """Преобразование объекта Vacancy в словарь"""
        return {
            "title": vacancy.title,
            "url": vacancy.url,
            "salary_from": vacancy.salary_from,
            "salary_to": vacancy.salary_to,
            "currency": vacancy.currency,
            "description": vacancy.description,
        }

    def __dict_to_vacancy(self, vacancy_dict: Dict[str, Any]) -> Vacancy:
        """Преобразование словаря в объект Vacancy"""
        return Vacancy(
            title=vacancy_dict["title"],
            url=vacancy_dict["url"],
            salary={
                "from": vacancy_dict["salary_from"],
                "to": vacancy_dict["salary_to"],
                "currency": vacancy_dict["currency"],
            },
            description=vacancy_dict["description"],
        )

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Добавление вакансии в файл"""
        vacancies = self.__read_vacancies()
        vacancy_dict = self.__vacancy_to_dict(vacancy)

        # Проверка на дубликаты
        if vacancy_dict not in vacancies:
            vacancies.append(vacancy_dict)
            self.__write_vacancies(vacancies)

    def get_vacancies(self, criteria: Optional[dict] = None) -> List[Vacancy]:
        """Получение вакансий по критериям"""
        vacancies_data = self.__read_vacancies()
        vacancies = [self.__dict_to_vacancy(v) for v in vacancies_data]

        if not criteria:
            return vacancies

        filtered_vacancies = []
        for vacancy in vacancies:
            match = True
            for key, value in criteria.items():
                if (
                    key == "keyword"
                    and value.lower() not in vacancy.description.lower()
                ):
                    match = False
                    break
                elif (key == "salary_from" and (vacancy.salary_from or 0)
                      < value):
                    match = False
                    break
                elif key == "salary_to" and (vacancy.salary_to or
                                             float("inf")) > value:
                    match = False
                    break
            if match:
                filtered_vacancies.append(vacancy)

        return filtered_vacancies

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Удаление вакансии из файла"""
        vacancies = self.__read_vacancies()
        vacancy_dict = self.__vacancy_to_dict(vacancy)

        if vacancy_dict in vacancies:
            vacancies.remove(vacancy_dict)
            self.__write_vacancies(vacancies)
