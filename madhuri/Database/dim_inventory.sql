CREATE TABLE dim_inventory (
    inventory_id INT PRIMARY KEY,
    product_id INT,
    branch_id INT,
    stock_capacity INT,
    opening_stock INT,
    current_stock INT,
    closing_stock INT,
    stock_status VARCHAR(50),
    inventory_start_date DATE,
    inventory_end_date DATE,
    FOREIGN KEY (product_id) REFERENCES dim_product(product_id),
    FOREIGN KEY (branch_id) REFERENCES dim_branch(branch_id)
)

select * from dim_inventory