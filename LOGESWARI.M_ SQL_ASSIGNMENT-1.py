#!/usr/bin/env python
# coding: utf-8
CREATE SCHEMA ` logeswaridb1’;CREATE TABLE `logeswaridb1`.`purchase history` (
  `Bills_Id` INT NOT NULL,
  `Customer` INT NOT NULL,
  `Product_Id` INT NOT NULL,
  `Sale_Qty` INT NOT NULL,
  `Bill Amount` FLOAT NOT NULL,
  `Bill_Date` DATE NOT NULL,
  PRIMARY KEY (`Bills_Id`));
SELECT * FROM logeswaridb1.`purchase history`;
INSERT INTO `logeswaridb1`.`purchase history` (`Bills_Id`, `Customer`, `Product_Id`, `Sale_Qty`, `Bill Amount`, `Bill_Date`) VALUES ('78807159', '44', '100', '1', '16000', '2020-02-22');
INSERT INTO `logeswaridb1`.`purchase history` (`Bills_Id`, `Customer`, `Product_Id`, `Sale_Qty`, `Bill Amount`, `Bill_Date`) VALUES ('82390697', '44', '100', '2', '5200', '2020-02-23');
INSERT INTO `logeswaridb1`.`purchase history` (`Bills_Id`, `Customer`, `Product_Id`, `Sale_Qty`, `Bill Amount`, `Bill_Date`) VALUES ('94479024', '44', '100', '1', '4200', '2020-02-27');
INSERT INTO `logeswaridb1`.`purchase history` (`Bills_Id`, `Customer`, `Product_Id`, `Sale_Qty`, `Bill Amount`, `Bill_Date`) VALUES ('94549714', '44', '100', '1', '21900', '2020-02-27');
INSERT INTO `logeswaridb1`.`purchase history` (`Bills_Id`, `Customer`, `Product_Id`, `Sale_Qty`, `Bill Amount`, `Bill_Date`) VALUES ('95521191', '44', '200', '1', '20000', '2020-02-27');
INSERT INTO `logeswaridb1`.`purchase history` (`Bills_Id`, `Customer`, `Product_Id`, `Sale_Qty`, `Bill Amount`, `Bill_Date`) VALUES ('142109733', '44', '200', '1', '8400', '2019-11-11');
INSERT INTO `logeswaridb1`.`purchase history` (`Bills_Id`, `Customer`, `Product_Id`, `Sale_Qty`, `Bill Amount`, `Bill_Date`) VALUES ('158391727', '44', '300', '1', '24100.01', '2019-11-16');
INSERT INTO `logeswaridb1`.`purchase history` (`Bills_Id`, `Customer`, `Product_Id`, `Sale_Qty`, `Bill Amount`, `Bill_Date`) VALUES ('168354993', '44', '300', '1', '24100.01', '2019-11-19');
INSERT INTO `logeswaridb1`.`purchase history` (`Bills_Id`, `Customer`, `Product_Id`, `Sale_Qty`, `Bill Amount`, `Bill_Date`) VALUES ('193504854', '44', '300', '1', '7600', '2019-11-26');
INSERT INTO `logeswaridb1`.`purchase history` (`Bills_Id`, `Customer`, `Product_Id`, `Sale_Qty`, `Bill Amount`, `Bill_Date`) VALUES ('195567022', '44', '300', '1', '2500', '2019-11-26');
INSERT INTO `logeswaridb1`.`purchase history` (`Bills_Id`, `Customer`, `Product_Id`, `Sale_Qty`, `Bill Amount`, `Bill_Date`) VALUES ('216619949', '44', '301', '1', '16000', '2019-12-01');
INSERT INTO `logeswaridb1`.`purchase history` (`Bills_Id`, `Customer`, `Product_Id`, `Sale_Qty`, `Bill Amount`, `Bill_Date`) VALUES ('228647858', '44', '401', '1', '28500.01', '2019-12-04');
INSERT INTO `logeswaridb1`.`purchase history` (`Bills_Id`, `Customer`, `Product_Id`, `Sale_Qty`, `Bill Amount`, `Bill_Date`) VALUES ('244924788', '66', '402', '1', '18200', '2019-12-08');
INSERT INTO `logeswaridb1`.`purchase history` (`Bills_Id`, `Customer`, `Product_Id`, `Sale_Qty`, `Bill Amount`, `Bill_Date`) VALUES ('244938525', '66', '403', '1', '16000', '2019-12-08');
INSERT INTO `logeswaridb1`.`purchase history` (`Bills_Id`, `Customer`, `Product_Id`, `Sale_Qty`, `Bill Amount`, `Bill_Date`) VALUES ('244947344', '66', '404', '2', '12600', '2019-12-08');
INSERT INTO `logeswaridb1`.`purchase history` (`Bills_Id`, `Customer`, `Product_Id`, `Sale_Qty`, `Bill Amount`, `Bill_Date`) VALUES ('245391938', '66', '405', '1', '4200', '2019-12-082019-12-08');
INSERT INTO `logeswaridb1`.`purchase history` (`Bills_Id`, `Customer`, `Product_Id`, `Sale_Qty`, `Bill Amount`, `Bill_Date`) VALUES ('245896327', '66', '406', '1', '12500', '2019-12-08');
INSERT INTO `logeswaridb1`.`purchase history` (`Bills_Id`, `Customer`, `Product_Id`, `Sale_Qty`, `Bill Amount`, `Bill_Date`) VALUES ('270582683', '66', '407', '1', '5900', '2019-12-16');
INSERT INTO `logeswaridb1`.`purchase history` (`Bills_Id`, `Customer`, `Product_Id`, `Sale_Qty`, `Bill Amount`, `Bill_Date`) VALUES ('271089616', '66', '405', '1', '22500', '2019-12-16');
INSERT INTO `logeswaridb1`.`purchase history` (`Bills_Id`, `Customer`, `Product_Id`, `Sale_Qty`, `Bill Amount`, `Bill_Date`) VALUES ('393252504', '66', '301', '1', '26100', '2020-01-19');
INSERT INTO `logeswaridb1`.`purchase history` (`Bills_Id`, `Customer`, `Product_Id`, `Sale_Qty`, `Bill Amount`, `Bill_Date`) VALUES ('395961027', '66', '401', '1', '12900', '2020-01-19');
INSERT INTO `logeswaridb1`.`purchase history` (`Bills_Id`, `Customer`, `Product_Id`, `Sale_Qty`, `Bill Amount`, `Bill_Date`) VALUES ('407474852', '77', '402', '1', '4900', '2020-01-23');




# ![Screenshot%20%2843%29.png](attachment:Screenshot%20%2843%29.png)
CREATE TABLE `logeswaridb1`.`product catalogue` (
  `Product_Id` INT NOT NULL,
  `Dep_Id` INT NOT NULL,
  `Cat_Id` INT NOT NULL,
  );

INSERT INTO `logeswaridb1`.`product catalogue` (`Product_Id`, `Dep_Id`, `Cat_Id`) VALUES ('100', '100', '1');
INSERT INTO `logeswaridb1`.`product catalogue` (`Product_Id`, `Dep_Id`, `Cat_Id`) VALUES ('100', '100', '1');
INSERT INTO `logeswaridb1`.`product catalogue` (`Product_Id`, `Dep_Id`, `Cat_Id`) VALUES ('100', '100', '1');
INSERT INTO `logeswaridb1`.`product catalogue` (`Product_Id`, `Dep_Id`, `Cat_Id`) VALUES ('100', '100', '1');
INSERT INTO `logeswaridb1`.`product catalogue` (`Product_Id`, `Dep_Id`, `Cat_Id`) VALUES ('200', '200', '1');
INSERT INTO `logeswaridb1`.`product catalogue` (`Product_Id`, `Dep_Id`, `Cat_Id`) VALUES ('200', '200', '1');
INSERT INTO `logeswaridb1`.`product catalogue` (`Product_Id`, `Dep_Id`, `Cat_Id`) VALUES ('300', '300', '2');
INSERT INTO `logeswaridb1`.`product catalogue` (`Product_Id`, `Dep_Id`, `Cat_Id`) VALUES ('300', '300', '2');
INSERT INTO `logeswaridb1`.`product catalogue` (`Product_Id`, `Dep_Id`, `Cat_Id`) VALUES ('300', '300', '2');
INSERT INTO `logeswaridb1`.`product catalogue` (`Product_Id`, `Dep_Id`, `Cat_Id`) VALUES ('301', '301', '2');
INSERT INTO `logeswaridb1`.`product catalogue` (`Product_Id`, `Dep_Id`, `Cat_Id`) VALUES ('401', '401', '3');
INSERT INTO `logeswaridb1`.`product catalogue` (`Product_Id`, `Dep_Id`, `Cat_Id`) VALUES ('403', '403', '3');
INSERT INTO `logeswaridb1`.`product catalogue` (`Product_Id`, `Dep_Id`, `Cat_Id`) VALUES ('404', '404', '3');

# ![Screenshot%20%2844%29.png](attachment:Screenshot%20%2844%29.png)
SELECT Bills_Id,Customer,Product_Id,Sale_Qty,Bill_Amount,Bill_Date
FROM `logeswaridb1`.`purchase history` 
ORDER BY Bill_Date desc;