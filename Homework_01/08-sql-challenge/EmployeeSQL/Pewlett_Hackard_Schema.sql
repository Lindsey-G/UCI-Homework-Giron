-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/WOHo36
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- CREATE TABLE for Dept_departments. Set PRIMARY KEY at dept_no.
CREATE TABLE Dept_departments (
    dept_no VARCHAR(50)   NOT NULL,
    dept_name VARCHAR(50)   NOT NULL,
    CONSTRAINT pk_Dept_departments PRIMARY KEY (
        dept_no
     )
);

-- CREATE TABLE for Titles. Set PRIMARY KEY as title_id.
CREATE TABLE Titles (
    title_id VARCHAR(50)   NOT NULL,
    title VARCHAR(50)   NOT NULL,
    CONSTRAINT pk_Titles PRIMARY KEY (
        title_id
     )
);

-- CREATE TABLE for Employee. Set PRIMARY KEY as emp_no.
CREATE TABLE Employee (
    emp_no INT   NOT NULL,
    emp_title_id VARCHAR   NOT NULL,
    birth_date DATE   NOT NULL,
    first_name VARCHAR   NOT NULL,
    last_name VARCHAR   NOT NULL,
    sex VARCHAR(1)   NOT NULL,
    hire_date DATE   NOT NULL,
    CONSTRAINT pk_Employee PRIMARY KEY (
        emp_no
     )
);

-- CREATE TABLE for Dept_emp.
CREATE TABLE Dept_emp (
    emp_no INT   NOT NULL,
    dept_no VARCHAR   NOT NULL
);

-- CREATE TABLE for Dept_manager.
CREATE TABLE Dept_manager (
    dept_no VARCHAR   NOT NULL,
    emp_no INT   NOT NULL
);

-- CREATE TABLE for Salaries.
CREATE TABLE Salaries (
    emp_no INT   NOT NULL,
    salary INT   NOT NULL
);

-- Using ALTER TABLE for Employee table, add FOREIGN KEY emp_title_id fro Titles table.
ALTER TABLE Employee ADD CONSTRAINT fk_Employee_emp_title_id FOREIGN KEY(emp_title_id)
REFERENCES Titles (title_id);

-- Using ALTER TABLE for Dept_emp table, add FOREIGN KEY emp_no from Employee table.
ALTER TABLE Dept_emp ADD CONSTRAINT fk_Dept_emp_emp_no FOREIGN KEY(emp_no)
REFERENCES Employee (emp_no);

-- Using ALTER TABLE for Dept_emp table, add FOREIGN KEY dept_no from Dept_departments table.
ALTER TABLE Dept_emp ADD CONSTRAINT fk_Dept_emp_dept_no FOREIGN KEY(dept_no)
REFERENCES Dept_departments (dept_no);

-- Using ALTER TABLE for Dept_manager table, add FOREIGN KEY dept from Dept_departments table.
ALTER TABLE Dept_manager ADD CONSTRAINT fk_Dept_manager_dept_no FOREIGN KEY(dept_no)
REFERENCES Dept_departments (dept_no);

-- Using ALTER TABLE for Dept_manager table, add FOREIGN KEY emp_no from Employee table.
ALTER TABLE Dept_manager ADD CONSTRAINT fk_Dept_manager_emp_no FOREIGN KEY(emp_no)
REFERENCES Employee (emp_no);

-- Using ALTER TABLE for Salaries table, add FOREIGN KEY emp_no from Employee table.
ALTER TABLE Salaries ADD CONSTRAINT fk_Salaries_emp_no FOREIGN KEY(emp_no)
REFERENCES Employee (emp_no);

