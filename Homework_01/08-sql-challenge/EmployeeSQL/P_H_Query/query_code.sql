-- -- CREATE TABLE for Dept_departments. Set PRIMARY KEY at dept_no.
-- CREATE TABLE Dept_departments (
--     dept_no VARCHAR(50)   NOT NULL,
--     dept_name VARCHAR(50)   NOT NULL,
--     CONSTRAINT pk_Dept_departments PRIMARY KEY (
--         dept_no
--      )
-- );

-- -- CREATE TABLE for Titles. Set PRIMARY KEY as title_id.
-- CREATE TABLE Titles (
--     title_id VARCHAR(50)   NOT NULL,
--     title VARCHAR(50)   NOT NULL,
--     CONSTRAINT pk_Titles PRIMARY KEY (
--         title_id
--      )
-- );

-- -- CREATE TABLE for Employee. Set PRIMARY KEY as emp_no.
-- CREATE TABLE Employee (
--     emp_no INT   NOT NULL,
--     emp_title_id VARCHAR   NOT NULL,
--     birth_date DATE   NOT NULL,
--     first_name VARCHAR   NOT NULL,
--     last_name VARCHAR   NOT NULL,
--     sex VARCHAR(1)   NOT NULL,
--     hire_date DATE   NOT NULL,
--     CONSTRAINT pk_Employee PRIMARY KEY (
--         emp_no
--      )
-- );

-- -- CREATE TABLE for Dept_emp.
-- CREATE TABLE Dept_emp (
--     emp_no INT   NOT NULL,
--     dept_no VARCHAR   NOT NULL
-- );

-- -- CREATE TABLE for Dept_manager.
-- CREATE TABLE Dept_manager (
--     dept_no VARCHAR   NOT NULL,
--     emp_no INT   NOT NULL
-- );

-- -- CREATE TABLE for Salaries.
-- CREATE TABLE Salaries (
--     emp_no INT   NOT NULL,
--     salary INT   NOT NULL
-- );

-- -- Using ALTER TABLE for Employee table, add FOREIGN KEY emp_title_id fro Titles table.
-- ALTER TABLE Employee ADD CONSTRAINT fk_Employee_emp_title_id FOREIGN KEY(emp_title_id)
-- REFERENCES Titles (title_id);

-- -- Using ALTER TABLE for Dept_emp table, add FOREIGN KEY emp_no from Employee table.
-- ALTER TABLE Dept_emp ADD CONSTRAINT fk_Dept_emp_emp_no FOREIGN KEY(emp_no)
-- REFERENCES Employee (emp_no);

-- -- Using ALTER TABLE for Dept_emp table, add FOREIGN KEY dept_no from Dept_departments table.
-- ALTER TABLE Dept_emp ADD CONSTRAINT fk_Dept_emp_dept_no FOREIGN KEY(dept_no)
-- REFERENCES Dept_departments (dept_no);

-- -- Using ALTER TABLE for Dept_manager table, add FOREIGN KEY dept from Dept_departments table.
-- ALTER TABLE Dept_manager ADD CONSTRAINT fk_Dept_manager_dept_no FOREIGN KEY(dept_no)
-- REFERENCES Dept_departments (dept_no);

-- -- Using ALTER TABLE for Dept_manager table, add FOREIGN KEY emp_no from Employee table.
-- ALTER TABLE Dept_manager ADD CONSTRAINT fk_Dept_manager_emp_no FOREIGN KEY(emp_no)
-- REFERENCES Employee (emp_no);

-- -- Using ALTER TABLE for Salaries table, add FOREIGN KEY emp_no from Employee table.
-- ALTER TABLE Salaries ADD CONSTRAINT fk_Salaries_emp_no FOREIGN KEY(emp_no)
-- REFERENCES Employee (emp_no);

-- Double check that import were sucessfull
SELECT * FROM dept_departments;
SELECT * FROM titles;
SELECT * FROM employee;
SELECT * FROM dept_emp;
SELECT * FROM dept_manager;
SELECT * FROM salaries;

-- List the following details of each employee: 
-- employee number, last name, firt name, sex, and salary.
	--SELECT columns to display from each table. 
	-- JOIN employee and salaries tables to join on emp_no to pull salary data
SELECT e.emp_no AS " Employee Number", 
		e.last_name AS "Last Name", 
		e.first_name AS " First Name", 
		e.sex AS "Gender", 
		s.salary AS "Salary"
FROM employee e
JOIN salaries s
ON e.emp_no = s.emp_no;

-- List first name, last name, and hire date for employees who were hired in 1986.
	-- SELECT columns to display FROM employee table 
	-- WHERE hire date is BETWEEN 1986-01-01 AND 1986-12-31 range to get the entire year.
SELECT first_name AS "First Name", 
		last_name AS " Last Name", 
		hire_date AS " Hire Date"
FROM employee
WHERE hire_date BETWEEN '1986-01-01' AND '1986-12-31';

-- List the manager of each department with the following information:
-- department number, department name, the manager's employee number, last name, first name.
	-- SELECT columns to display from each table
	-- FROM employee  
	-- JOIN dept_departments to dept_manager ON dept_no to link dept_name to dept_no
	-- JOIN dept_manager to employee to link emp_no to dept_no
SELECT dd.dept_no AS " Department Number", 
		dd.dept_name AS " Department", 
		dm.emp_no AS "Employee Number", 
		e.last_name As "Last Name", 
		e.first_name AS "First Name"
FROM dept_departments dd
JOIN dept_manager dm
ON dd.dept_no = dm.dept_no
	JOIN employee e
	ON dm.emp_no = e.emp_no;

-- List the department of each employee whose first name is 
-- "Hercules" and last name begins with "B"
	-- SELECT columns to display FROM employee table
	-- WHERE fist_name = 'Hercules' AND last_name LIKE 'B%' 
	-- Wildcard used after B to get last names that start with B
SELECT first_name AS "First Name", 
		last_name AS "Last Name", 
		sex AS " Gender"
FROM employee
WHERE first_name = 'Hercules' AND last_name LIKE 'B%';

-- List all employees in the Sales department, including their employee number, 
-- last name, first anme, and department name.
	-- SELECT columns to display
	-- JOIN employee and dept_emp ON emp_no to link emp_no to dept_no
	-- JOIN dept_deparment to dept_emp ON dept_no to link to dept_name 
	-- WHERE dept_name = 'Sales'
SELECT e.emp_no AS "Employee Number", 
		e.last_name AS " Last Name", 
		e.first_name AS " First Name", 
		dd.dept_name AS "Department"
FROM employee e
JOIN dept_emp de
ON e.emp_no = de.emp_no
	JOIN dept_departments dd
	ON de.dept_no = dd.dept_no
	WHERE dept_name = 'Sales';

-- List all employess in the Sales and Development departments, 
-- including their employee number, last name, first name, and department name.
	-- SELECT columns to display
	-- JOIN employee and dept_emp ON emp_no to link emp_no to dept_no
	-- JOIN dept_deparment to dept_emp ON dept_no to link to dept_name 
	-- WHERE dept_name = 'Sales' OR dept_name = 'Development'
SELECT e.emp_no AS "Employee Number", 
		e.last_name AS " Last Name", 
		e.first_name AS " First Name", 
		dd.dept_name AS "Department"
FROM employee e
JOIN dept_emp de
ON e.emp_no = de.emp_no
	JOIN dept_departments dd
	ON de.dept_no = dd.dept_no
	WHERE dept_name = 'Sales' OR dept_name = 'Developement';
	
-- In decending order, list frequency count of employee last name, i.e., 
-- how many employees share each last name.
	-- SELECT column to display  
	-- Use COUNT to get last_name totals. GROUP BY to get SUM of each last_name
	-- ORDER BY last_name in DESC order
	
SELECT last_name, COUNT(last_name) AS "Frequency"
FROM employee
GROUP BY last_name
ORDER BY last_name DESC;
	