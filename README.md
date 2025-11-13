\# My First Django Project



Это мой первый проект на Django, созданный для учебного задания.



\## Описание проекта



Простой Django проект с базовой структурой:

\- Главная страница с приветствием

\- Настроенные URL-маршруты

\- Виртуальное окружение

\- Готовый к работе сервер разработки



\## Структура проекта



my\_django\_project/

├── myapp/

│   ├── \_\_init\_\_.py

│   ├── admin.py

│   ├── apps.py

│   ├── migrations/

│   ├── models.py

│   ├── tests.py

│   ├── urls.py

│   └── views.py

├── myproject/

│   ├── \_\_init\_\_.py

│   ├── asgi.py

│   ├── settings.py

│   ├── urls.py

│   └── wsgi.py

├── venv/

├── .gitignore

├── manage.py

├── requirements.txt

└── README.md



\## Установка и запуск



1\. Клонировать репозиторий:

git clone https://github.com/savoya19/my-django-project.git

cd my\_django\_project



2\. Активировать виртуальное окружение:

venv\\Scripts\\activate



3\. Установить зависимости:

pip install -r requirements.txt



4\. Запустить сервер:

python manage.py runserver



5\. Открыть в браузере:

http://127.0.0.1:8000/



\## Требования



\- Python 3.x

\- Django 5.2.8





