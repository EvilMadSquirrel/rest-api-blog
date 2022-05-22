### Тестовое задание по реализации REST API
#### Описание

| Function                            | REQUEST | Endpoint                                                  | form-data |
|-------------------------------------|---------|-----------------------------------------------------------|-----------|
| Список пользователей                | GET     | http://127.0.0.1:8000/api/v1/users/                       |           |
| Подробная информация о пользователе | GET     | http://127.0.0.1:8000/api/v1/users/{int:id}               |           |
| Лента новостей пользователя         | GET     | http://127.0.0.1:8000/api/v1/users/{int:id}/news/         |           |
| Посты пользователя                  | GET     | http://127.0.0.1:8000/api/v1/users/{int:id}/posts/        |           |
| Подписка на других пользователей    | PUT     | http://127.0.0.1:8000/api/v1/users/{int:id}               | follow    |
| Отметить пост прочитанным           | PUT     | http://127.0.0.1:8000/api/v1/users/{int:id}/news/{int:id} | readers   |


#### Установка и настройка

Установить make. Установить Poetry. Установить Docker Engine и Docker Compose.

```bash
git clone https://github.com/EvilMadSquirrel/rest-api-blog.git
cd rest-api-blog
```
Создайте .env файл по образцу (.env_example)
Сгенерируйте секретный ключ:
```bash
make secretkey
```
Запишите его в .env файл в поле SECRET_KEY

Запустите настройку проекта:

```bash
make setup
```

В процессе настройки создайте суперпользователя.

Запуск проекта:

```bash
make start
```


По необходимости можно заполнить базу тестовыми данными.
В файле data_generator.py укажите желаемое количество пользователей и постов в константах BLOGGERS_COUNT и POSTS_COUNT

Запустите консоль Django:
```bash
make console
```

Выполните последовательно следующие команды:
```bash
from data_generator import create_users, fill_blogs
create_users()
fill_blogs()
exit()
```
