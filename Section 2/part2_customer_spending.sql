SELECT R.Customer_name, sum(C.price) AS Total Spending
FROM transaction_record AS R
INNER JOIN car AS C
ON R.car_serial_number=C.serial_number
GROUP BY R.customer_name;