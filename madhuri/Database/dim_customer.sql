CREATE TABLE dim_customer (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    customer_email_id VARCHAR(100),
    customer_DOB DATE,
    customer_contact_no VARCHAR(20),
    gender VARCHAR(10),
    location_id INT,
    registration_date DATE,
    customer_type VARCHAR(50),
    FOREIGN KEY (location_id) REFERENCES dim_location(location_id)
)

select * from dim_customer