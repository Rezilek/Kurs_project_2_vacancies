from typing import List

from src.models.vacancy import Vacancy


def filter_vacancies(
    vacancies: List[Vacancy], filter_words: List[str]
) -> List[Vacancy]:
    """
    Фильтрация вакансий по ключевым словам в описании

    :param vacancies: Список вакансий
    :param filter_words: Список ключевых слов
    :return: Отфильтрованный список вакансий
    """
    if not filter_words:
        return vacancies

    filtered = []
    for vacancy in vacancies:
        description = vacancy.description.lower()
        if any(word.lower() in description for word in filter_words):
            filtered.append(vacancy)
    return filtered


def get_vacancies_by_salary(
    vacancies: List[Vacancy], salary_range: str
) -> List[Vacancy]:
    """
    Фильтрация вакансий по диапазону зарплат

    :param vacancies: Список вакансий
    :param salary_range: Диапазон зарплат (например: "100000-150000")
    :return: Отфильтрованный список вакансий
    """
    if not salary_range:
        return vacancies

    try:
        min_salary, max_salary = map(int, salary_range.split("-"))
    except ValueError:
        return vacancies

    filtered = []
    for vacancy in vacancies:
        salary_from = vacancy.salary_from or 0
        salary_to = vacancy.salary_to or float("inf")

        if salary_from >= min_salary and salary_to <= max_salary:
            filtered.append(vacancy)

    return filtered


def sort_vacancies(vacancies: List[Vacancy]) -> List[Vacancy]:
    """
    Сортировка вакансий по зарплате (по убыванию)

    :param vacancies: Список вакансий
    :return: Отсортированный список вакансий
    """
    return sorted(vacancies, reverse=True)


def get_top_vacancies(vacancies: List[Vacancy], top_n: int) -> List[Vacancy]:
    """
    Получение топ N вакансий

    :param vacancies: Список вакансий
    :param top_n: Количество вакансий для вывода
    :return: Список топ N вакансий
    """
    return vacancies[:top_n] if top_n > 0 else vacancies


def print_vacancies(vacancies: List[Vacancy]) -> None:
    """
    Вывод вакансий в консоль

    :param vacancies: Список вакансий для вывода
    """
    if not vacancies:
        print("Вакансии не найдены")
        return

    for i, vacancy in enumerate(vacancies, 1):
        print(f"Вакансия #{i}")
        print(vacancy)
        print("-" * 50)
