CREATE TABLE dim_product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    product_type VARCHAR(50),
    launch_date DATE,
    brand VARCHAR(50),
    price DECIMAL(10,2),
    product_status VARCHAR(20)
)

select * from dim_product