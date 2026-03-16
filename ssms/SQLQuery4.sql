
-- when you have multiple special charecter then use translate and replce to prin the on strings
select 
REPLACE(translate('!@h#$e%l^l&o*','!@#$%^&*','********'),'*','')

-- round functions is use for round for the 0.5 values 
select round(38.5,0)

-- in this work like 2 means round with 2 decimal value
select round(35.65549,2)

-- in this -1 means is takine range 350-360 mid value 355 above this than 360 and below thant 350
select round(385,-3)

-- ciel is the alwayes take the upper value
select ceiling(38.9)

-- floor is taking always taking lower value
select floor(38.9)

-- conversions--
-- used to cinvert one data type to onothor data type
-- cast()
select cast(10.5 as int)

-- in convert the data type 
select convert(int ,15.8)

select format(5000,'c','en-ind')


use company;
select * from emp;
 
 -- ranke() functions for rank function data must be sorted
 -- find the rank on employee based on salary high salary
 select eid,ename,salary,
 rank() over (order by salary DESC) as ran
 from emp

 -- rank() is same when the salary i same is the count the rank as same number skip the next rank
 -- dence ranke() is used when we have same salary then not skip the dance rank alwayes in
 -- sequance next rank like rank()
  

use company;
select * from emp;

--- SELECT eid, ename, salary, department
-- Retrieves employee ID, name, salary, and department from the emp table.
-- DENSE_RANK() OVER (...) AS rnk
-- This is a window function. It assigns a ranking number to each row within a partition (group), based on the ordering criteria.
--  PARTITION BY department
-- Divides the dataset into groups by department. Each department is treated separately.
-- ORDER BY salary DESC
-- Within each department, employees are ranked by salary in descending order (highest salary first)

select eid,ename,salary,department,
DENSE_RANK()over(PARTITION BY department order by salary DESC) as rnk
from emp;


--  in this row_number based on salary it gives the salary wise row number
select eid,ename,salary,
ROW_NUMBER() over(order by salary DESC) as rno
from emp;

select eid,ename,salary,
ROW_NUMBER()over(order by eid ASC) as rno
from emp;

-- display top 3 highest paid employess
-- display top 3 max salary
--  display 5 max salary
-- display top 3 max salary in each department

-- asn is DENCE_rank() functions used

-- display first 5 row 
-- ans is row_number

-- LEG/LEAD function
-- LEG return pivios row value
-- LEAD return next value

select eid,ename,salary,
LAG(salary,1) over (order by eid ASC) prev_sal
from emp;-- LAG() retun privios row salary in this quary

select eid,ename,salary,
LEAD(salary,1) over (order by eid ASC) nex_sal
from emp;-- in this it;s give the nex salaary value when is not exist then nu

create table population(
year int,
population int);

INSERT INTO population(year, population)
VALUES 
    (2020, 130000),
    (2021, 135478),
    (2022, 145687),
    (2023, 1452357),
    (2024, 25646484),
    (2025, 35435456);

    -- displya year populaaton growth pct
SELECT 
    year,
    population,
    LAG(population, 1) OVER (ORDER BY year ASC) AS prev_population,
    ((population - LAG(population, 1) OVER (ORDER BY year ASC)) 
      / LAG(population, 1) OVER (ORDER BY year ASC)) * 100 AS pct
FROM population;

-- aggreigate function ->these functionas returns one value from the gropu of row

--max() is findin the maximum values
use company;

select max(salary) from emp;

-- min() finding the min value 
select min(salary) from emp;
select min(ename) from emp; -- in this arrangeing in alphbetical order

-- sum() it givve the total sum 
select sum(salary) from emp;

-- round() round the total salary thousands

select round(sum(salary),-3) from emp;

-- after rounding displaytoal salry with currency simbol

select format (round(sum(salary),-3),'c','en-in') 
from emp;

-- when adding the value than salaary + null=null,salary +isnull(salary,0)=salary
-- calculate total salary including cummistion
select sum(salary +isnull(comm,0)) as totalsalary from emp;

select * from emp;

-- avg() return average value
select avg(salary) from emp;
--round avg salary to highest integer
select CEILING(avg(salary)) from emp; -- ceiling is higest valus 

-- calculate avg salary paid to department wise
-- sum and avg can apply only numerical values and cannot apply the data and charecte
select avg(salary)
from emp
where department='it';

-- count()->return number of values present in columns it's count only not null values
select count(eid) from emp;
select * from emp;

-- count(*)-> return numbers of row in a table
select count(*) from emp;



-- add the column 
ALTER TABLE emp
ADD hire_date DATE,
    job_role VARCHAR(50);

UPDATE emp SET hire_date = '2020-01-15', job_role = 'Sales Executive' WHERE eid = 101;
UPDATE emp SET hire_date = '2019-03-10', job_role = 'HR Manager' WHERE eid = 102;
UPDATE emp SET hire_date = '2021-07-20', job_role = 'Software Engineer' WHERE eid = 103;
UPDATE emp SET hire_date = '2018-11-05', job_role = 'Accountant' WHERE eid = 104;
UPDATE emp SET hire_date = '2022-02-12', job_role = 'Data Scientist' WHERE eid = 105;
UPDATE emp SET hire_date = '2020-06-18', job_role = 'Sales Associate' WHERE eid = 106;
UPDATE emp SET hire_date = '2017-09-25', job_role = 'Operations Manager' WHERE eid = 107;
UPDATE emp SET hire_date = '2021-01-30', job_role = 'Marketing Analyst' WHERE eid = 108;
UPDATE emp SET hire_date = '2019-12-12', job_role = 'Financial Analyst' WHERE eid = 109;
UPDATE emp SET hire_date = '2020-08-22', job_role = 'Recruiter' WHERE eid = 110;
UPDATE emp SET hire_date = '2016-05-14', job_role = 'Project Manager' WHERE eid = 111;
UPDATE emp SET hire_date = '2021-04-09', job_role = 'Sales Coordinator' WHERE eid = 112;
UPDATE emp SET hire_date = '2018-07-01', job_role = 'Logistics Supervisor' WHERE eid = 113;
UPDATE emp SET hire_date = '2022-09-17', job_role = 'Content Strategist' WHERE eid = 114;
UPDATE emp SET hire_date = '2019-10-28', job_role = 'Senior Accountant' WHERE eid = 115;

select * from emp;

--> 6/3/26
--> group ny clause-> group by clause is used to grup rows based on one one or more columns
--> to calculate max,min,sum,avg,count for each group for ex to calculate 
--> dept wise total salary first group the row based on department and apply sum function on each group

select * from emp;
 
--> detaild data means all record are thire 
--> summerize data means client requrement use data 
--> group by clause convert detailed data into summarrized data by using group by
--> alwayes by analyse the summerise data
--> syntex   [select columns  
--          from emp
--          where conditin
--          gruop by cola,col2,
--          having conditon
--          order by col asc/desc]
--> Q1->display department wise total salary or total salary paid to each department
select department,sum(salary) as totalsal
from emp
group by department

--> display job wise salary 
select * from emp;
use company;
select * from emp;

select job_role,min(salary) as minsal,
                max(Salary) as maxsal,
                sum(salary) as tptalsal,
                AVG(salary) as avgsal,
                count(*) as cnt
                from emp
group by job_role;

--> display year wise no of employee
select datepart(yy,hire_date)as year,count(*)
from emp
group by DATEPART(yy,hire_date)

--> day wise no of employees
select datename(DW,hire_date)as year,count(*)
from emp
group by DATENAME(DW,hire_date)

--> month wise no of employees in the year 1981?
select datename(MM,hire_date)as year,count(*)
from emp
where DATEPART(yy,hire_date)=2016
group by DATENAME(MM,hire_date)

--> find the department more than 3 employees?
select department
from emp
where count(*)>3
group by department 
-->sql servver can't calculate dept wise count before the and it cna calculate only after group by
select department,count(*)
from emp
group by department
having count(*)>10;

--> where vs having most asking quisteen in interview
--> where -> select specific rows row,conditon applied before gruop by,use where clause if condition
--> not contain aggregate function
-->having-> select specific gruop,condition applied after gruop by,use having caluse if condtion 
--> contains aggregare functions

-- 7/3/26
--> display dept wise no of employees
use company;
select * from emp;

select department,count(*) as cnt
from emp
where department in (HR,IT)
group by department
order by department 
having count(*)>3

--> no of orders placed by each customers in last 3months
--> display only the customers placed more than 5 orders?

select * from population;

select cid,count(ordid) as no_of_orders
from orders
where orddt between dateadd(mm,-3,GETDATE()) and GETDATE()
gruop by cid
having count(ordid) > 5;

--> creating the customers DB and tables
CREATE DATABASE customers;
GO

USE customers;
GO

--> customers tables
-- Customers table
CREATE TABLE customers (
    cid INT PRIMARY KEY,
    cname VARCHAR(50),
    city VARCHAR(50)
);

-- Orders table
CREATE TABLE Orders (
    ordid INT PRIMARY KEY,
    cid INT FOREIGN KEY REFERENCES customers(cid),
    orddt DATE
);

--> inserting the records in tables
-- Insert Customers
INSERT INTO customers (cid, cname, city) VALUES
(1, 'Ravi Kumar', 'Hyderabad'),
(2, 'Sneha Reddy', 'Bangalore'),
(3, 'Arjun Mehta', 'Mumbai'),
(4, 'Priya Sharma', 'Delhi'),
(5, 'Vikram Singh', 'Chennai'),
(6, 'Anita Rao', 'Pune'),
(7, 'Rahul Verma', 'Kolkata'),
(8, 'Neha Gupta', 'Jaipur'),
(9, 'Kiran Das', 'Lucknow'),
(10, 'Manoj Iyer', 'Coimbatore');

-- Insert Orders (last 3 months)
INSERT INTO Orders (ordid, cid, orddt) VALUES
(101, 1, '2026-01-05'), (102, 1, '2026-01-15'), (103, 1, '2026-02-02'),
(104, 1, '2026-02-20'), (105, 1, '2026-03-01'), (106, 1, '2026-03-05'),

(107, 2, '2026-01-10'), (108, 2, '2026-02-14'), (109, 2, '2026-02-28'),
(110, 2, '2026-03-02'), (111, 2, '2026-03-04'), (112, 2, '2026-03-06'),

(113, 3, '2026-01-12'), (114, 3, '2026-02-01'), (115, 3, '2026-02-15'),
(116, 3, '2026-02-25'), (117, 3, '2026-03-03'),

(118, 4, '2026-01-08'), (119, 4, '2026-01-20'), (120, 4, '2026-02-10'),
(121, 4, '2026-02-22'), (122, 4, '2026-03-01'), (123, 4, '2026-03-05'),

(124, 5, '2026-01-05'), (125, 5, '2026-02-12'), (126, 5, '2026-02-18'),
(127, 5, '2026-03-02'), (128, 5, '2026-03-04'), (129, 5, '2026-03-06');

use customers;
select * from Orders;

--> calculatee dept wise and with in dept job wise total salary?
use company;
select * from emp;

select department,job_role,sum(salary) as totalsal
from emp
group by department,job_role
order by department ASC; --> show the salary in acending form

--> rollup -> is show the perticular group total also tells the grand total and is user difine

select department,job_role,sum(salary) as totalsal
from emp
group by rollup(department,job_role)
order by department asc,job_role;
--> cube displayes subtotal fro each group by columns fro example -> departno,job and is user define

select department,job_role,sum(salary) as totalsal
from emp
group by cube(department,job_role)
order by department asc,job_role asc;

--> display year wise and with in year quartile wise total sales and also display year wise subtotal?
use customers;
select * from Orders;

-- select datepart(yy,[orddt]) as year,
--    DATEPART(QQ,[orddt]) as qrt,
--    sum(sale) as totalsalaes
-- from Orders;
-- group by rollup(datepart(yy,[orddt]),
--               DATEPART(QQ,[orddt]))
-- order by year asc ,qrt asc

-- order of exicution 1.from 
--                    2.group by
--                    3.select
--                    4.order by
-- note-> columns alias cannot be used in group by clause beacause grouo by clause is exicuted before select
-- columns alias can be used in orders by clause because order by is exicuted after select
--> display state wiae and with in state gender wisr total no of person ?
--> display state wise and gender wise subtotal

-- {{selct state,count(*) as no_person
-- from persons
--group by cube(state ,gender)
--order by state asc}}

--> GROUPING SESTS:-> groupong sets clause allowd you to generate multile aggregate function within as sin
select department,job_role,sum(salary) as totalsal
from emp
group by grouping sets((department,job_role),(department),(job_role),())
order by department asc,job_role;

--> summery:
--1.importent of groupby
--2.writing quaries using group by
--3.where vs having
--4.roll up and cube
--5.grouping based on multiple columns
--6.grouping sets

--> (case statements):-
--> case statements are use to impliments if -else in SQL quaries
--> using case stamenents we can retuen values base on condition
--> case statement are 2 rypes
--1.simplae case
--2.searched case

--> simple case:- use simple case when conditon based on'='operator
-- case columns:- syntex(when value1 than return expr1,when value2 then return expr2)
use company;
select * from emp;

--> display ename job_role
select ename,
case job_role
when 'Sales' then 'exicutive'
when 'HR' then 'employee'
when 'IT' then 'senior emp'
else 'others'
end as job
from emp;

--> serched case:- use searched case when cinditon not based on '=' operators
-- searched case columns:- syntex(when conditon1 than return expr1,when cond2 then return expr2) else return expr end

-- display enmae salary salary range
use company;
select * from emp;

select ename,salary,
case
when salary >30000 then 'high salary'
when salary <30000 then 'low salary'
else 'avg salary'
end as salaryrange
from emp;

--display sno toal avg s=result?

--SELECT sno, 
  --               s1 + s2 + s3  as total,
    --             (s1+s2+s3)/3 as avg,
      --           CASE
        --         WHEN  s1>=35 AND s2>=35 AND s3>=35 THEN 'pass'
          --       ELSE  'fail'
            --     END as result
--  FROM student

--[joins]
-->  join is an operation  performed to display data from two or more table.				
--> To display data from two tables join those two tables
--> In DB  related data stored in multiple tables , To gather or to combine data stored in
-->multiple tables we need to join those tables.

-- types of joins

 --1 Inner join
 --        equi join
 --        non equi join
--         self join
-- 2 Outer join
  --        left join
    --      right join
      --    full join
 --2  Cross / Cartesian join
 
 -- Equi Join :-
  -----------------

-->  Equi join is performed between the tables sharing a common field
-->  Name of the common field need not to be same
-->  Common field datatype must be same
-->  Equi join is performed based on the common field with same datatype

  --   SELECT  columns
    -- FROM  tab1  INNER JOIN  tab2
    -- ON join condition--

  --  join condition :-
-- --------------------
         
--  =>  join condition specifies which record of 1st table joined with which record of 2nd table
-- =>  based on the given join condition sql server joins the records of two table

-- SELECT empno,ename,sal,dname,loc
--      FROM emp INNER JOIN dept
--      ON  emp.deptno = dept.deptno

	 
   -- NOTE :- 
--> in join queries declare table alias and prefix column names with table alias for two reasons


--       1  to avoid ambiguity
--       2  for faster execution

-- SELECT e.empno,e.ename,e.sal,
--                     d.deptno,d.dname,d.loc
--      FROM emp as e INNER JOIN dept as d
--       ON  e.deptno = d.deptno 

-->  display employee details with dept details working at NEW YORK loc ?

  --       SELECT e.ename,d.dname,d.loc
  --       FROM emp as e INNER JOIN dept as d
  --       ON e.deptno = d.deptno              /*  join condition */ 
  --       WHERE  d.loc = 'NEW YORK'   

 -- joining more than two tables :-
  -----------------------------------------

-->   if no of tables increases no of join conditions also increases 
-->  To join N tables N-1 join conditions required 

--   SELECT columns
--   FROM tab1 
--   INNER JOIN tab2
--   ON join cond1
--   INNER JOIN tab3
--  ON join cond2
--   INNER JOIN tab4
 -- ON join cond3
  ---------------------