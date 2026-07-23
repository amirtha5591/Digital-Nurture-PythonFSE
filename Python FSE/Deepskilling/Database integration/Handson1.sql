##TASK 1
-- Create Database
CREATE DATABASE college_db;

-- Use Database
USE college_db;

-- 1. Departments Table
CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL,
    hod_name VARCHAR(100),
    budget DECIMAL(12,2)
);

-- 2. Students Table
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    date_of_birth DATE,
    department_id INT,
    enrollment_year INT,
    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);

-- 3. Courses Table
CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(150) NOT NULL,
    course_code VARCHAR(20) UNIQUE,
    credits INT,
    department_id INT,
    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);

-- 4. Enrollments Table
CREATE TABLE enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    grade CHAR(2),
    FOREIGN KEY (student_id)
        REFERENCES students(student_id),
    FOREIGN KEY (course_id)
        REFERENCES courses(course_id)
);

-- 5. Professors Table
CREATE TABLE professors (
    professor_id INT AUTO_INCREMENT PRIMARY KEY,
    prof_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    department_id INT,
    salary DECIMAL(10,2),
    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);

-- Verify Tables
SHOW TABLES;

DESCRIBE departments;
DESCRIBE students;
DESCRIBE courses;
DESCRIBE enrollments;
DESCRIBE professors;
TASK 2
-- ===========================
-- Task 2: Verify Normalisation
-- ===========================

-- 1NF:
-- All tables contain atomic (single) values in each column.
-- There are no repeating groups or multiple values stored in a single field.
-- Example violation: Storing multiple phone numbers in one column (9876543210,9123456789).

-- 2NF:
-- Every table uses a primary key, and all non-key attributes depend on the whole primary key.
-- In the enrollments table, student_id and course_id together uniquely identify an enrollment.
-- enrollment_date and grade depend on the complete enrollment record, not just one key.

-- 3NF:
-- There are no transitive dependencies in the schema.
-- Department details such as dept_name are stored only in the departments table.
-- The students table stores only department_id as a foreign key.
-- This avoids data redundancy and maintains database consistency.

-- 3NF Analysis for Enrollments:
-- The enrollments table contains only enrollment-specific information.
-- grade and enrollment_date depend directly on the enrollment record.
-- No non-key attribute depends on another non-key attribute.
-- Therefore, the enrollments table satisfies Third Normal Form (3NF).
TASK 3
-- ===========================
-- Task 3: Alter and Extend the Schema
-- ===========================

-- 10. Add phone_number column to students table
ALTER TABLE students
ADD phone_number VARCHAR(15);

-- 11. Add max_seats column to courses table
ALTER TABLE courses
ADD max_seats INT DEFAULT 60;

-- 12. Add CHECK constraint for grade
ALTER TABLE enrollments
ADD CONSTRAINT chk_grade
CHECK (grade IN ('A', 'B', 'C', 'D', 'F') OR grade IS NULL);

-- 13. Rename hod_name to head_of_dept
ALTER TABLE departments
RENAME COLUMN hod_name TO head_of_dept;

-- 14. Drop phone_number column
ALTER TABLE students
DROP COLUMN phone_number;

-- Verify the changes
DESCRIBE departments;
DESCRIBE students;
DESCRIBE courses;
DESCRIBE enrollments;
