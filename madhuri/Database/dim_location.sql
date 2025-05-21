CREATE TABLE dim_location (
    location_id INT PRIMARY KEY,
    house_no VARCHAR(50),
    building_apartment VARCHAR(100),
    locality_area VARCHAR(100),
    landmark VARCHAR(100),
    village_city_district VARCHAR(100),
    postal_code INT,
    state VARCHAR(100),
    country VARCHAR(100)
)

select * from dim_location