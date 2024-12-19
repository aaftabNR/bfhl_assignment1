CREATE Database bhfl;
use bhfl;

CREATE TABLE Accounts (
    AccountId VARCHAR(18) PRIMARY KEY,
    Name VARCHAR(255),
    Age INT,
    City VARCHAR(255),
    State VARCHAR(255),
    Pincode VARCHAR(10)
);

CREATE TABLE Policies (
    HAN VARCHAR(255) PRIMARY KEY,
    PolicyName VARCHAR(255)
);

CREATE TABLE Claims (
    Id INT PRIMARY KEY AUTO_INCREMENT,
    CreatedDate DATE,
    CaseNumber VARCHAR(255),
    HAN VARCHAR(255),
    BillAmount DECIMAL(10, 2),
    Status VARCHAR(50),
    AccountId VARCHAR(18)
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/accounts_cleaned.csv'
INTO TABLE Accounts
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(AccountId, Name, Age, City, State, Pincode);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/claims_cleaned_with_fixed_dates.csv'
INTO TABLE Claims
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Id, CreatedDate, CaseNumber, HAN, BillAmount, Status, AccountId);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Policies.csv'
INTO TABLE Policies
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(HAN,PolicyName);

-- Query 1:
SELECT 
    A.AccountId, 
    A.Name, 
    A.Age, 
    A.City, 
    A.State, 
    A.Pincode, 
    C.Id AS ClaimId, 
    C.CreatedDate, 
    C.CaseNumber, 
    C.BillAmount, 
    C.Status, 
    P.HAN AS PolicyHAN, 
    P.PolicyName
FROM 
    Accounts A
INNER JOIN 
    Claims C ON A.AccountId = C.AccountId
INNER JOIN 
    Policies P ON C.HAN = P.HAN
WHERE 
    A.AccountId = '0012j00000GjoGnAAJ';
    
-- Query 2:
SELECT * 
FROM Claims 
WHERE AccountId = '0018p000007tIsVAAU';

-- Query 3:
SELECT DISTINCT AccountId 
FROM Claims;

-- Query 4:
SELECT C.HAN 
FROM Claims C 
WHERE C.AccountId = '0012j00000GjoGnAAJ';

-- Query 5:
INSERT INTO Claims (Id, CreatedDate, CaseNumber, HAN, BillAmount, Status, AccountId)
VALUES 
('123456789', '2024-07-01', 'CASE001', 'HAN123', 1000.50, 'Open', '0012j00000GjoGnAAJ');

-- Query 6:
INSERT INTO Policies (HAN, PolicyName)
VALUES 
('HAN123', 'Life Insurance');

-- Query 7:
DELETE FROM Claims 
WHERE HAN = '01CHSP0000002222' LIMIT 1;

-- Query 8:
SELECT 
    A.AccountId, 
    A.Name, 
    A.Age, 
    A.City, 
    A.State, 
    A.Pincode, 
    C.Id AS ClaimId, 
    C.CreatedDate, 
    C.CaseNumber, 
    C.BillAmount, 
    C.Status, 
    P.PolicyName
FROM 
    Accounts A
INNER JOIN 
    Claims C ON A.AccountId = C.AccountId
INNER JOIN 
    Policies P ON C.HAN = P.HAN
WHERE 
    C.Status = 'Paid';
    
-- Query 9:
SELECT 
    Status, 
    COUNT(*) AS TotalClaims
FROM 
    Claims
GROUP BY 
    Status;
    
-- Query 10:
SELECT 
    Id, 
    AccountId, 
    HAN, 
    BillAmount, 
    CreatedDate, 
    Status
FROM 
    Claims
ORDER BY 
    BillAmount DESC
LIMIT 5;

-- Query 11:
SELECT 
    P.HAN, 
    P.PolicyName
FROM 
    Policies P
LEFT JOIN 
    Claims C ON P.HAN = C.HAN
WHERE 
    C.HAN IS NULL;
    
-- Query 12:
UPDATE 
    Claims
SET 
    Status = 'Unpaid'
WHERE 
    Id = '500OA00000FX0aqYAD';





 


SELECT User, Host, authentication_string FROM mysql.user;

ALTER USER 'root'@'localhost' IDENTIFIED BY '7861';

