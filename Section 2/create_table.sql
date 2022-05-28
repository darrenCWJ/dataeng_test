CREATE TABLE car(
    serial_number VARCHAR(50) PRIMARY KEY,
    model         VARCHAR(50),
    manufacturer  VARCHAR(50),
    weight_kg     DECIMAL(10,2),
    price         DECIMAL(10,2)
);

CREATE TABLE sales_person(
    sales_person_id   VARCHAR(50) PRIMARY KEY,
    sales_person_name VARCHAR(50)
);

CREATE TABLE transaction_record(
    sales_person_id         VARCHAR(50),
    car_serial_number       VARCHAR(50),
    customer_name           VARCHAR(50),
    customer_phone          NUMERIC(12),
    characteristic_car      VARCHAR(100),
    FOREIGN KEY (sales_person_id) REFERENCES sales_person(sales_person_id),
    FOREIGN KEY (car_serial_number) REFERENCES car(serial_number)
);

