# Flask Project Template

> Tagline
>
> [![](https://img.shields.io/badge/some-badge-lightblue)](https://shields.io 'Badges website')

## Technology stack

- python3
- Flask + addons
- SQLAlchemy ORM
- VK API

## Инструкция по запуску

1. Склонируйте репозиторий и перейдите в директорию с проектом
    ```
    git clone <link>
    cd <project_directory>
    ```
    
2. Создайте и активируйте виртуальное окружение
    ```
    virtualenv --python=python3 venv
    source venv/bin/activate
    ```

3. Установите зависимости
    ```
    pip3 install -r requirements.txt
    ```

4. Создайте таблицы в БД
    ```
    python3 manage.py db_reset
    ```

5. Запустите веб-приложение
    ```
    python3 manage.py runserver
    ```

Developed by [](https://example.com 'hover comment')
