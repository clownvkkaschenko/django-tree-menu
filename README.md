# Django-tree-menu
Джанго приложение, которое реализовывает древовидное меню. Позволяет вносить/редактировать меню через админку, и нарисовать на любой нужной странице меню по названию.
```
{% draw_menu 'name' %}
```
# Запуск проекта
Склонируйте репозиторий к себе на компьютер
```
git clone git@github.com:clownvkkaschenko/django-tree-menu.git
```
Перейдите в папку с проектом, создайте и активируйте виртуальное окружение
```
python -m venv venv
source venv/Scripts/activate
```
Перейдите в папку с приложением /app/ установите зависимости и запустите проект
```
pip install -r requirements.txt
```
Выполните миграции
```
python manage.py makemigrations
python manage.py migrate
```
После этого проект будет готов к работе по команде
```
python manage.py runserver
```