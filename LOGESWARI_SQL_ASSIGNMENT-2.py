#!/usr/bin/env python
# coding: utf-8

# # SQL_ASSIGNMENT-2
# 

# ## Name : Logeswari
CREATE SCHEMA ` logeswaridb1’;
CREATE TABLE `logeswaridb1`.`customer` (
    'customer' VARCHAR NOT NULL);
SELECT * FROM logeswaridb1.`customer_name`;
INSERT INTO `logeswaridb1`.`customer_name` VALUES ('Abhinash'),('Vipin'),('Mahesh'),('Bijoy'),('Bhabani'),('Ashutosh')    CREATE TABLE `logeswaridb1`.'voucher' (Voucher_Id varchar(255) UNIQUE);
INSERT INTO `logeswaridb1`.'voucher_Id' VALUES('ABXFH'),('SDFGH'),('ERTYY'),('PPLKM')with cte as(select *,row_number() over(order by Customer_name) rr from Customers1),
cte2 as(select *,row_number() over(order by voucher_Id) rr from Voucher)
    
select Customer_name Customer_Key,Voucher_Id Gift_Voucher_Key
from cte c1
join cte2 c2 on c1.rr=c2.rr
