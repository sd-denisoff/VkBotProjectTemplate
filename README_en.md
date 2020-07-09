# VK bot Project Template

> Tagline
>
> [![](https://img.shields.io/badge/some-badge-lightblue)](https://shields.io 'Badges website')

## Technology stack

- python3
- Flask + addons
- SQLAlchemy ORM
- VK API

## Launch instruction

1. Clone the repository and change the directory
    ```
    git clone <link>
    cd <project_directory>
    ```
    
2. Create a virtual environment and activate it
    ```
    virtualenv --python=python3 venv
    source venv/bin/activate
    ```

3. Install dependencies
    ```
    pip3 install -r requirements.txt
    ```

4. Create tables in the database
    ```
    python3 manage.py db_reset
    ```

5. Launch web application
    ```
    python3 runner.py
    ```

Developed by [someone](https://example.com 'hover comment')
