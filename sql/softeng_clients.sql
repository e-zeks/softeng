-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: softeng
-- ------------------------------------------------------
-- Server version	8.0.37

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `clients`
--

DROP TABLE IF EXISTS `clients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clients` (
  `ClientID` int NOT NULL AUTO_INCREMENT,
  `Last_Name` varchar(45) NOT NULL,
  `First_Name` varchar(45) NOT NULL,
  `Address` varchar(99) NOT NULL,
  `Birthdate` date NOT NULL,
  `Contact_Number` varchar(11) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Username` varchar(45) NOT NULL,
  `Password` varchar(64) NOT NULL,
  `Program_Plan` varchar(45) NOT NULL,
  `Conditions` varchar(45) DEFAULT NULL,
  `LOA` varchar(15) DEFAULT 'Client',
  PRIMARY KEY (`ClientID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clients`
--

LOCK TABLES `clients` WRITE;
/*!40000 ALTER TABLE `clients` DISABLE KEYS */;
INSERT INTO `clients` VALUES (1,'Cruz','Myek Jego','1234 Mango Street, Barangay San Antonio, Pasig City','2000-05-16','09845527624','myek@gmail.com','myek','134563d4e440f0e418b0f382f23a2cf301af6d7f648ccfae9895018345d779a3','Body Building','','Client'),(2,'Tate','Andrew','567 Mahogany Street, Barangay Santo Tomas, Quezon City','2002-12-10','09845776145','lootboxorloottraps@gmail.com','king','134563d4e440f0e418b0f382f23a2cf301af6d7f648ccfae9895018345d779a3','Calisthenics','','Client'),(3,'Reyes','Mark','432 Sunflower Drive, Barangay Bagong Pag-asa, Mandaluyong City','2000-01-01','09053530823','markshjasf@gmail.com','markreyes','134563d4e440f0e418b0f382f23a2cf301af6d7f648ccfae9895018345d779a3','Weight Loss','','Client'),(4,'Dela Cruz','Jan Carlos','Cainta Rizal','2002-07-04','09053530823','myek2@gmail.com','iamJCDC','134563d4e440f0e418b0f382f23a2cf301af6d7f648ccfae9895018345d779a3','Weight Loss','','Client'),(5,'Raphael','Garcia','11 Homestead Drive, Cainta, Rizal','2002-02-24','09152637208','rm.garcia1729@gmail.com','rofl','9d12d5ea282c58aa5f092ade6818f01a8059ee6067725c1a5a966506c5eff121','Weight Loss','N/A','Client');
/*!40000 ALTER TABLE `clients` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-09  1:29:02
