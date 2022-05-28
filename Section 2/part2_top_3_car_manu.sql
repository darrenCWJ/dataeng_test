SELECT *
FROM
(SELECT C.manufacturer, COUNT(DISTINCT C.car_serial_number) AS total quantity,
SUM(C.price) AS total sales,
MONTH(R.transaction_date) AS month,
YEAR(R.transaction_date) AS year
FROM transaction_record AS R
INNER JOIN car AS C
ON R.car_serial_number=C.serial_number
GROUP BY C.manufacturer, month,year)
WHERE month(transaction_date)= month (getdate())
AND year(transaction_date)= year(getdate())
ORDER BY total quantity DESC
LIMIT 3;