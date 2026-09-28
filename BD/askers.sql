-- 1. Таблица групп
CREATE TABLE Groups (
    group_id    CHAR(5)      NOT NULL,
    group_name  VARCHAR(100) NOT NULL,
    PRIMARY KEY (group_id),
    UNIQUE (group_name)
)

-- 2. Таблица студентов
CREATE TABLE Students (
    student_id   INT          NOT NULL,
    student_name VARCHAR(100) NOT NULL,
    group_id     CHAR(5)      NOT NULL,
    PRIMARY KEY (student_id),
    FOREIGN KEY (group_id) REFERENCES Groups(group_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
)

-- 3. Таблица предметов
CREATE TABLE Subjects (
    subject_id   INT          NOT NULL,
    subject_name VARCHAR(100) NOT NULL,
    PRIMARY KEY (subject_id),
    UNIQUE (subject_name)
)

-- 4. Таблица преподавателей
CREATE TABLE Teachers (
    teacher_id   INT          NOT NULL,
    teacher_name VARCHAR(100) NOT NULL,
    PRIMARY KEY (teacher_id)
)

-- 5. Таблица экзаменов 
CREATE TABLE Exams (
    student_id INT  NOT NULL,
    subject_id INT  NOT NULL,
    exam_date  DATE NOT NULL,
    teacher_id INT  NOT NULL,
    grade      INT  NOT NULL,
    PRIMARY KEY (student_id, subject_id, exam_date),
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CHECK (grade BETWEEN 1 AND 5)
)