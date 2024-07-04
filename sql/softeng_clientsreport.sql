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
-- Table structure for table `clientsreport`
--

DROP TABLE IF EXISTS `clientsreport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientsreport` (
  `Client_ID` int NOT NULL AUTO_INCREMENT,
  `Client_Name` varchar(90) NOT NULL,
  `Coach_Name` varchar(100) NOT NULL,
  `Completed_Sessions` int NOT NULL DEFAULT '0',
  `Sessions_Left` int NOT NULL DEFAULT '0',
  `Package_Type` varchar(100) NOT NULL,
  PRIMARY KEY (`Client_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientsreport`
--

LOCK TABLES `clientsreport` WRITE;
/*!40000 ALTER TABLE `clientsreport` DISABLE KEYS */;
INSERT INTO `clientsreport` VALUES (1,'Cruz','Ezekiel Gebala',12,0,'Private Package'),(2,'Myek Jego','Jeffrey Stonks',12,0,'Private Package'),(3,'09845527624','Jeffrey Stonks',10,0,'Private Package'),(4,'09845527624','Jeffrey Stonks',10,0,'Private Package'),(5,'Cruz','Jeffrey Stonks',6,0,'Private Package'),(6,'myek','Jeffrey Stonks',8,0,'Private Package'),(7,'myek','Ezekiel Gebala',8,0,'Public Package'),(8,'myek','Jeffrey Stonks',8,0,'Private Package'),(9,'myek','Jeffrey Stonks',8,0,'Private Package'),(10,'markreyes','Jeffrey Stonks',6,0,'Private Package'),(11,'myek','Ezekiel Gebala',6,0,'Private Package'),(12,'king','Jeffrey Stonks',6,0,'Public Package'),(13,'king','Ezekiel Gebala',6,0,'Private Package');
/*!40000 ALTER TABLE `clientsreport` ENABLE KEYS */;
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
