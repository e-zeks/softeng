-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: softeng
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `client_sessions_summary`
--

DROP TABLE IF EXISTS `client_sessions_summary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `client_sessions_summary` (
  `SummaryID` int NOT NULL AUTO_INCREMENT,
  `Client_Name` varchar(100) DEFAULT NULL,
  `Coach_Name` varchar(100) DEFAULT NULL,
  `Package_Name` varchar(100) DEFAULT NULL,
  `Completed_Sessions` int DEFAULT NULL,
  `Status` enum('Completed','Cancelled','Not Done') DEFAULT NULL,
  PRIMARY KEY (`SummaryID`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client_sessions_summary`
--

LOCK TABLES `client_sessions_summary` WRITE;
/*!40000 ALTER TABLE `client_sessions_summary` DISABLE KEYS */;
INSERT INTO `client_sessions_summary` VALUES (1,'Cruz','Ezekiel Gebala','Private Package',0,''),(2,'Myek Jego','Jeffrey Stonks','Private Package',0,''),(3,'09845527624','Jeffrey Stonks','Private Package',0,''),(4,'myek','Jeffrey Stonks','Private Package',0,''),(5,'myek','Ezekiel Gebala','Public Package',0,''),(6,'markreyes','Jeffrey Stonks','Private Package',0,''),(7,'myek','Ezekiel Gebala','Private Package',6,'Not Done'),(8,'king','Jeffrey Stonks','Public Package',0,'Not Done'),(9,'king','Ezekiel Gebala','Private Package',6,'Not Done'),(10,'myek','Ezekiel Gebala','Public Package',0,'Not Done'),(11,'myek','Jeffrey Stonks','Private Package',0,'Not Done'),(12,'rofl','Ezekiel Gebala','Private Package',0,'Not Done'),(13,'iamJCDC','Ezekiel Gebala','Private Package',0,'Not Done');
/*!40000 ALTER TABLE `client_sessions_summary` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-09 19:29:53
