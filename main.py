from src.api.hh_api import HeadHunterAPI
from src.models.vacancy import Vacancy
from src.storage.json_storage import JSONStorage
from src.utils.filters import (
    filter_vacancies,
    get_vacancies_by_salary,
    sort_vacancies,
    get_top_vacancies,
    print_vacancies
)


def user_interaction(hh_api=None, search_query=None, hh_vacancies_data=None, vacancies=None):
    """Функция для взаимодействия с пользователем"""
    print("Добро пожаловать в программу поиска вакансий!")

    # Инициализация API и хранилища
    hh_api = HeadHunterAPI()
    storage = JSONStorage()

    # Получение параметров от пользователя
    search_query = input("Введите поисковый запрос (например: Python): ").strip()
    top_n = int(input("Введите количество вакансий для вывода в топ N: ").strip())
    filter_words = input("Введите ключевые слова для фильтрации вакансий (через пробел): ").strip().split()
    salary_range = input("Введите диапазон зарплат (например: 100000-150000): ").strip()

    # Получение вакансий с hh.ru
    print("\nПолучаем вакансии с HeadHunter...")
    hh_vacancies_data = hh_api.get_vacancies(search_query)
    vacancies = Vacancy.cast_to_object_list(hh_vacancies_data)

    # Сохранение вакансий
    for vacancy in vacancies:
        storage.add_vacancy(vacancy)

    # Фильтрация и сортировка
    print("\nФильтруем и сортируем вакансии...")
    filtered_vacancies = filter_vacancies(vacancies, filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    # Вывод результатов
    print("\nРезультаты поиска:")
    print_vacancies(top_vacancies)

    print("\nПоиск завершен. Результаты сохранены в файл vacancies.json")

    if __name__ == "__main__":
        user_interaction()
        