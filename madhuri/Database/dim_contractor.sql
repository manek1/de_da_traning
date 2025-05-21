CREATE TABLE dim_contractor (
    contractor_id INT PRIMARY KEY,
    contractor_name VARCHAR(100),
    contractor_type VARCHAR(50),
    contract_start_date DATE,
    contract_end_date DATE,
    cont_contact_no VARCHAR(20),
    location_id INT,
    performance_rating INT,
    FOREIGN KEY (location_id) REFERENCES dim_location(location_id)
)

select * from dim_contractor