CREATE TABLE `user_logs` (
    `LogID` int NOT NULL AUTO_INCREMENT,
    `EmployeeID` int DEFAULT NULL,
    `ClientID` int DEFAULT NULL,
    `UserType` enum('Employee', 'Client') NOT NULL,
    `First_Name` varchar(45) NOT NULL,
    `Last_Name` varchar(45) NOT NULL,
    `Login_Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `Logout_Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`LogID`),
    FOREIGN KEY (`EmployeeID`) REFERENCES `employees`(`EmployeeID`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (`ClientID`) REFERENCES `clients`(`ClientID`) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE user_logs
SELECT * FROM user_logs