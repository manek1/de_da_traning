CREATE TABLE dim_branch (
    branch_id INT PRIMARY KEY,
    branch_name VARCHAR(100),
    branch_type VARCHAR(50),
    br_opening_time VARCHAR(20),
    br_closing_time VARCHAR(20),
    br_holiday VARCHAR(50),
    location_id INT,
    email_id VARCHAR(100),
    br_contact_number BIGINT,
    opening_date DATE,
    stock_capacity INT,
    stock_availability INT,
    service_capacity INT,
    FOREIGN KEY (location_id) REFERENCES dim_location(location_id)
)

select * from dim_branch