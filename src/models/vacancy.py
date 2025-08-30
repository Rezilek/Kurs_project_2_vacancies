from typing import Any, Optional


class Vacancy:
    """Класс для представления вакансии"""

    __slots__ = (
        "_title",
        "_url",
        "_salary_from",
        "_salary_to",
        "_currency",
        "_description",
    )

    def __init__(self, title: str, url: str,
                 salary: dict, description: str):
        """
        Инициализация объекта вакансии

        :param title: Название вакансии
        :param url: Ссылка на вакансию
        :param salary: Информация о зарплате
        :param description: Описание вакансии
        """
        self._title = self._validate_title(title)
        self._url = self._validate_url(url)
        (self._salary_from, self._salary_to,
         self._currency) = self._validate_salary(
            salary
        )
        self._description = self._validate_description(description)

    def _validate_title(self, title: str) -> str:
        """Валидация названия вакансии"""
        if not title or not isinstance(title, str):
            return "Название не указано"
        return title

    def _validate_url(self, url: str) -> str:
        """Валидация URL вакансии"""
        if not url or not isinstance(url, str) or not url.startswith("http"):
            return "URL не указан или невалиден"
        return url

    def _validate_salary(
        self, salary: dict
    ) -> tuple[Optional[int], Optional[int], Optional[str]]:
        """Валидация зарплаты"""
        if not salary:
            return None, None, None

        salary_from = salary.get("from")
        salary_to = salary.get("to")
        currency = salary.get("currency")

        salary_from = salary_from if salary_from is not None else 0
        salary_to = salary_to if salary_to is not None else 0
        currency = currency if currency else "RUR"

        return salary_from, salary_to, currency

    def _validate_description(self, description: str) -> str:
        """Валидация описания вакансии"""
        if not description or not isinstance(description, str):
            return "Описание не указано"
        return description

    @property
    def title(self) -> str:
        return self._title

    @property
    def url(self) -> str:
        return self._url

    @property
    def salary_from(self) -> Optional[int]:
        return self._salary_from

    @property
    def salary_to(self) -> Optional[int]:
        return self._salary_to

    @property
    def currency(self) -> Optional[str]:
        return self._currency

    @property
    def description(self) -> str:
        return self._description

    def __str__(self) -> str:
        salary_info = "не указана"
        if self._salary_from or self._salary_to:
            salary_info = (
                f"{self._salary_from or '?'}-{self._salary_to or '?'}"
                f" {self._currency}"
            )
        return (f"{self._title}\nЗарплата: {salary_info}\nСсылка: "
                f"{self._url}\n")

    def __repr__(self) -> str:
        return f"Vacancy(title='{self._title}', url='{self._url}')"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Vacancy):
            return False
        return (
            self._salary_from == other.salary_from
            and self._salary_to == other.salary_to
        )

    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, Vacancy):
            raise TypeError("Сравнение возможно только между объектами "
                            "Vacancy")
        return (self._salary_from or 0) < (other.salary_from or 0)

    def __gt__(self, other: Any) -> bool:
        if not isinstance(other, Vacancy):
            raise TypeError("Сравнение возможно только между объектами "
                            "Vacancy")
        return (self._salary_from or 0) > (other.salary_from or 0)

    @classmethod
    def cast_to_object_list(cls, vacancies_data: list[dict])\
            -> list["Vacancy"]:
        """Преобразование списка словарей в список объектов Vacancy"""
        vacancies = []
        for vacancy_data in vacancies_data:
            try:
                vacancy = cls(
                    title=vacancy_data.get("name", ""),
                    url=vacancy_data.get("alternate_url", ""),
                    salary=vacancy_data.get("salary", {}),
                    description=vacancy_data.get("snippet",
                                                 {}).get("requirement", "")
                    or vacancy_data.get("snippet",
                                        {}).get("responsibility", ""),
                )
                vacancies.append(vacancy)
            except Exception as e:
                print(f"Ошибка при создании вакансии: {e}")
        return vacancies
