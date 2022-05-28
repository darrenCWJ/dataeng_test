## Table of Contents
-[About the Section](#about-the-section)
-[Setting Up Dockerfile Create Tables](#setting-up-dockerfile-create-tables)
-[Programs used](#programs-used)

<!-- ABOUT THE SECTION -->
## About The Section
Section 2: Databases
You are appointed by a car dealership to create their database infrastructure. There is only one store. In each business day, cars are being sold by a team of salespersons. Each transaction would contain information on the date and time of transaction, customer transacted with, and the car that was sold.

The following are known:

Each car can only be sold by one salesperson.
There are multiple manufacturers’ cars sold.
Each car has the following characteristics:
Manufacturer
Model name
Serial number
Weight
Price
Each sale transaction contains the following information:

Customer Name
Customer Phone
Salesperson
Characteristics of car sold
Set up a PostgreSQL database using the base docker image here given the above. We expect at least a Dockerfile which will stand up your database with the DDL statements to create the necessary tables. Produce entity-relationship diagrams as necessary to illustrate your design.

Your team also needs you to query some information from the database that you have designed. You are tasked to write a sql statement for each of the following task:

I want to know the list of our customers and their spending.

I want to find out the top 3 car manufacturers that customers bought by sales (quantity) and the sales number for it in the current month.

<!-- Setting Up Dockerfile -->
## Setting Up Dockerfile Create Tables
Since im using a windows laptop, I downloaded docker desktop which allows me to easily connect to my [Docker Website Repo](https://hub.docker.com/repository/docker/newbie4000/dataeng_test) where i can push my codes
up to test if its working. When setting up the dockerfile, i select the version of postGres that is stable to use as my base. Following which i use an SQL command to create the tables for the data.
After which looking at the container tab, it will show the creation of the database and whether there's any error that i may encounter from it.

![Alt text](https://github.com/darrenCWJ/dataeng_test/blob/master/Section%202/Section%202_%20ERD.png)
Above is the schema that i used for the database. As 1 salesperson can sell many different cars, and each sold car will generate a transaction record, there will be a 1 to many connection from Salesperson to Transaction Records.
Since each car can only be sold once, each car will have a 1 to 1 link to the transaction records. 

<!-- Programs used -->
## Programs used
Programs use to create the schema is from (lucid chart)[https://www.lucidchart.com/pages/]

Programs use to create docker and test is from (docker)[https://www.docker.com/products/personal/] 
