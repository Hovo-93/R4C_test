# R4C - Robots for consumers

## Небольшая предыстория.
Давным-давно, в далёкой-далёкой галактике, была компания производящая различных 
роботов. 

Каждый робот(**Robot**) имел определенную модель выраженную двух-символьной 
последовательностью(например R2). Одновременно с этим, модель имела различные 
версии(например D2). Напоминает популярный телефон различных моделей(11,12,13...) и его версии
(X,XS,Pro...). Вне компании роботов чаще всего называли по серийному номеру, объединяя модель и версию(например R2-D2).

Также у компании были покупатели(**Customer**) которые периодически заказывали того или иного робота. 

Когда роботов не было в наличии - заказы покупателей(**Order**) попадали в список ожидания.

---
Список технологий: Python, Django, db.sqlite3, Celery, Redis

## Подготовка и запуск проекта

#### Шаг 1. Клонируйте репозиторий себе на компьютер
Введите команду:
```bash
git clone https://github.com/Hovo-93/R4C_test.git
```
#### Шаг 2. Для создания и активации виртуального окружения:
```python
    python -m venv venv

    venv\Scripts\activate - для Windows;
    
    source venv/bin/activate - для Linux и MacOS.
```
#### Шаг 3.Создаем и применяем миграции:
```python
    python manage.py makemigrations
    python manage.py migrate
```
#### Шаг 4.Устанавливаем все зависимости:
```python
    pip install -r requirements.txt
```

#### Шаг 5. Создайте в клонированной директории файл .env можете использовать эти данные
Пример:
```bash

CELERY_BROKER_URL = redis://localhost:6379/0
CELERY_RESULT_BACKEND = redis://localhost:6379/0
EMAIL_HOST_USER = ovo.aroyan@gmail.ru
EMAIL_HOST_PASSWORD = lmeldhqtjmqqzvub
FROM_EMAIL = ovo.aroyan@gmail.com

```

#### Шаг 6.Создаем  суперюзера для входа в Django Admin
```python
  python manage.py createsuperuser
```

## Примеры
Для формирования запросов и ответов использована программа [Postman](https://www.postman.com/).

### 1.API-endpoint, принимающий и обрабатывающий информацию в формате JSON
```json
  POST http://127.0.0.1:8000/api/add_robot/
#BODY(json)
{
    {"model":"R2","version":"M2","created":"2023-10-05 23:59:59"},
    {"model":"13","version":"XS","created":"2023-01-01 00:00:00"},
    {"model":"X5","version":"LT","created":"2023-01-01 00:00:01"}
}
```
### 2. Скачивание по прямой ссылке Excel-файл со сводкой по суммарным показателям производства роботов
```html
  Переходим по ссылке http://127.0.0.1:8000/api/download_exel/
```
### 3. Отправка уведомлений о налиии робота
```json
POST http://127.0.0.1:8000/api/order/

# Body(json)
{
   "customer": "test@mail.ru",
   "robot_serial": "ABC12"
}
```