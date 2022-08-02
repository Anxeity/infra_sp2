## Проект YaMDb

Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка». В каждой категории есть произведения: книги, фильмы или музыка. Произведению может быть присвоен жанр. Новые жанры может создавать только администратор. Пользователи могут оставить к произведениям текстовые отзывы и поставить произведению оценку в диапазоне от одного до десяти. Из пользовательских оценок формируется усреднённая оценка произведения — рейтинг. Присутствует возможность комментирования отзывов.

Функционал API:
1) Просмотр произведений (кино, музыка, книги), которые подразделяются по жанрам и категориям..
2) Возможность оставлять отзывы на произведения и ставить им оценки, на основе которых построена система рейтингов.
3) Комментирование оставленных отзывов.

Проект разработан командой из трех человек с использованием Git в рамках учебного курса Яндекс.Практикум.

## Разработчики

1. Дамир Шамсутдинов (https://github.com/alvaresShD):
Разработка системы регистрации и аутентификации, прав доступа, работы с токеном, системы подтверждения через e-mail.

2. Михаил Глазов (https://github.com/Anxeity):
Разработка моделей "категории" (Categories), "жанры" (Genres) и "произведения" (Titles), а также разработка представлений и эндпойнтов для них.

3. Алексей Смирнов (https://github.com/AxelVonReems):
Разработка моделей "отзывы" (Review) и "комментарии" (Comments), а также разработка представлений и эндпойнтов для них. Настройка прав доступа для запросов. Реализация системы рейтингов.

## Стек технологий

Python 3.9
Django 2.2.16
Django REST Framework 3.12.4
Django REST Framework simplejwt 5.1.0

## Как запустить проект

#### 1.Клонируем репозиторий на локальную машину:
```
https://github.com/Anxeity/infra_sp2
git clone https://github.com/Anxeity/infra_sp2.git
```
#### 2.Создать .env файл внутри директории infra (на одном уровне с docker-compose.yaml) Пример .env файла:
```
SECRET_KEY = 'p&l%385148kslhtyn^##a1)ilz@4zqj=rq&agdol^##zgl9(vs'
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432

```
#### 3. Запуск тестов (опционально, если не нужно - переходите к следующему шагу)
#### Создаем и активируем виртуальное окружение:
Для Mac или Linux
```
cd infra_sp2
python3 -m venv venv
source venv/bin/activate
cd api_yamdb
pip install -r requirements.txt
cd ..
pytest
```

Для Windows
```
cd infra_sp2
python -m venv venv
source venv/Scripts/activate
cd api_yamdb
pip install -r requirements.txt
cd ..
pytest
```

#### 4.Запуск Docker контейнеров: Запустите docker-compose
```
cd infra/
docker-compose up -d --build
```

#### 5.Cоздайте суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```
#### 6.Проверьте доступность сервиса
```
http://localhost/admin
```

### Документация
```
http://localhost/redoc/
```
## Права доступа: Доступно без токена.
```
GET /api/v1/categories/ - Получение списка всех категорий
GET /api/v1/genres/ - Получение списка всех жанров
GET /api/v1/titles/ - Получение списка всех произведений
GET /api/v1/titles/{title_id}/reviews/ - Получение списка всех отзывов
GET /api/v1/titles/{title_id}/reviews/{review_id}/comments/ - Получение списка всех комментариев к отзыву
```

## Права доступа: Администратор
__GET /api/v1/users/__ - Получение списка всех пользователей


## Получение JWT-токена:
__POST /api/v1/auth/token/__
   
```
{
  "username": "string",
  "confirmation_code": "string"
}
```

[Примеры запросов и документация по ссылке](http://127.0.0.1:8000/redoc/)
