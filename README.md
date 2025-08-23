# Проект "Поиск вакансий"

## 1. Настройка проекта

### 1.1. Создание структуры проекта

vacancy_search/
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
├── src/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── abstract_api.py
│   │   └── hh_api.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── vacancy.py
│   ├── storage/
│   │   ├── __init__.py
│   │   ├── abstract_storage.py
│   │   └── json_storage.py
│   └── utils/
│       ├── __init__.py
│       └── filters.py
└── tests/
    ├── __init__.py
    ├── test_api.py
    ├── test_vacancy.py
    └── test_storage.py

### 1.2. Настройка окружения

1. Создаем виртуальное окружение:

python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows

2. Создаем файл `requirements.txt`:

requests==2.31.0
pytest==7.4.0
python-dotenv==1.0.0

3. Устанавливаем зависимости:

pip install -r requirements.txt

### 1.3. Настройка .gitignore

Создаем файл `.gitignore`:

venv/
__pycache__/
*.pyc
*.pyo
*.pyd
.DS_Store
.env
*.json
*.csv
*.xlsx

## 2. Реализация кода

### 2.1. Абстрактный класс для работы с API (abstract_api.py)

### 2.2. Класс для работы с API HeadHunter (hh_api.py)

### 2.3. Класс для работы с вакансиями (vacancy.py)

### 2.4. Абстрактный класс для работы с хранилищем (abstract_storage.py)

### 2.5. Класс для работы с JSON-хранилищем (json_storage.py)

### 2.6. Утилиты для фильтрации (filters.py)

### 2.7. Основной скрипт (main.py)

## 3. Тестирование

### 3.1. Тесты для API (test_api.py)

### 3.2. Тесты для вакансий (test_vacancy.py)

### 3.3. Тесты для хранилища (test_storage.py)

## 4. Запуск проекта

1. Убедитесь, что все зависимости установлены:
 
pip install -r requirements.txt

2. Запустите основной скрипт:

python main.py

3. Для запуска тестов:

pytest tests/

## 5. Дополнительные возможности для расширения

1. Добавьте поддержку других платформ с вакансиями (например, SuperJob)
2. Реализуйте кэширование запросов к API
3. Добавьте возможность экспорта в другие форматы (CSV, Excel)
4. Реализуйте графический интерфейс с помощью Tkinter или PyQt
5. Добавьте систему логирования для отслеживания ошибок

Этот проект предоставляет полную реализацию системы поиска и управления вакансиями с HeadHunter 
с соблюдением всех требований и принципов ООП.

## Требования

- Python 3.8+
- Poetry для управления зависимостями

## Лицензия

MIT License

## Контакты

**Автор:** Резиля Столярова
**Email:** rezilek5177@gmail.com
**GitHub:** [Rezilek](https://github.com/Rezilek)
