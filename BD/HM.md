часть 1
    -(student_id, subject_id, exam_date)
    -
| student_id | student_name | group_id | group_name | teacher_id | teacher_name | subject_id | subject_name | exam_date | grade |
|------------|--------------|----------|------------|------------|--------------|------------|--------------|-----------|-------|
|   int      | varchar(100) |varchar(10)|varchar(20)|  integer   | varchar(100) |    integer | varchar(50)  |   date    |integer|
|------------|--------------|----------|------------|------------|--------------|------------|--------------|-----------|-------|
| 1          | Петров П.    | G-1      | Группа А   | 5          | Петрова М.   | 1          | Математика   | 2026-01-15| 4     |
| 2          | Иванов И.    | G-1      | Группа А   | 7          | Смирнов А.   | 2          | Физика       | 2026-01-20| 3     |
| 3          | Сидоров С.   | G-2      | Группа Б   | 5          | Петрова М.   | 1          | Математика   | 2026-01-18| 5     |
| 4          | Петров П.    | G-1      | Группа А   | 8          | Козлова Е.   | 3          | Информатика  | 2026-01-25| 5     |
| 5          | Кузнецов К.  | G-2      | Группа Б   | 7          | Смирнов А.   | 2          | Физика       | 2026-01-22| 4     |
    -   student_id → student_name — студент имеет одно имя.

        student_id → group_id 

        group_id → group_name

        teacher_id → teacher_name 

        subject_id → subject_name  

        (student_id, subject_id, exam_date) → grade 

        (student_id, subject_id, exam_date) → teacher_id
    - 1НФ


┌─────────────┐       ┌─────────────┐       ┌─────────────┐
│   Groups    │       │  Students   │       │  Subjects   │
├─────────────┤       ├─────────────┤       ├─────────────┤
│ group_id PK │◄──────│ group_id FK │       │ subject_id PK│
│ group_name  │       │ student_id PK│      │ subject_name │
└─────────────┘       │ student_name│       └─────────────┘
                      └──────┬──────┘              ▲
                             │                     │
                             │                     │
┌─────────────┐       ┌──────▼─────────────────────┴──────┐
│  Teachers   │       │           Exams                   │
├─────────────┤       ├───────────────────────────────────┤
│ teacher_id PK│◄─────│ teacher_id FK                     │
│ teacher_name │      │ student_id FK                     │
└─────────────┘       │ subject_id FK                     │
                      │ exam_date                         │
                      │ grade                             │
                      │ PK (student_id, subject_id, exam_date)│
                      └───────────────────────────────────┘