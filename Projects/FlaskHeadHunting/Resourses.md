# Resourses

# Часть первая - Создание каркаса

В файле resourses.py создать функции `render_home_page()`, 'render_user_profile_page()' и т.д. Каждая функция должна возвращать правильный вызов render_template()

## Часть вторая - Связь с content_manager

Каждая функция должна подтягивать нужные данные из content_manager. Для user_profile - информацию о пользователе и так далее.

## Часть третья - Создание и правильное заполнение шаблона

Переделать каждый html документ в jinja2 щаблон, с заполнением с помощью моделей, полученных из вызова content_manager'а