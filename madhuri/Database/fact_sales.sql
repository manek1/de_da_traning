CREATE TABLE fact_sales (
    sales_id INT PRIMARY KEY,
    date_key datetime FOREIGN KEY REFERENCES dim_date(date_key),
    product_id INT FOREIGN KEY REFERENCES dim_product(product_id),
    customer_id INT FOREIGN KEY REFERENCES dim_customer(customer_id),
    contractor_id INT FOREIGN KEY REFERENCES dim_contractor(contractor_id),
    employee_id INT FOREIGN KEY REFERENCES dim_employee(employee_id),
    order_id INT FOREIGN KEY REFERENCES fact_order_details(order_id),
    branch_id INT FOREIGN KEY REFERENCES dim_branch(branch_id),
    quantity INT,
    amount DECIMAL(10, 2)
)
select * from fact_sales