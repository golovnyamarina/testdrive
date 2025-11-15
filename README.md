## Проект по django "Запись на тестдрайв"
### Руководство пользователя.
Проект представляет собой сайт из 3-х страниц с функцией записи на тестдрайв. 
На главной странице отображаются активные записи клиентов

<img width="789" height="442" alt="image" src="https://github.com/user-attachments/assets/3dfc3bd5-12ac-44ca-9566-6ad5efa176fc" />

На странице "О компании" содержится описание деятельности компании.

<img width="1515" height="707" alt="image" src="https://github.com/user-attachments/assets/09ad05b1-3f58-4ba5-b5ac-62481b0addc4" />

Для записи на тестдрайв нужно перейти на страницу "Тестдрайв" и заполнить форму.

<img width="908" height="733" alt="image" src="https://github.com/user-attachments/assets/737c28c0-51fa-404b-ad53-525f887242ed" />

После заполнения и отправки формы ваша запись появится на главной странице.

<img width="899" height="587" alt="image" src="https://github.com/user-attachments/assets/ce829680-547f-41ac-8a66-51d80dedda0d" />

### Руководство программиста
> Django — это высокоуровневый, бесплатный фреймворк для веб-разработки на языке Python, который позволяет создавать безопасные и масштабируемые веб-сайты быстрее и проще, предоставляя готовые компоненты для типовых задач.
Начало работы со средой:
---
#  Создание вирт.среды
python -m venv .venv
# Активация вирт.среды
.venv\Scripts\activate
# Установка библиотеки
pip install django==5
# Создаю проект
djanho-admin startproject testdrive
# Перехожу
cd testdrive
# Создаю приложение
python manage.py startapp myapp
# Перейдите в файл settings.py и в разделе INSTALLED_APPS впишите(в конец) название приложения "myapp"
# Запускаю проект
python manage.py runserver 
---

