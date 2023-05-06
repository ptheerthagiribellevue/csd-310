/*
Group: Group3
Members: Loren Alwarez-Mejias & Praveen Theerthagiri 
Assignment: Wilson Financial case study - Assignment 9, 10, 11
Date: 05/05/2023

SQL scripts for WilsonFinancialDB. 
- Sql statements to create tables for 
      clients, assets, transaction, departments, employees, compliance regulations and compliance managers.
- Sql statements for populating sample data in these tables. 

*/ 

Use WilsonFinancialDB;

DROP TABLE IF EXISTS ComplianceManager;
DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS Department;
DROP TABLE IF EXISTS ComplianceRegulation;
DROP TABLE IF EXISTS Transactions;
DROP TABLE IF EXISTS Assets;
DROP TABLE IF EXISTS Clients;

-- COMMENT 1.  Create the Clients table 
CREATE TABLE Clients (
    client_id INT PRIMARY KEY,
    client_first_name VARCHAR(50) NOT NULL,
    client_last_name VARCHAR(50) NOT NULL,
    client_email VARCHAR(100) NOT NULL,
    client_phone VARCHAR(20),
    Address VARCHAR(200), 
    account_balance DECIMAL(10,2),
    account_open_date DATE
    );

-- COMMENT 2. Create Assets table  
CREATE TABLE Assets (
    asset_id INT PRIMARY KEY,
    asset_type VARCHAR(50) NOT NULL,
    asset_value DECIMAL(10, 2) NOT NULL,
    purchase_date DATE NOT NULL,
    client_id INT NOT NULL,
    FOREIGN KEY (client_id) REFERENCES Clients (client_id)
    );

-- COMMENT 3. Create Transactions table  
CREATE TABLE Transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_type VARCHAR(50) NOT NULL,
    transaction_date DATE,
    transaction_amount DECIMAL(10, 2) NOT NULL,
    Description VARCHAR(255),
    asset_id INT NOT NULL,
    FOREIGN KEY (asset_id) REFERENCES Assets (asset_id)
    );

-- COMMENT 4. Create Department table
CREATE TABLE Department (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    department_name VARCHAR(255) NOT NULL
    );

-- COMMENT 5. Create the Employees table
CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    employee_first_name VARCHAR(50) NOT NULL,
    employee_last_name VARCHAR(50) NOT NULL,
    employee_email VARCHAR(100) NOT NULL,
    employee_phone VARCHAR(20),
    Title VARCHAR(100),
    employee_hire_date DATE NOT NULL,
    department_id INT NOT NULL,
    FOREIGN KEY (department_id) REFERENCES Department (department_id)
    );

-- COMMENT 6. Create the ComplianceRegulation table
CREATE TABLE ComplianceRegulation (
    regulation_id INT(11) NOT NULL AUTO_INCREMENT,
    regulation_name VARCHAR(50) NOT NULL,
    regulation_description TEXT,
    client_id INT(11) NOT NULL,
    PRIMARY KEY (regulation_id),
    FOREIGN KEY (client_id) REFERENCES Clients (client_id)
    );

-- COMMENT 7. Create table ComplianceManager
CREATE TABLE ComplianceManager (
    manager_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT(11) NOT NULL,
    employee_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    FOREIGN KEY (client_id) REFERENCES Clients (client_id),
    FOREIGN KEY (employee_id) REFERENCES Employees (employee_id)
    );


--  COMMENT Sample data creation

-- COMMENT 1. Inserting sample data in Clients table
INSERT INTO Clients (client_id, client_first_name, client_last_name, client_email, client_phone, Address, account_balance, account_open_date) VALUES
('1', 'John', 'Smith', 'johnsmith@example.com', '555-1234', '123 Main St', '25000.00', '2022-12-01'),
('2', 'Jane', 'Garcia', 'janegarcia@example.com', '555-5678', '456 Maple Ave', '250000.00', '2023-01-01'),
('3', 'Bob', 'Smith', 'bobsmith@example.com', '555-9012', '789 Oak St', '5000.00', '2023-01-15'),
('4', 'Alice', 'Jones', 'alicejones@example.com', NULL, '456 Pine St', '10000.00', '2022-11-15'),
('5', 'Charlie', 'Brown', 'charliebrown@example.com', '555-3456', '789 Elm St', '50000.00', '2023-02-15'),
('6', 'Lucy', 'Smith', 'lucysmith@example.com', '555-7890', '123 Oak Ave', '100000.00', '2023-03-15'),
('7', 'David', 'Lee', 'davidlee@example.com', '555-2345', '456 Cherry St', '1000.00', '2023-03-25'),
('8', 'Emily', 'Davis', 'emilydavis@example.com', NULL, '789 Birch Rd', '125000.00', '2022-10-25');


-- COMMENT 2. Inserting sample data in Assets table
INSERT INTO Assets (asset_id, asset_type, asset_value, purchase_date, client_id) VALUES
    (1, 'Stocks', 10000.00, '2021-01-01', 1),
    (2, 'Bonds', 5000.00, '2021-02-15', 1),
    (3, 'Real Estate', 150000.00, '2020-05-01', 2),
    (4, 'Stocks', 20000.00, '2020-10-15', 3),
    (5, 'Bonds', 10000.00, '2021-03-01', 4),
    (6, 'Real Estate', 250000.00, '2019-12-01', 4),
    (7, 'Stocks', 5000.00, '2021-04-15', 5),
    (8, 'Bonds', 15000.00, '2020-07-01', 5),
    (9, 'Stocks', 10000.00, '2021-04-01', 6),
    (10, 'Bonds', 5000.00, '2021-05-15', 6),
    (11, 'Real Estate', 150000.00, '2021-06-01', 6);


-- COMMENT 3. Inserting sample data in Transactions table
INSERT INTO Transactions (transaction_id, transaction_type, transaction_date, transaction_amount, description, asset_id) VALUES
('1', 'Purchase', '2021-01-15', '5000.00', 'Bought 100 shares of AAPL', '1'),
('2', 'Purchase', '2021-02-15', '5000.00', 'Purchase 200 shares of XYZ Corp', '1'),
('3', 'Purchase', '2021-03-16', '5000.00', 'Purchase of XYZ Bond', '1'),
('4', 'Sale', '2023-05-01', '10000.00', 'Sold 50 shares of AAPL', '2'),
('5', 'Purchase', '2023-05-01', '75000.00', 'Bought 50 shares of AMZN', '3'),
('6', 'Dividend', '2023-05-01', '1000.00', 'Received dividend for MSFT', '4'),
('7', 'Sale', '2023-05-02', '3000.00', 'Sold 20 shares of MSFT', '5'),
('8', 'Purchase', '2023-05-02', '150000.00', 'Bought 200 shares of TSLA', '6'),
('9', 'Purchase', '2023-05-02', '100000.00', 'Bought 500 shares of GOOGL', '7'),
('10', 'Sale', '2023-05-03', '50000.00', 'Sold 100 shares of TSLA', '8'),
('11', 'Purchase', '2023-04-15', '5000.00', 'Bought 100 shares of AAPL', '1'),
('12', 'Purchase', '2023-04-15', '5000.00', 'Purchase 200 shares of XYZ Corp', '1'),
('13', 'Purchase', '2023-04-16', '5000.00', 'Purchase of XYZ Bond', '1'),
('14', 'Sale', '2023-05-01', '10000.00', 'Sold 50 shares of AAPL', '1'),
('15', 'Purchase', '2023-05-02', '75000.00', 'Bought 50 shares of AMZN', '1'),
('16', 'Dividend', '2023-05-03', '1000.00', 'Received dividend for MSFT', '1'),
('17', 'Sale', '2023-05-02', '3000.00', 'Sold 20 shares of MSFT', '1'),
('18', 'Purchase', '2023-05-02', '150000.00', 'Bought 200 shares of TSLA', '1'),
('19', 'Purchase', '2023-05-02', '100000.00', 'Bought 500 shares of GOOGL', '1'),
('20', 'Sale', '2023-05-03', '50000.00', 'Sold 100 shares of TSLA', '1'),
('21', 'Purchase', '2023-05-15', '5000.00', 'Bought 100 shares of AAPL', '1'),
('22', 'Purchase', '2023-05-17', '5000.00', 'Bought 100 shares of AAPL', '1'),
('23', 'Purchase', '2023-05-20', '5000.00', 'Purchase of XYZ Bond', '1'),
('24', 'Purchase', '2023-04-15', '5000.00', 'Bought 100 shares of AAPL', '2'),
('25', 'Purchase', '2023-04-15', '5000.00', 'Purchase 200 shares of XYZ Corp', '2'),
('26', 'Purchase', '2023-04-16', '5000.00', 'Purchase of XYZ Bond', '2'),
('27', 'Sale', '2023-04-01', '10000.00', 'Sold 50 shares of AAPL', '2'),
('28', 'Purchase', '2023-04-02', '75000.00', 'Bought 50 shares of AMZN', '2'),
('29', 'Dividend', '2023-04-03', '1000.00', 'Received dividend for MSFT', '2'),
('30', 'Sale', '2023-04-02', '3000.00', 'Sold 20 shares of MSFT', '2'),
('31', 'Purchase', '2023-04-02', '150000.00', 'Bought 200 shares of TSLA', '2'),
('32', 'Purchase', '2023-04-02', '100000.00', 'Bought 500 shares of GOOGL', '2'),
('33', 'Sale', '2023-04-03', '50000.00', 'Sold 100 shares of TSLA', '2'),
('34', 'Purchase', '2023-04-15', '5000.00', 'Bought 100 shares of AAPL', '2'),
('35', 'Purchase', '2023-04-17', '5000.00', 'Bought 100 shares of AAPL', '2'),
('36', 'Purchase', '2023-04-20', '5000.00', 'Purchase of XYZ Bond', '2'),
('37', 'Purchase', '2023-04-15', '5000.00', 'Bought 100 shares of AAPL', '3'),
('38', 'Purchase', '2023-04-15', '5000.00', 'Purchase 200 shares of XYZ Corp', '3'),
('39', 'Purchase', '2023-04-16', '5000.00', 'Purchase of XYZ Bond', '3'),
('40', 'Sale', '2023-04-01', '10000.00', 'Sold 50 shares of AAPL', '3'),
('41', 'Purchase', '2023-04-02', '75000.00', 'Bought 50 shares of AMZN', '3'),
('42', 'Dividend', '2023-04-03', '1000.00', 'Received dividend for MSFT', '3'),
('43', 'Sale', '2023-04-02', '3000.00', 'Sold 20 shares of MSFT', '3'),
('44', 'Purchase', '2023-04-02', '150000.00', 'Bought 200 shares of TSLA', '3'),
('45', 'Purchase', '2023-04-02', '100000.00', 'Bought 500 shares of GOOGL', '3'),
('46', 'Sale', '2023-04-03', '50000.00', 'Sold 100 shares of TSLA', '3'),
('47', 'Purchase', '2023-04-15', '5000.00', 'Bought 100 shares of AAPL', '3'),
('48', 'Purchase', '2023-04-17', '5000.00', 'Bought 100 shares of AAPL', '3'),
('49', 'Purchase', '2023-04-20', '5000.00', 'Purchase of XYZ Bond', '3'),
('50', 'Purchase', '2023-03-15', '5000.00', 'Bought 100 shares of AAPL', '5'),
('51', 'Purchase', '2023-03-15', '5000.00', 'Purchase 200 shares of XYZ Corp', '5'),
('52', 'Purchase', '2023-03-16', '5000.00', 'Purchase of XYZ Bond', '5'),
('53', 'Sale', '2023-03-01', '10000.00', 'Sold 50 shares of AAPL', '5'),
('54', 'Purchase', '2023-03-02', '75000.00', 'Bought 50 shares of AMZN', '5'),
('55', 'Dividend', '2023-03-03', '1000.00', 'Received dividend for MSFT', '5'),
('56', 'Sale', '2023-03-02', '3000.00', 'Sold 20 shares of MSFT', '5'),
('57', 'Purchase', '2023-03-02', '150000.00', 'Bought 200 shares of TSLA', '5'),
('58', 'Purchase', '2023-03-02', '100000.00', 'Bought 500 shares of GOOGL', '5'),
('59', 'Sale', '2023-03-03', '50000.00', 'Sold 100 shares of TSLA', '5'),
('60', 'Purchase', '2023-03-15', '5000.00', 'Bought 100 shares of AAPL', '5'),
('61', 'Purchase', '2023-03-17', '5000.00', 'Bought 100 shares of AAPL', '5'),
('62', 'Purchase', '2023-03-20', '5000.00', 'Purchase of XYZ Bond', '5');
  

-- COMMENT 4. Inserting sample data in Department table
INSERT INTO Department (department_name) VALUES 
('Finance'),
('Compliance'),
('Marketing'),
('Human Resources');

-- COMMENT 5. Inserting sample data in Employees table
INSERT INTO Employees (employee_id, employee_first_name, employee_last_name, employee_email, employee_phone, Title, employee_hire_date, department_id)
VALUES 
(1001, 'June', 'Santos', 'junesantos@email.com', '123-456-7890', 'Financial Advisor', '2020-01-01', 1),
(1002, 'Jane', 'Doe', 'janedoe@email.com', '123-456-7891', 'Compliance Manager', '2020-02-01', 2),
(1003, 'Phoenix', 'TwoStar', 'phoenixtwostar@email.com', '123-456-7892', 'Office Administrator', '2020-03-01', 3),
(1004, 'Sarah', 'Johnson', 'sarahjohnson@email.com', '123-456-7893', 'Financial Advisor', '2020-04-01', 1),
(1005, 'Mike', 'Brown', 'mikebrown@email.com', '123-456-7894', 'Financial Analyst', '2020-05-01', 4),
(1006, 'Jessica', 'Lee', 'jessicalee@email.com', '123-456-7895', 'Marketing Manager', '2020-06-01', 1),
(1007, 'William', 'Nguyen', 'williamnguyen@email.com', '123-456-7896', 'Compliance Officer', '2020-07-01', 2),
(1008, 'Emily', 'Wang', 'emilywang@email.com', '123-456-7897', 'Financial Advisor', '2020-08-01', 1);

-- COMMENT 6. Inserting sample data in ComplianceRegulation table
INSERT INTO ComplianceRegulation (regulation_name, regulation_description, client_id)
VALUES ('SEC Rule 17a-4', 'Requires firms to retain records for specified periods', 1),
       ('FINRA Rule 2111', 'Requires firms to make recommendations in clients’ best interests', 2),
       ('SEC Rule 15c3-3', 'Requires broker-dealers to segregate customers’ securities and cash from their own', 3),
       ('FINRA Rule 4512', 'Requires firms to make and preserve certain records regarding customer accounts', 4),
       ('SEC Rule 206(4)-7', 'Requires firms to implement policies and procedures to prevent and detect violations of federal securities laws', 5),
       ('FINRA Rule 2121', 'Requires firms to ensure that the prices charged to customers are fair', 6),
       ('SEC Rule 17a-5', 'Requires firms to maintain certain financial and operational records', 7),
       ('FINRA Rule 4530', 'Requires firms to report certain events to FINRA', 8);


-- COMMENT 7. Inserting sample data in ComplianceManager table
INSERT INTO ComplianceManager (client_id, employee_id, start_date, end_date)
VALUES
  (1, 1001, '2022-01-01', '2022-06-30'),
  (2, 1002, '2022-03-01', '2022-08-31'),
  (3, 1002, '2022-02-01', '2022-07-31'),
  (4, 1004, '2022-04-01', '2022-09-30'),
  (5, 1005, '2022-05-01', '2022-10-31'),
  (6, 1002, '2022-06-01', '2022-11-30'),
  (7, 1007, '2022-07-01', '2022-12-31'),
  (8, 1002, '2022-08-01', '2023-01-31');
