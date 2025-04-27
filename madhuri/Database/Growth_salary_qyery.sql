create table employee (
    name varchar(20),
    department varchar(20),
    salary int
);

insert into employee (name, department, salary) VALUES
('John', 'HR', 60000),
('Jane', 'HR', 65000),
('Jake', 'HR', 60000),
('Alice', 'IT', 80000),
('Bob', 'IT', 90000),
('Charlie', 'IT', 85000);

select * from employee

WITH ranked_employees AS (
    SELECT
        name,
        department,
        salary,
        ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary) AS rn,
        LAG(salary, 1, NULL) OVER (PARTITION BY department ORDER BY salary) AS prev_salary
    FROM employee
),
growth_classification AS (
    SELECT
        name,
        department,
        salary,
        CASE
            WHEN prev_salary IS NULL THEN 'No Growth'
            WHEN salary > prev_salary THEN 'High Growth'
            WHEN salary < prev_salary THEN 'Low Growth'
            ELSE 'No Growth'
        END AS growth_status
    FROM ranked_employees
)
SELECT * FROM growth_classification ORDER BY department, salary;