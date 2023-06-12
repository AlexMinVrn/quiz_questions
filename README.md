# quiz_questions
Платформа вопросов для викторины

### Описание
В сервисе реализовано REST API, принимающее на вход POST запросы вида:
```
{"questions_num": integer}
```
После получения запроса сервис, в свою очередь, запрашивает с публичного API (англоязычные вопросы для викторин) https://jservice.io/api/random?count=1 указанное в полученном запросе количество вопросов.

Полученные ответы сохраняются в базе данных: 
1. ID вопроса
2. Текст вопроса
3. Текст ответа
4. Дата создания вопроса

В случае, если в БД имеется такой же вопрос, к публичному API с викторинами выполняются дополнительные запросы до тех пор, пока не будет получен уникальный вопрос для викторины.

Ответом на POST запрос {"questions_num": integer} является предыдущей сохранённый вопрос для викторины. В случае его отсутствия - пустой объект.

### Технологии
- [Python] v3.7
- [Django] v3.2.19
- [Django REST framework] v3.14.0
- [Docker]
- Gunicorn
- nginx
### Запуск проекта
Этот проект работает с приложением Docker. Если на вашем компьютере он не установлен, зайдите  
на официальный сайт [Docker], скачайте и запустите установочный файл для вашей операционной системы.  

- Клонируйте проект на свой компьютер:
```YAML
git clone git@github.com:AlexMinVrn/quiz_questions.git
```
- Создайте в директории infra/ файл .env и наполните его следующими данными
```YAML
SECRET_KEY='b)*-@1niuu)vj^^f-7w0xm#+l1v)*c6%8pfej4f+ut#=nt$juq'
DB_ENGINE= django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=пароль для подключения к БД (установите свой)
DB_HOST=db
DB_PORT=5432
```
- Из директории infra выполните команду:
```BASH
docker-compose up -d --build
```
- Выполните миграции:
```BASH
docker-compose exec web python manage.py migrate
```
- Создайте суперпользователя:
```BASH
docker-compose exec web python manage.py createsuperuser
```
- Соберите статику:
```BASH
docker-compose exec web python manage.py collectstatic --no-input
```
Сделайте POST запрос по адресу:

<http://localhost/api/questions_num>

В теле запроса напишите:

```
{"questions_num": integer}
```
где integer - это количество вопросов  
##### в ответ вы получите предыдущий сохранённый вопрос для викторины.
### Автор
- [Александр Минаев]

[//]: # 
  [Python]: <https://www.python.org>
  [Django REST framework]: <https://www.django-rest-framework.org>
  [Django]: <https://www.djangoproject.com>
  [Docker]: <https://www.docker.com>
  [Pillow]: <https://pillow.readthedocs.io/>
  [Александр Минаев]: <https://github.com/AlexMinVrn>