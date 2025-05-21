CREATE TABLE dim_employee (
    employee_id INT PRIMARY KEY,
    employee_first_name VARCHAR(50),
    employee_middle_name VARCHAR(50),
    employee_last_name VARCHAR(50),
    department VARCHAR(100),
    designation VARCHAR(100),
    location_id INT,
    branch_id INT,
    contact_number BIGINT,
    gender VARCHAR(10),
    aadhar_no BIGINT,
    DOB DATE,
    DOJ DATE,
    LWD DATE,
    salary INT,
    account_no BIGINT,
    FOREIGN KEY (location_id) REFERENCES dim_location(location_id), 
    FOREIGN KEY (branch_id) REFERENCES dim_branch(branch_id)
)

select * from dim_employee