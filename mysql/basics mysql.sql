-- creating the data base
create database nit;

-- show the all database in server
show databases;

-- use to impliment 
use nit;

-- in this useing the wildcard operators to find with start position and ending postion 
 
select * from student where name like 'a%';
select * from student;
select * from student where name like 'r%';
select * from student where name like '_a%';
select * from student where name like '%s_';

-- creating the table of employee
create table emp(
id int not null primary key,
salary int,
empcode int,
name varchar(30)
);

-- inserting the values in table
insert into emp value(12,20000,102,'aman'),(23,60000,104,'arup'),(78,30000,105,'max')
,(80,25000,103,'ram'),(34,90000,106,'sam');

-- selecting two table to performace to the quarryes 
select * from emp;
select * from student;

-- in this used ti the joins 

select * from student inner join emp on student.id=emp.id;
select * from student left join emp on student.id=emp.id;
select * from emp left join student on emp.id=student.id;
select * from emp right join student on emp.id=student.id;
select * from student cross join emp;

create database orders;
use orders; 
use customers;
select * from customers;
CREATE TABLE orders (
    OID INT PRIMARY KEY,
    DATE DATETIME,
    CUSTOMER_ID INT,
    AMOUNT DECIMAL(10,2)
);

INSERT INTO Orders (OID, DATE, CUSTOMER_ID, AMOUNT) VALUES
(102, '2009-10-08 00:00:00', 3, 3000),
(100, '2009-10-08 00:00:00', 3, 1500),
(101, '2009-11-20 00:00:00', 2, 1560),
(103, '2008-05-20 00:00:00', 4, 2060);


select * from orders;
SELECT ID, NAME, AGE, AMOUNT
FROM CUSTOMERS, ORDERS
WHERE CUSTOMERS.ID = ORDERS.CUSTOMER_ID;

-- in this useing the inner joins it's return the comman elements in the table
select id,name,amount,date -- INNERS JOINS IN USERED
from customers
inner join orders
on customers.id = orders.customer_id;

-- in this left join it return all the values of left and commons in right 
select id,age, name,date,amount -- LEFT JOIN ARE USED
 from customers
left join orders 
on customers.id= orders.customer_id;

-- in right join it return the all right element and common element on left
select id, name, amount
from customers
right join orders
on customers.id = orders.customer_id;

--  in mysql full join is not working
SELECT ID, NAME, AMOUNT, DATE
FROM CUSTOMERS
full JOIN ORDERS -- in sql is not working full joins
ON CUSTOMERS.ID = ORDERS.CUSTOMER_ID;

-- this is full join example it return all record in both table
SELECT ID, NAME, AMOUNT,date
FROM CUSTOMERS
LEFT JOIN ORDERS
ON CUSTOMERS.ID = ORDERS.CUSTOMER_ID
UNION ALL
SELECT ID, NAME, AMOUNT, DATE
FROM CUSTOMERS
RIGHT JOIN ORDERS
ON CUSTOMERS.ID = ORDERS.CUSTOMER_ID;

-- in this apply the condition 
SELECT A.ID,B.NAME,A.SALARY
FROM CUSTOMERS A, CUSTOMERS B
WHERE A.SALARY < B.SALARY;

SELECT ID, NAME, AMOUNT,date
FROM CUSTOMERS,ORDERS;

-- it also example og full outer join
SELECT ID,NAME, AMOUNT,DATE
FROM CUSTOMERS
LEFT JOIN  ORDERS
ON CUSTOMERS.ID = ORDERS.CUSTOMER_ID
UNION 
SELECT ID,NAME,DATE,AMOUNT
FROM CUSTOMERS
RIGHT JOIN ORDERS
ON CUSTOMERS.ID= ORDERS.CUSTOMER_ID;

SELECT ID,NAME,DATE,AMOUNT
FROM CUSTOMERS
LEFT JOIN ORDERS
ON CUSTOMERS.ID = ORDERS.CUSTOMER_ID
UNION
SELECT ID,NAME,AMOUNT,DATE
FROM CUSTOMERS
RIGHT JOIN ORDERS
ON CUSTOMERS.ID = ORDERS.CUSTOMER_ID;

-- useing inserting  Returns only the rows that appear in both result sets

SELECT ID,NAME,AMOUNT,date
FROM CUSTOMERS
LEFT JOIN ORDERS
ON CUSTOMERS.ID = ORDERS.CUSTOMER_ID
INTERSECT
SELECT ID,NAME,AMOUNT,DATE
FROM CUSTOMERS
RIGHT JOIN ORDERS
ON CUSTOMERS.ID = ORDERS.CUSTOMER_ID;

-- - The EXCEPT ensures you only get rows that appear in the first query but not in the second.

SELECT ID,NAME,AMOUNT,date
FROM CUSTOMERS
LEFT JOIN ORDERS
ON CUSTOMERS.ID = ORDERS.CUSTOMER_ID
EXCEPT
SELECT ID,NAME,DATE,AMOUNT
FROM CUSTOMERS
RIGHT JOIN ORDERS
ON CUSTOMERS.ID = ORDERS.CUSTOMER_ID;

-- in this findin the not null values
SELECT ID,NAME,AGE,ADDRESS,SALARY
FROM CUSTOMERS
WHERE SALARY IS NOT NULL;

SELECT ID, NAME,AGE,ADDRESS,SALARY
FROM CUSTOMERS
WHERE SALARY IS NULL;

SELECT C.ID,C.NAME,C.AGE,O.AMOUNT
FROM CUSTOMERS AS C, orders AS O
where C.ID = O.CUSTOMER_ID;

SELECT ID AS CUSTOMER_ID , NAME AS CUSTOMER_NAME
FROM CUSTOMERS
WHERE SALARY IS NOT NULL;

create index  kamlesh
on customers (name);

create index nilesh
on customers (id , name);

select * from customers;
alter table customers add product varchar(30);
alter table customers drop column product;
alter table customers modify column name varchar(30);
alter table customers modify column name varchar(30) not null;

alter table customers 
add constraint myuniqueconstraint unique(name,age);

alter table customers 
add constraint myuniqueconstraint check (age= 25);

alter table customers 
add constraint myprimarykey primary key(name,age);

alter table customers
drop constraint myuniqueconstraint ;

alter table customers
drop index myuniqueconstrain;

alter table customers
drop  myprimarykey;

alter table customers add sex char(1);
select * from customers;
alter table customers drop sex;

truncate table customers;
truncate table customers;
select * from customers;

create view customers_view as
select name,age
from customers;
select * from customers_view;
create view customers_view as 
select name,age
from customers
where age is not null 
with check option;
update customers_view
set age =35
where name='nilesh';
select * from customers;

delete from customers_view 
where age= 22;
drop view view_name;
drop view customers_view;

show databases;
