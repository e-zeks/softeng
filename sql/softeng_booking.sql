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
-- Table structure for table `booking`
--

DROP TABLE IF EXISTS `booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `booking` (
  `BookingID` int NOT NULL AUTO_INCREMENT,
  `Coach_Name` varchar(100) DEFAULT NULL,
  `Client_Name` varchar(100) DEFAULT NULL,
  `Program_Plan` varchar(255) DEFAULT NULL,
  `Package_Name` varchar(100) DEFAULT NULL,
  `Session_Count` int DEFAULT NULL,
  `Total_Price` decimal(10,2) DEFAULT NULL,
  `Status` enum('paid','unpaid') NOT NULL DEFAULT 'unpaid',
  PRIMARY KEY (`BookingID`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking`
--

LOCK TABLES `booking` WRITE;
/*!40000 ALTER TABLE `booking` DISABLE KEYS */;
INSERT INTO `booking` VALUES (1,'Ezekiel Gebala','Cruz','Body Building','Private Package',12,5500.00,'paid'),(2,'Jeffrey Stonks','Myek Jego','Body Building','Private Package',12,5500.00,'paid'),(3,'Jeffrey Stonks','09845527624','Body Building','Private Package',10,4500.00,'paid'),(4,'Jeffrey Stonks','09845527624','Body Building','Private Package',10,4500.00,'paid'),(5,'Jeffrey Stonks','Cruz','Body Building','Private Package',6,2500.00,'paid'),(6,'Jeffrey Stonks','myek','Body Building','Private Package',8,3500.00,'paid'),(7,'Ezekiel Gebala','myek','Body Building','Public Package',8,3000.00,'paid'),(8,'Jeffrey Stonks','myek','Body Building','Private Package',8,3500.00,'paid'),(9,'Jeffrey Stonks','myek','Body Building','Private Package',8,3500.00,'paid'),(10,'Jeffrey Stonks','markreyes','Weight Loss','Private Package',6,2500.00,'paid'),(11,'Ezekiel Gebala','myek','Body Building','Private Package',6,2500.00,'paid'),(12,'Jeffrey Stonks','king','Calisthenics','Public Package',6,2000.00,'unpaid'),(13,'Ezekiel Gebala','king','Calisthenics','Private Package',6,2500.00,'unpaid'),(14,'Ezekiel Gebala','myek','Body Building','Public Package',8,3000.00,'paid'),(15,'Jeffrey Stonks','myek','Body Building','Private Package',8,3500.00,'paid'),(16,'Jeffrey Stonks','myek','Body Building','Private Package',8,3500.00,'paid');
/*!40000 ALTER TABLE `booking` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-04 16:10:05
