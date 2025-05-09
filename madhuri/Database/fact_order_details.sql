CREATE TABLE fact_order_details (
    order_id INT PRIMARY KEY,
    date_key DATETIME,
    customer_id INT,
    employee_id INT,
    branch_id INT,
    order_status VARCHAR(50),
    order_quantity INT,
    order_amount DECIMAL(10,2),
    delivery_date DATE,
    FOREIGN KEY (date_key) REFERENCES dim_date(date_key),
    FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id),
    FOREIGN KEY (employee_id) REFERENCES dim_employee(employee_id),
    FOREIGN KEY (branch_id) REFERENCES dim_branch(branch_id)
);