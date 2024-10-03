# drf-postgres

Simple Django DRF application with Postgres database

This is a simple CRUD application built with Python Django/DRF and PostgresSQL.
The main purpose is to demonstrate Django/DRF functionalities. For easy
testing, We will use docker to containerize all the applications.

In this system, we will build a course management system, where, there will be
2 types of users, the teachers, and the students. Only authenticated users can
make `POST/PUT/PATCH/DELETE` requests.

Celery is integrated to send email to both teacher and registered students for 
any specific course on the day of the exam [see the model in 
[models.py](./courses/models.py)].

## Docker
Copy [sample.env](./sample.env) into [.env](./.env) and updatetbe values 
accordingly. Then, spin up the containers by

```
$ docker compose up
```

Once you are done, remove all the containers and associated objects by
```
$ docker compose down --rmi local -v
```

## API Documentation

* **Swagger-UI**: http://localhost:8000/api/schema/swagger-ui/
* **Redoc**: http://localhost:8000/api/schema/redoc/
## Tasks

| **Task ID** | **Details**                                     | **Status**         | **Comment(s)** |
|-------------|-------------------------------------------------|--------------------|----------------|
| Task-1      | Create Django/DRF app outline                   | :white_check_mark: |                |
| Task-2      | Create docker compose for Postgres and PG Admin | :white_check_mark: |                |
| Task-3      | Create Django/DRF app                           | :white_check_mark: |                |
| Task-4      | Define models                                   | :white_check_mark: |                |
| Task-5      | Define Views and URLs                           | :white_check_mark: |                |
| Task-6      | Write Tests                                     | :x:                |                |
| Task-7      | create custom command                           | :white_check_mark: |                |
| Task-8      | Celery + RabbitMQ for task scheduling           | :white_check_mark: |                |
| Task-9      | API Documentation                               |                    |                |
| Task-10     | To be amended in the future                     | :x:                |                |

## References
* https://www.django-rest-framework.org/api-guide/serializers/#dealing-with-nested-objects
* https://github.com/beda-software/drf-writable-nested
* https://www.django-rest-framework.org/api-guide/serializers/