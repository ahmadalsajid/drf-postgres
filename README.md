# drf-postgres
Simple Django DRF application with Postgres database

This is a simple CRUD application built with Python Django/DRF and PostgresSQL.
The main purpose is to demonstrate Django/DRF functionalities. For easy 
testing, We will use docker to containerize all the applications.

In this system, we will build a course management system, where, there will be
2 types of users, the teachers, and the students. For simplicity, admin will 
create the teachers, students and courses. The teachers can assign courses to 
the students, list, modify all the details. Students can view their assigned 
courses. More details to be added with the progress.

## Docker 

```
$ docker compose up
$ docker compose down --rmi local -v
```

## Tasks

| **Task ID** | **Details**                                     | **Status**         | **Comment(s)** |
|-------------|-------------------------------------------------|--------------------|----------------|
| Task-1      | Create Django/DRF app outline                   | :white_check_mark: |                |
| Task-2      | Create docker compose for Postgres and PG Admin | :white_check_mark: |                |
| Task-3      | Create Django/DRF app                           | :white_check_mark: |                |
| Task-4      | Define models                                   | :x:                |                |
| Task-5      | Define Views and URLs                           | :x:                |                |
| Task-6      | Write Tests                                     | :x:                |                |
| Task-7      | To be amended in the future                     | :x:                |                |

